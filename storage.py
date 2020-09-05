import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["twitter_db"]

mycol = mydb["tweets_2"]

mydict = { "name": "John", "address": "Highway 37" }

def insert_tweets(tweets):
    mycol.insert_many(tweets)


pipeline = [
    { "$unwind": "$entities.hashtags" },
    { "$sortByCount": "$entities.hashtags.tag" }
    #{ "$group": { "_id": "$entities.hashtags.tag", "TotalFrequency": { "$sum" : 1 } } }
]

agg = list(mycol.aggregate(pipeline))
print(agg)