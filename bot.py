#!/usr/bin/python
__author__ = 'cannon'

import praw
import string
import datetime
import os
import time
import analysis

already_stored = []
start_time = time.time()

r = praw.Reddit(user_agent='Bot to scrape post title text by u/Cannon10100')
r.login('expected_reddit', 'lewis678')

files = [f for f in os.listdir('./text') if os.path.isfile("./text/" + f)]
for f in files:
    if f.endswith(".txt"):
        with open("./text/" + f, "r") as read_file:
            for line in read_file:
                params = string.rsplit(line, "***")
                already_stored.append(string.replace(params[1], "\n", ""))

print already_stored

while True:
    today = datetime.date.today()
    subreddit = r.get_subreddit('funny')

    with open("./text/" + str(today) + ".txt", "a") as store_file:
        for submission in subreddit.get_hot(limit=20):
            if submission.id not in already_stored and submission.score > 1000:
                store_file.write(str(string.replace(submission.title, '.', '')) + "***" + submission.id + "\n")
                already_stored.append(submission.id)
                print "Stored ID: %s" % submission.id
            else:
                print "Already stored ID: %s" % submission.id

    time.sleep(600)

    if time.time() > start_time + 86400:
        start_time = time.time()
        r.submit("expectedreddit", "Expected title for stardate %s" % datetime.today(), text=analysis.analyze())
