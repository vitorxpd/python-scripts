import os
import yt_dlp

def download_audio_as_mp3(url, output_folder, prefix):
  ffmpeg_path = '/opt/homebrew/bin/ffmpeg'

  ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f'{output_folder}/{prefix}%(title)s.%(ext)s',
    'postprocessors': [{
      'key': 'FFmpegExtractAudio',
      'preferredcodec': 'mp3',
      'preferredquality': '192',
    }],
    'ffmpeg_location': ffmpeg_path,
    'progress_hooks': [progress_hook],
    'no_warnings': True,
    'ignoreerrors': True
  }

  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

def progress_hook(d):
  if d['status'] == 'downloading':
    print(f"Baixando: {d['filename']} - {d['_percent_str']} completo")
  elif d['status'] == 'finished':
    print(f"Download concluído, convertendo para MP3: {d['filename']}")

url = input("Digite a URL do vídeo ou playlist: ")
prefix = input("Digite o prefixo para o nome do arquivo (opcional, pressione Enter para deixar vazio): ")
output_folder = f'{os.getcwd()}/downloads'

if not os.path.exists(output_folder):
  os.makedirs(output_folder)

download_audio_as_mp3(url, output_folder, prefix)
