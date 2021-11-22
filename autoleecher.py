import requests
from os.path import exists
import urllib.request
import subprocess

def saveVideo(url, title): # Use youtube-dl to parse the twitch clip, so we don't have to do the dirty optimization
    if exists('\\Videos\\' + title + '.mp4') != True:
        if 'twitch' in url:
            print('A new clip is being downloaded...', title[:30])
            output = subprocess.run(['youtube-dl', url, '-o', title + '.mp4'], capture_output=True).stdout.decode()
            print(output)
    else:
        print('We\'ve already downloaded that file...')

if __name__ == "__main__":
    url = 'https://www.reddit.com/r/LivestreamFail/top/.json' # Expanding to other URLs by using a for loop to iterate over different amounts of URLs, indiviudal subreddits...
    r = requests.get(url, headers= {'User-agent': 'something'}) # To bypass reddit preventing our requests, I would change this for your purpose...

    for i in r.json()['data']['children']:
        saveVideo(i['data']['url_overridden_by_dest'], i['data']['title'])
