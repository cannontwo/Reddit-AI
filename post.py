__author__ = 'cannon'

import praw
import requests
import time
import datetime
import analysis_n

while True:
    try:
        r = praw.Reddit(user_agent='Bot to scrape post title text by u/Cannon10100')
        r.login()
        break
    except requests.exceptions.HTTPError as e:
        if e.response.status_code in [429, 500, 502, 503, 504]:
            print "Reddit is down (error %s), sleeping..." % e.response.status_code
            time.sleep(30)
            pass
        else:
            raise
    except Exception as e:
        print "Couldn't do Reddit stuff: %s" % str(e)
        raise

title = 'Expected Title for ' + str(datetime.date.today()) + ' at ' + str(time.time())
my_text = '2nd order 40-char title: ' + str(analysis_n.analyze(2))
r.submit(r.get_subreddit('expectedreddit'), title, text=my_text)
