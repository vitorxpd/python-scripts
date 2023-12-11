import os
import ssl
from pytube import YouTube
from moviepy.editor import VideoFileClip

# Disable SSL certificate verification (use with caution)
ssl._create_default_https_context = ssl._create_unverified_context

def download_video(video_url, output_folder=''):
  try:
    # Create a YouTube object
    yt = YouTube(video_url)

    # Get the highest resolution available
    video_stream = yt.streams.get_highest_resolution()

    # Set the output path
    video_path = os.path.join(output_folder, f"{yt.title}.mp4")

    # Download the video
    video_stream.download(output_path=output_folder, filename=f"{yt.title}.mp4")

  except Exception as e:
    print(f'Error processing {video_url}: {str(e)}')

if __name__ == "__main__":
  video_url = input("Enter the YouTube video URL: ")
  output_folder = input("Enter the Output Folder (optional): ")

  download_video(video_url, output_folder)
