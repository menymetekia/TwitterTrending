import tweepy
from tweepy import TweepError
import storage
from datetime import datetime, timedelta
import yaml

config = yaml.safe_load(open("./config.yaml"))
auth = tweepy.OAuthHandler(config["consumer_key"],config["consumer_secret"])
api = tweepy.API(auth)

geo_location = config["geo_location"]

def get_tweets(since):
    query = 'lang:en OR lang:nl'
    amount_of_pages = 0
    pages = tweepy.Cursor(api.search, q=query,geocode=geo_location,count=100).pages()
    try:
        storage.insert_ingestion_data()
        for page in pages:
            continue_value = process_tweets(page,since)
            amount_of_pages += len(page)
            print("Inserted " + str(amount_of_pages) + " pages")
            if not continue_value:
                break
    except TweepError:
        print("Reached rate limit")


def process_tweets(page,since):
    tweets = []
    for t in page:
        if check_date(t.created_at,since):
            tweets.append({"type":"tweet","date":t.created_at,"text":t.text,"hashtags":t.entities["hashtags"]})
        else:
            return False
    storage.insert_tweets(tweets)
    return True

def check_date(date,last_x_hours=1):
    last_hour_date_time = datetime.utcnow() - timedelta(hours=last_x_hours)
    return not date <= last_hour_date_time

#print(check_date(""))
get_tweets(72)