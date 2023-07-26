'''The program to take media from Instagram was inspired by @nang on YT, who has a very cool video on 
how to automate your own meme compilation channel on YT! Here is the link to the repository I took the code from and also his YT channel.
GitHub: https://github.com/nathan-149/automated_youtube_channel
YT channel: https://www.youtube.com/@nang88
'''

from datetime import datetime, timedelta
import instaloader
import os

'''Scrape the Instagram profiles of an account's following list
for the post today they posted (at the current date).
@param username The username of the user to get the followees from.
@param password The password of the user to get the followees from.
@return A list of the data of each post taken:
        index 0: the type of post it is
        index 1: the caption (if it is a sidecar) or the media file name
        index 2 onwards: the sidecar posts if it is a sidecar
'''

def get_posts(username: str, password: str):
        
        today = datetime.today().date()
        print(today)
        folder_name = r"C:\Users\r4che\Downloads\tweet_poster\posts\New Post " + today.strftime('%Y-%m-%d')

        L = instaloader.Instaloader(dirname_pattern=folder_name, download_videos = False)
        #we only need the media from the post to be downloaded
        L.save_metadata_json = False 
        L.save_caption = False

        L.login(username, password)
        profile = instaloader.Profile.from_username(L.context, username)
        following_list = profile.get_followees()

        post_data = []

        for followee in following_list:
            print(followee.username)
            posts = followee.get_posts() #get all of the followee's posts
            for post in posts:
                print(post.date_utc)
                if post.date.date() >= today:
                    
                    print(post.typename)
                    try:
                        data = []
                        if post.typename == 'GraphSidecar':
                            if not os.path.exists(folder_name):
                                os.mkdir(folder_name)
                            file_names = []
                            data.append(post.caption)
                            
                            #get filenames of the media
                            nodes = post.get_sidecar_nodes()
                            for index, node in enumerate(nodes):
                                file_name = str(post.date_utc).replace(":", "-").replace(" ", "_") + '_UTC_' + f'{index+1}' + '.jpg'
                                file_names.append(file_name)
                            data.append(file_names)
                            post_data.append(data)
                        else:
                            filename = L.format_filename(post, target=profile.username) + '.jpg'
                            data.append(post.caption)
                            data.append([filename])
                            post_data.append(data)
                        
                        #download post - for some reason it keeps giving a TypeError?
                        L.download_post(post, target = folder_name)

                    except Exception as e:
                         print("Could not download due to:")
                         print(e)
            
            post_data.reverse()
            
        return post_data
