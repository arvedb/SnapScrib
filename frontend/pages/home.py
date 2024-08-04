import streamlit as st
from SnapScrib.youtube_audio.extract_audio import download_youtube_video_as_audio

class Home():
    def __init__(self):
        pass

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
        self.link = st.chat_input(placeholder='Enter the link here', max_chars=None, )

        self.check_link()

    def check_link(self):
        if not self.link:
            st.error('Please enter a valid YouTube link.')

        with st.status('Processing...'):
            st.write('Checking link...')
            
            st.write('Found URL')

            st.write('')

    def downloading(self):
        download_youtube_video_as_audio(self.link)
        st.success('Download completed!')

    def surface(self):
        self.link_input()


home = Home()
home.surface()

"""
variables from yt_dlp:
    title (str)
    creators (list)
    duration_string (str)
"""