'''Posts a test tweet that says "Jenny smells" as the caption,
with the picture of New Jeans' EP "Get Up" '''
import tweepy
import keys
import time

client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
auth = tweepy.OAuth1UserHandler(keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
api = tweepy.API(auth)

time.sleep(5)

media = api.media_upload("get-up.png")

#client.create_tweet(direct_message_deep_link (str | None)  for_super_followers_only (bool | None) place_id (str | None) media_ids (list[int | str] | None) media_tagged_user_ids (list[int | str] | None) poll_duration_minutes (int | None) poll_options (list[str] | None) quote_tweet_id (int | str | None) exclude_reply_user_ids (list[int | str] | None) in_reply_to_tweet_id (int | str | None) reply_settings (str | None) text (str | None) user_auth (bool) )
client.create_tweet(text="Jenny smells", media_ids = [media.media_id], user_auth = True)