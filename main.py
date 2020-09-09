import argparse
import ingestion,storage

"""Command line file to view stock and herd for a given XML file and elapsed days"""

parser = argparse.ArgumentParser(description='Imports xml file for a given amount of days and returns current stock')
parser.add_argument('amount_hours', type=int, default=72,
                   help='Amount of hours to go back when retrieving tweets')
args = parser.parse_args()

ingestion.get_tweets(args.amount_hours)

