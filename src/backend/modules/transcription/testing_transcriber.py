import sys
import os

from numpy import source

from transcriber_factory import get_transcriber

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from modules.audio.audio_data import Audio
from utils.logger_config import LOGGER

if __name__ == "__main__":
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    # print(f"current_dir: {current_dir}")
    # source_file = os.path.join(current_dir, "..", "..", "..", "..", "data", "audio.mp3")

    # url = "https://www.youtube.com/watch?v=-HV0B8pHjuA"

    # transcription = get_transcription().transcribe(
    #     audio_file=source_file, youtube_url=url
    # )
    # LOGGER.info(f"RETURN: {transcription}")

    ### --- Testing transcriber factory --- ###
    # transcriber = get_transcriber()
    # print(transcriber)

    # transcriber = get_transcriber("whisper")
    # print(transcriber)

    # transcriber = get_transcriber("lightning_mlx")
    # print(transcriber)

    # transcriber = get_transcriber("mlx")
    # print(transcriber)

    # transcriber = get_transcriber("youtube")
    # print(transcriber)

    # transcriber = get_transcriber("WhiSper")
    # print(transcriber)

    # transcriber = get_transcriber("lIghtning_mLx")
    # print(transcriber)

    # transcriber = get_transcriber("MLX")
    # print(transcriber)

    # transcriber = get_transcriber("YouTube")
    # print(transcriber)

    # transcriber = get_transcriber("irgendwas")
    # print(transcriber)

    yt_url = "https://www.youtube.com/watch?v=-HV0B8pHjuA"
    youtube_transcriber = get_transcriber("youtube")
    audio_dummy = Audio(audio_file=yt_url, ource=yt_url)
    transcription = youtube_transcriber.transcribe(audio_dummy)
