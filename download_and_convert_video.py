import os
import ssl
from pytube import YouTube
from moviepy.editor import VideoFileClip

# Disable SSL certificate verification (use with caution)
ssl._create_default_https_context = ssl._create_unverified_context

def convert_video_to_mp3(video_path, output_folder):
    try:
        # Load the video file
        video_clip = VideoFileClip(video_path)

        # Extract only the audio
        audio_clip = video_clip.audio

        # Save the audio in MP3 format
        mp3_path = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(video_path))[0]}.mp3")
        audio_clip.write_audiofile(mp3_path)

        print(f'Conversion to MP3 successful: {mp3_path}')
    except Exception as e:
        print(f'Error in MP3 conversion: {str(e)}')

def download_and_convert_video(video_url, output_folder=''):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the highest resolution available
        video_stream = yt.streams.get_highest_resolution()

        # Set the output path
        video_path = os.path.join(output_folder, f"{yt.title}.mp4")

        # Download the video
        video_stream.download(output_path=output_folder, filename=f"{yt.title}.mp4")

        # Convert video to MP3
        convert_video_to_mp3(video_path, output_folder)

        # Delete the original video file
        os.remove(video_path)
        print(f'{video_path} deleted successfully!')

    except Exception as e:
        print(f'Error processing {video_url}: {str(e)}')

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    output_folder = input("Enter the Output Folder (optional): ")

    download_and_convert_video(video_url, output_folder)
