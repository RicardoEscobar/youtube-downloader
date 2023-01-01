import subprocess
from pathlib import Path
from time_it import time_it


@time_it
def convert_to_mp3(input_file: Path, output_file: Path) -> None:
    if input_file.suffix == '.webm':
        output_file_mp4 = input_file.with_suffix(".mp4")
        command = f'ffmpeg -i "{input_file}" -c:a libmp3lame -y "{output_file_mp4}"'
        subprocess.run(command, shell=True, check=True)
        command = f'ffmpeg -i "{output_file_mp4}" -vn -acodec libmp3lame -y "{output_file}"'
        subprocess.run(command, shell=True, check=True)
    else:
        command = f'ffmpeg -i "{input_file}" -vn -acodec libmp3lame -y "{output_file}"'
        subprocess.run(command, shell=True, check=True)

    # clean up
    output_file_mp4.unlink()


if __name__ == '__main__':
    # Test the function with an input audio file and output MP3 file
    input_file = Path('She Knows - J Cole  Español.mp4')
    output_file = Path('She Knows - J Cole  Español.mp3')
    convert_to_mp3(input_file, output_file)
