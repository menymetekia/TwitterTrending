import argparse
import ingestion,storage

"""Command line file to view stock and herd for a given XML file and elapsed days"""

parser = argparse.ArgumentParser(description='Imports xml file for a given amount of days and returns current stock')
parser.add_argument('amount_hours', type=str, default="72h",
                   help='Amount of hours to go back when retrieving tweets')
parser.add_argument('location', type=int,
                   help='Location we want to get trends from')
args = parser.parse_args()

tweets = ingestion.get_tweets(args.amount_hours,"")
storage.insert_tweets(tweets)

