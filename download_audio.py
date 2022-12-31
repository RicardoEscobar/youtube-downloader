from time_it import time_it
from download_highest_quality_audio import download_highest_quality_audio
from convert_to_mp3 import convert_to_mp3


@time_it
def download_audio(url: str) -> None:
    audio = download_highest_quality_audio(url)
    output = audio.with_name(audio.stem + ' (prime)' + '.mp3')
    convert_to_mp3(audio, output)

    # clean up
    audio.unlink()


if __name__ == '__main__':
    # Replace this with the URL of the YouTube video you want to download
    download_audio("https://youtu.be/qpCNaRkIh2E")
