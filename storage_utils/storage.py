import pymongo
import yaml
from datetime import datetime, timedelta

def initialize_db():
    config = yaml.safe_load(open("./config.yaml"))
    myclient = pymongo.MongoClient(config["mongo_client_location"])
    mydb = myclient[config["mongo_db"]]
    mycol = mydb[config["mongo_collection"]]
    return mycol

def insert_ingestion_data(mycol):
    """Insert general information about the ingestion"""
    mycol.insert({"type":"info","reference_datetime":datetime.utcnow()})

def insert_tweets(mycol,tweets):
    """Insert a batch of tweets"""
    mycol.insert_many(tweets)

def get_reference_date(mycol):
    """Get the date and time the ingestion took place on"""
    return mycol.find_one({"type":"info"})["reference_datetime"]

def getTrends(mycol,amount_trends=5,last_x_hours=1):
    """Get the trends for a specified date time range"""
    reference = get_reference_date(mycol)
    since = reference - timedelta(hours=last_x_hours)
    ### MongoDB aggregation framework pipeline that gets tweets for a requested date
    ### and calculates the frequency of hashtags within tweets ##
    pipeline = [
        { "$match":{"date": { "$gt": since }} },
        { "$unwind": "$hashtags" },
        { "$sortByCount": "$hashtags.text" }
    ]
    agg = list(mycol.aggregate(pipeline))[:amount_trends]
    date_format = "%m/%d/%Y, %H:%M:%S"
    return {"since":since.strftime(date_format),"until":reference.strftime(date_format),"trends":agg}