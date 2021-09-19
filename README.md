# twitter-scraping-bot
developed in python using tweepy API, pandas to compile collected tweets into table, and textblob to perform sentiment analysis

you can put in whatever text you want for the subject and this script will compile recent 100 tweets regarding that individual or topic and put it all into a CSV file with the tweet text, date/time posted, and a feeling associated with it

used textblob to generate sentiment analysis for the text from each tweet ( output > 0 means positive feeling, output == 0 means neutral, output < 0 means negative)

returns a csv file and prints whether public sentiment involving subject of choice is positive or negative
