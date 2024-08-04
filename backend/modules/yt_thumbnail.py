import pytube 
import urllib.request

def download_thumbnail(url):
    try:
        video = pytube.YouTube(url)
        thumbnail = video.thumbnail_url
        path = 'tests/thumbnail.jpg'
        urllib.request.urlretrieve(thumbnail, path)
        print("Thumbnail downloaded successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

path = 'https://www.youtube.com/watch?v=6d3LwuTIOeQ'
download_thumbnail(path)