# "John Bot" Source (generic version)
# A Twitter bot by wizardidiot
# Tweets a source text file one word at a time.

import tweepy
import time

# Setup time!
waitInMins = 120 # Time between tweets
wordSourcePath = "myTextFile.txt" # path to text file with words to be tweeted.

# Twitter App keys from apps.twitter.com
consumerKey = ''
consumerSecret = ''
accessKey = ''
accessSecret = ''

# You don't need to change this one.
count = 0

# Log into Twitter w/ OAuth

print("Bot Accessing Twitter")

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessKey, accessSecret)
api = tweepy.API(auth)

print("Access successful. Priming text file contents...")

# Open file, split into lines then words, tweet each, then wait.

wordSource = open(wordSourcePath, 'r')

print("Begin tweet cycle.")

try:
    for line in wordSource:
        words = line.split()
        for word in words:
            api.update_status(word) # Tweet!
            count += 1
            print("Tweeted: " + word + " (Word Number: " + str(count) + ")")
            print("Waiting for " + str(waitInMins) + " mins.\n")
            time.sleep(waitInMins * 60)
except KeyboardInterrupt:
    print("Interrupt accepted. Shutting down.")
    wordSource.close()
    exit()

print("It's finally over. Closing speech file.")

speech.close()

print("Tata!")
