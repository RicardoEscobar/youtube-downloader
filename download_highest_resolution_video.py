import pytube


def download_highest_resolution_video(url: str) -> None:
    """Download the highest resolution DASH stream of a YouTube video"""
    # Create a YouTube object using the URL
    yt = pytube.YouTube(url)

    # Get the highest resolution DASH stream
    dash_stream = yt.streams.get_by_itag(yt.streams.filter(
        adaptive=True).order_by('resolution').desc().first().itag)

    # Download the DASH stream
    dash_stream.download()


if __name__ == '__main__':
    # Test the function with a YouTube video URL
    download_highest_resolution_video(
        'https://www.youtube.com/watch?v=dQw4w9WgXcQ')
