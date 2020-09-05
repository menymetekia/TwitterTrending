# from searchtweets import ResultStream, load_credentials, gen_rule_payload, collect_results, api_utils
#
# def get_tweets(start_time,location):
#     # search_args = load_credentials("./twitter_keys.yaml",
#     #                                yaml_key="search_tweets_v2",
#     #                                env_overwrite=False)
#     #
#     # # query = gen_rule_payload("test",results_per_call=100,tweet_fields="entities",start_time=start_time,)
#     # query = gen_rule_payload("test", results_per_call=100)
#     #
#     # #Better
#     # rs = ResultStream(rule_payload=query,
#     #                     max_results=10,
#     #                     max_pages=1, **search_args)
#     #
#     # tweets = list(rs.stream())
#     # return tweets
#
# get_tweets(0,0)

import tweepy
consumer_key = "OLcLHYFi7tbr48XhV7TdLMju1"
consumer_secret = "XX6FoV9l0LO7HuxtbdF7b6PRfUQwKnSZ6blJwsbYeqVLYAcMcA"
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

api = tweepy.API(auth)
amsterdam_geo = "52.379189,4.899431,20km"

def get_tweets(since,location):
    query = 'since:2015-12-21'
    max_tweets = 1000
    test = [status for status in tweepy.Cursor(api.search, q=query,geocode=amsterdam_geo).items(max_tweets)]
    tweets = [{"text":t.text,"hashtags":t.entities["hashtags"]} for t in test]
    return tweets

print(get_tweets(0,0))