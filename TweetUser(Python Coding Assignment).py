''' Find who tweeted the most ''' 

from collections import Counter

def max_tweet_user(tweeters):
    max_key_values = max(tweeters.values())
    max_tweeter = ([key for key in tweeters.keys() if tweeters[key]==max_key_values])
    max_tweeter.sort() # sort the list by alphabetical order
    return max_tweeter

t = int(input())
for _ in range(t):
    n = int(input())
    names = []
    for _ in range(n):
        user_name,tweet_id = map(str,input().split())
        names.append(user_name)
    tweeters = dict(Counter(names))  #strings along with their frequency in dict
    user_list = max_tweet_user(tweeters)
    for i in range(0,len(user_list)):
        print(user_list[i],tweeters[user_list[i]])
   
        
    
    
                
