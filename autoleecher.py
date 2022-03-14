import requests
from os.path import exists
import urllib.request
import subprocess
import datetime
import uploader

def checkTitles(title):
    with open('titles.txt') as f:
        for line in f:
            if line.strip() == title:
                return True
    return False

def calculatePublishTime():
    td = datetime.timedelta(minutes=5)
    upload_date_time = datetime.datetime.now() + td
    new_uploadtime = upload_date_time.isoformat()[:19] + '.000Z'
    return new_uploadtime

def saveVideo(url, title): # Use youtube-dl ro parse the twitch clip, so we don't have to do the dirty optimization
    path = (title + '.mp4')
    if checkTitles(title) != True:
        if 'twitch' in url:
            print('A new clip is being downloaded...')
            subprocess.run(['youtube-dl', url, '-o', path])
            uploader.uploadVideo(cs_file, path, title, calculatePublishTime())
            with open('titles.txt') as f:
                f.write(title)
        else:
            print("We've found a non-twitch clip, skipping...")
    else:
        print('We\'ve already downloaded that file...')

if __name__ == "__main__":
    cs_file = 'client_secret.json' # For the uploading portion, feel free to comment it out if need be...
    url = 'https://www.reddit.com/r/LivestreamFail/top/.json' # Expanding to other URLs by using a for loop to iterate over different amounts of URLs, indiviudal subreddits...
    r = requests.get(url, headers= {'User-agent': 'something'}) # To bypass reddit preventing our requests, I would change this for your purpose...

    for i in r.json()['data']['children']:
        saveVideo(i['data']['url_overridden_by_dest'], i['data']['title'])
