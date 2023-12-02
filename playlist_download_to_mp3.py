
import os
import ssl
from pytube import Playlist
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

def download_and_convert_playlist(url, output_folder='', title_prefix=''):
  playlist = Playlist(url)

  for video in playlist.videos:
    try:
      print(f'Downloading: {title_prefix}{video.title}')
      video_stream = video.streams.filter(file_extension="mp4", progressive=True).first()

      # Extract the original file extension from the stream
      file_extension = video_stream.mime_type.split('/')[-1]

      # Download with the correct file extension
      video_path = os.path.join(output_folder, f"{title_prefix}{video.title}.{file_extension}")
      video_stream.download(output_path=output_folder, filename=f"{title_prefix}{video.title}.{file_extension}")

      # Convert video to MP3
      convert_video_to_mp3(video_path, output_folder)

      # Delete the original video file
      os.remove(video_path)
      print(f'{video_path} deleted successfully!')

    except Exception as e:
      print(f'Error processing {title_prefix}{video.title}: {str(e)}')

if __name__ == "__main__":
  playlist_id = input("Enter the Playlist ID: ")
  title_prefix = input("Enter the Title Prefix (optional): ")
  output_folder = input("Enter the Output Folder (optional): ")

  playlist_url = f"https://www.youtube.com/playlist?list={playlist_id}"

  download_and_convert_playlist(playlist_url, output_folder, title_prefix)
