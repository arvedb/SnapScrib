import pytube 
import urllib.request

def download_thumbnail(url, path):
    try:
        video = pytube.YouTube(url)
        thumbnail = video.thumbnail_url
        urllib.request.urlretrieve(thumbnail, path)
        print("Thumbnail downloaded successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = 'https://www.youtube.com/watch?v=jrElyXgqrss'
    path = 'tests/thumbnail.jpg'
    download_thumbnail(url, path)