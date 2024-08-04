import streamlit as st
from SnapScrib.youtube_audio.extract_audio import download_youtube_video_as_audio
from backend.modules.yt_thumbnail import download_thumbnail
import time

class Home():
    def __init__(self):
        self.link = 'https://www.youtube.com/watch?v=jrElyXgqrss'
        
        self.valid_link = True

    # bestaetigung der abfrage 
    # herunterladen der untertitel 
    # video soll auf seite laufen


    def load_button(self):
        pass

    def video_preview(self):
        pass

    def result_text_box(self):
        pass

    def link_input(self):
        self.link = st.chat_input(placeholder='Enter the link here', max_chars=None)

        self.check_link()

    def check_link(self):
        if self.link:
            st.error('Please enter a valid YouTube link.')
            self.valid_link = False

        
        with st.status('Processing...') as  status:
            #while not self.valid_link:
            #time.sleep(1)

            st.write('Checking link...')
            st.write('Found URL')

            while not self.download() and not self.thumbnail():
                time.sleep(1)

            st.success('Download completed!')
        
    def download(self):
        download_youtube_video_as_audio(self.link)

    def thumbnail(self):
        path = 'tests/thumbnail.jpg'
        if self.link:
            download_thumbnail(self.link, path)
        else:
            st.error('Please enter a valid YouTube link.')

    def surface(self):
        self.link_input()


home = Home()
home.surface()


#variables from yt_dlp:
#    title (str)
#    creators (list)
#    duration_string (str)
