'''Creates a client using Twitter API then uses this to post a Tweet 
using the media and the caption from get_media.py'''

import tweepy
import keys
import time
from datetime import datetime
import get_media

client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
auth = tweepy.OAuth1UserHandler(keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
api = tweepy.API(auth)

time.sleep(5)

todays_date = datetime.today().date().strftime("%Y-%m-%d")
post_data = get_media.get_posts(username='XXX', password='XXX')
print(post_data)
file_destination = r'C:\Users\r4che\Downloads\tweet_poster\posts\New Post ' + str(todays_date) + "\\"

for data in post_data:
    media_ids = []
    caption = '' if not data[0] else data[0] #assign empty string to the caption if there is no caption
    print(caption)

    for i in range(1, len(data)):
        for media in data[i]:
            file_name = file_destination + media
            m = api.media_upload(file_name)
            media_id = m.media_id
            media_ids.append(media_id)
            print(media_ids)

        client.create_tweet(text = caption, media_ids= media_ids, user_auth = True)
        media_ids = []
    

