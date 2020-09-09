import pymongo
import yaml
from datetime import datetime, timedelta

config = yaml.safe_load(open("./config.yaml"))
myclient = pymongo.MongoClient(config["mongo_client_location"])
mydb = myclient[config["mongo_db"]]
mycol = mydb[config["mongo_collection"]]

def insert_ingestion_data():
    mycol.insert({"type":"info","reference_datetime":datetime.utcnow()})

def insert_tweets(tweets):
    mycol.insert_many(tweets)

def get_reference_date():
    return mycol.find_one({"type":"info"})["reference_datetime"]

def getTrends(amount_trends=5,last_x_hours=1):
    reference = get_reference_date()
    since = reference - timedelta(hours=last_x_hours)
    pipeline = [
        { "$match":{"date": { "$gt": since }} },
        { "$unwind": "$hashtags" },
        { "$sortByCount": "$hashtags.text" }
    ]
    agg = list(mycol.aggregate(pipeline))[:amount_trends]
    date_format = "%m/%d/%Y, %H:%M:%S"
    return {"since":since.strftime(date_format),"until":reference.strftime(date_format),"trends":agg}

#getTrends(10,72)