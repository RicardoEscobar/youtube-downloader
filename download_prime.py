from time_it import time_it
from download_highest_quality_audio import download_highest_quality_audio
from download_highest_resolution_video import download_highest_resolution_video
from merge_audio_video import merge_video_audio


@time_it
def download_prime(url: str) -> None:
    """Download the highest resolution DASH stream of a YouTube video"""
    video = download_highest_resolution_video(url)
    audio = download_highest_quality_audio(url)
    output = video.with_name(video.stem + ' (prime)' + video.suffix)
    merge_video_audio(video, audio, output)

    # Clean up
    video.unlink()
    audio.unlink()


if __name__ == '__main__':
    # Test the function with a YouTube video URL
    download_prime(
        'https://youtu.be/7ZuYuqooW_k')
