from searchtweets import ResultStream, load_credentials, gen_request_parameters, collect_results, api_utils

def get_tweets(start_time,location):
    search_args = load_credentials("./twitter_keys.yaml",
                                   yaml_key="search_tweets_v2",
                                   env_overwrite=False)

    query = gen_request_parameters("",results_per_call=100,tweet_fields="entities",start_time=start_time,)

    #Better
    rs = ResultStream(request_parameters=query,
                        max_results=10,
                        max_pages=1, **search_args)

    tweets = list(rs.stream())
    return tweets