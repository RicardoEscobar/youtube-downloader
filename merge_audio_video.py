import subprocess
from pathlib import Path
from time_it import time_it


@time_it
def merge_video_audio(input_video: Path, input_audio: Path, output: Path) -> Path:
    input_video_str = str(input_video.resolve())
    input_audio_str = str(input_audio.resolve())
    output_str = str(output.resolve())

    command = f'ffmpeg -i "{input_video_str}" -i "{input_audio_str}" -c:v copy -c:a copy -y "{output_str}"'
    print(command)
    subprocess.run(command, shell=True, check=True)

    # Return a path to the output file
    output_file = Path(output_str)
    return output_file


if __name__ == '__main__':
    input_video = Path(
        'Class Spotlight - Veteran Sharpshooter  Warhammer 40000 Darktide.mp4')
    input_audio = Path(
        'Class Spotlight - Veteran Sharpshooter  Warhammer 40000 Darktide.webm')
    output = Path(
        'Class Spotlight - Veteran Sharpshooter  Warhammer 40000 Darktide MERGED.mp4')

    merge_video_audio(input_video, input_audio, output)
