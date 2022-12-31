import subprocess
from pathlib import Path


def merge_video_audio(input_video: Path, input_audio: Path, output: Path) -> None:
    input_video_str = str(input_video.resolve())
    input_audio_str = str(input_audio.resolve())
    output_str = str(output.resolve())

    command = f"ffmpeg -i {input_video_str} -i {input_audio_str} -c:v copy -c:a copy -y {output_str}"
    subprocess.run(command, shell=True, check=True)


if __name__ == '__main__':
    input_video = Path('video.mp4')
    input_audio = Path('audio.mp3')
    output = Path('output.mp4')

    merge_video_audio(input_video, input_audio, output)
