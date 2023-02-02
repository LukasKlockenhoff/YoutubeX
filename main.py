from pytube import YouTube
import os

yt_url = YouTtube(str(input("Enter a http://youtu.be: \n >>>")))

vid = yt_url.streams.filter(only_audio=True).first()

out_path = os.path.splitext(str(input("Enter outdir. Blank for .\n>>>")))[0] or os.path.splitext('.')[0]

out_file = vid.download(output_path=out_path)
new_file = out_path + '.mp3'

os.rename(out_file, new_file)                             
