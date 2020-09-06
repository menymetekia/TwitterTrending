import tweepy
import storage
from datetime import datetime, timedelta, timezone
consumer_key = "OLcLHYFi7tbr48XhV7TdLMju1"
consumer_secret = "XX6FoV9l0LO7HuxtbdF7b6PRfUQwKnSZ6blJwsbYeqVLYAcMcA"
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

api = tweepy.API(auth)
amsterdam_geo = "52.379189,4.899431,20km"

def get_tweets(since,location):
    query = ''
    max_pages = 3
    amount_of_pages = 0
    pages = tweepy.Cursor(api.search, q=query,geocode=amsterdam_geo,count=100).pages()
    for page in pages:
        continue_value = process_tweets(page)
        amount_of_pages += len(page)
        print("Inserted " + str(amount_of_pages) + " pages")
        if not continue_value:
            break


def process_tweets(page):
    tweets = []
    for t in page:
        if check_date(t.created_at):
            tweets.append({"date":t.created_at,"text":t.text,"hashtags":t.entities["hashtags"]})
        else:
            return False
    storage.insert_tweets(tweets)
    return True

def check_date(date,last_x_hours=1):
    last_hour_date_time = datetime.utcnow() - timedelta(hours=last_x_hours)
    if date <= last_hour_date_time:
        return False
    return True

#print(check_date(""))
get_tweets(0,0)