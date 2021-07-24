import tweepy

auth = tweepy.OAuthHandler('ac9l9i1fJB1DfbufKeCKBfgvP', 'TEJ84Bb3oL6Vi0Tm8xI80WGMDQGSHnDjPe07rYbPm5JkRKdEBT')
auth.set_access_token('2554547677-H74578SGu8OBjOn3T8IpEsyMw9Hkuxwln3DSZNx', 'gN8KahU2bqTEF7SyYe7NxyUef2YS9CoJPhjalxDRV18ci')

api = tweepy.API(auth)

search_string = '66daysofdata'
NumOfTweets = 10

for tweet in tweepy.Cursor(api.search, search_string).items(NumOfTweets):
    try:
        tweet.favorite()
        print('I LIKED THAT TWEET')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break