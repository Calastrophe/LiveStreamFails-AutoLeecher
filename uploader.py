import datetime
import os
from Google import Create_Service
from googleapiclient.http import MediaFileUpload


def deleteVideo(path):
    print("Now removing the file... ", path)
    try:
        os.remove(path)
    except:
        print("There was an error in deleting a file...")
        exit(-1)

def uploadVideo(csfilepath, path, title, publishtime):
    service = Create_Service(csfilepath, 'youtube', 'v3', ['https://www.googleapis.com/auth/youtube.upload'])
    print("I'm uploading ", title," at ", publishtime)

    request_body = {
    'snippet': {
        'categoryI': 19,
        'title': title,
        'description': 'new software | github.com/calastrophe',
        'tags': ['software', 'twitch test', 'twitch clips']
    },
    'status': {
        'privacyStatus': 'private',
        'publishAt': publishtime,
        'selfDeclaredMadeForKids': False,
    },
    'notifySubscribers': True
    }

    mediaFile = MediaFileUpload(path)
    response_upload = service.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=mediaFile
    ).execute()

    service.thumbnails().set(
        videoId=response_upload.get('id'),
        media_body=MediaFileUpload('thumbnail.png')
    ).execute()
    deleteVideo(path)
