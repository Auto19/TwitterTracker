import tweepy
import time
import smtplib
#from credentials import *

UsersTweet = ""
UsersOldTweet = ""

P = raw_input("Who do you want to track (please use twitter account name without @ sign): ")

while True:
    

    CONSUMER_KEY = 'CONSUMER_KEY'
    CONSUMER_SECRET = 'CONSUMER_SECRET'
    ACCESS_KEY = 'ACCESS_KEY'
    ACCESS_SECRET = 'ACCESS_SECRET'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    stuff = api.user_timeline(screen_name = P, count = 1, include_rts = True)

    for status in stuff:
        UsersTweet = status.text

    UsersTweet = UsersTweet.encode('ascii', 'ignore').decode('ascii')
    if(not(UsersTweet == UsersOldTweet)):
        fromaddr = 'fromaddr@gmail.com'
        toaddrs  = 'toaddrs@gmail.com'
        msg = "\n " + P + " tweeted: " + "\n " + UsersTweet
        username = 'fromaddr@gmail.com'
        password = 'password'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg)
        
        
        server.quit()

        print "Sent Lastest Tweet"

        print UsersTweet
    else:
        print "No new tweets since last check"
        
    UsersOldTweet = UsersTweet

    time.sleep(30)

    

    

