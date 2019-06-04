#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import sys

import pandas as pd
import twitter
from requests_oauthlib import OAuth1Session


# In[2]:


consumer_key = os.environ["CONSUMER_KEY"]
consumer_secret = os.environ["CONSUMER_SECRET"]
access_token = os.environ["ACCESS_TOKEN_KEY"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]


# In[3]:


def return_twitter_api():

    api = twitter.Api(consumer_key=consumer_key,
                          consumer_secret=consumer_secret,
                          access_token_key=access_token,
                          access_token_secret=access_token_secret)

    return api


# In[4]:


def delete_tweets(tweet_ids):
    api = return_twitter_api()
    count = 0
    

    
    for id in tweet_ids:
        status = None
        
        try:
            status = api.DestroyStatus(id)
        except:
            if  'No status found with that ID.':
                continue
        finally:
            if status != None:
                count += 1
            else:
                pass

        
    return print("{}件のツイートを消去しました。".format(count))


# In[5]:


tweet_df = pd.read_csv("/hoge/tweets.csv")


# In[6]:


tw_id_and_text_df = tweet_df.reindex(columns=["timestamp", "tweet_id", "text"])


# In[7]:


print("消したい単語を入力してください。複数の単語を入力するにはスペースで区切る（cを入力でキャンセル）")
input_words = input().split()
if input_words == "c" or "C":
    sys.exit()
else:
    pass


# In[8]:


wanna_delete_words = "|".join(input_words)
wanna_delete_df = tw_id_and_text_df[tw_id_and_text_df["text"].str.contains(wanna_delete_words) == True]


# In[9]:


wd_tweet_ids = wanna_delete_df["tweet_id"]


# In[10]:


columns = ["timestamp", "text"]
new_df = wanna_delete_df.reindex(columns=columns)


# In[11]:


print(new_df)
print("対象ツイートは{}件あります。実行しますか？ y/N".format(len(wd_tweet_ids)))
ans = input()

if ans == "y":
    delete_tweets(wd_tweet_ids)
else:
    print("キャンセルしました。")

