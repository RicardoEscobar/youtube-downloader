"""This is a unit test for the download_highest_quality_audio function in the download_highest_quality_audio.py file."""
import unittest
from pathlib import Path
from download_highest_quality_audio import download_highest_quality_audio


class TestDownloadHighestQualityAudio(unittest.TestCase):
    def test_download_highest_quality_audio(self):
        # Test download_highest_quality_audio function
        # Create a Path object for the current working directory
        cwd = Path.cwd()
        # Create a Path object for the test video
        video = cwd / 'tests' / 'unit' / 'test_video.mp4'
        # Create a Path object for the test audio
        audio = cwd / 'tests' / 'unit' / 'test_audio.mp4'
        # Create a Path object for the test output
        output = cwd / 'tests' / 'unit' / 'test_output.mp4'
        # Create url for the test video
        url = 'https://youtu.be/7ZuYuqooW_k'
        # Download the highest quality audio
        download_highest_quality_audio(url, output)
        # Check if the output file exists
        self.assertTrue(output.exists())
        # Clean up
        video.unlink()
        audio.unlink()
        output.unlink()

if __name__ == '__main__':
    unittest.main()