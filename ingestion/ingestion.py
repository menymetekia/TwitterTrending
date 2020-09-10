import tweepy
from tweepy import TweepError
from storage_utils import storage
from datetime import datetime, timedelta
import yaml
import argparse

def get_tweets(api,collection,since,geo_location):
    """Retrieve tweets using the tweepy twitter API"""
    query = 'lang:en OR lang:nl' #Get tweets only in english or dutch
    amount_of_pages = 0
    # Use the query to find all tweets in a certain geolocation
    pages = tweepy.Cursor(api.search, q=query,geocode=geo_location,count=1000).pages()
    try:
        storage.insert_ingestion_data(collection)
        for page in pages: #Tweets are retrieved in pages/batches of approx. 100 tweets each
            continue_value = process_tweets(collection,page,since)
            amount_of_pages += len(page)
            print("Inserted " + str(amount_of_pages) + " tweets")
            if not continue_value:
                break
    except TweepError:
        print("Reached rate limit")


def process_tweets(collection, page,since):
    """Process each tweet within a page"""
    tweets = []
    for t in page:
        if check_date(t.created_at,since):
            tweets.append({"type":"tweet","date":t.created_at,"text":t.text,"hashtags":t.entities["hashtags"]})
        else:
            return False
    storage.insert_tweets(collection, tweets)
    return True


def check_date(date,last_x_hours=1):
    """Check if the date of a tweet is not older than the specified range we want to search for"""
    last_hour_date_time = datetime.utcnow() - timedelta(hours=last_x_hours)
    return not date <= last_hour_date_time

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Imports xml file for a given amount of days and returns current stock')
    parser.add_argument('amount_hours', type=int, default=72,
                        help='Amount of hours to go back when retrieving tweets')
    args = parser.parse_args()

    config = yaml.safe_load(open("./config.yaml"))
    auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
    api = tweepy.API(auth)
    geo_location = config["geo_location"]

    collection = storage.initialize_db()
    get_tweets(api,collection,args.amount_hours,geo_location)