import tweepy
import time
auth = tweepy.OAuthHandler('<consumer key', '<consumer secret>')  #inclues consumer key and consumer secret
auth.set_access_token('<Api key>', '<API secret>') #api key and secret

api = tweepy.API(auth)

user = api.me()

'''print(user.name)
print(user.screen_name)
print(user.followers_count)'''

#super generous bot follow back
def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()

    except tweepy.RateLimitError:
        time.sleep(1000)

# for follower in (tweepy.Cursor(api.followers).items()):
#     if follower.name == 'Bhavy':
#         follower.unfollow()
#         break
#     print(follower.name)
    

search_string = 'python'
numberOFtweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOFtweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.error)
    except StopIteration:
        break



