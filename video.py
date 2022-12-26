import os
import subprocess
import pytube
from pytube import Playlist
import pathlib



path = os.getcwd() + "/downloads"



def main():

	op = 1
	while(op != 0 ):
		op = int(input("Options: \n1. Download MP4\n2. Download MP4 Playlist\n3. Download MP3\n4. Download MP3 Playlist\n0. Exit\nOpcion: "))
		if op == 0:
			break
		url = input("Please input your video url: ")
		if op == 1:		
			mp4Download(url)
		elif op == 2:
			mp4Playlist(url)
		elif op == 3:			
			mp3Download(url)
		elif op == 4:
			mp3Playlist(url)

		elif op > 4 or op < 0:
			print("Option must be between 0 and 4")

def mp4Download(url):
	try: 

		yt = pytube.YouTube(url)
		search = yt.streams.filter(file_extension='mp4', resolution='720p').first()
		if(search.download(output_path=path + "/mp4")):
			print("[+] {} succesfully downloaded".format(search.default_filename))
		else:
			print("[-] Could not download the video")

	except:
		print("[-] Invalid URL")

def mp4Playlist(url):
	try:

		p = Playlist(url)
		for url in p.video_urls:
			print("Link: " + url)
			yt = pytube.YouTube(url)
			search = yt.streams.filter(file_extension='mp4', resolution='720p').first()
			
			if(search.download(output_path=path + "/mp4")):
				print("[+] {} succesfully downloaded".format(search.default_filename))
			else:
				print("[-] Could not download the video")

	except:
		print("[-] Invalid URL")

def mp3Download(url):
	try:

		yt = pytube.YouTube(url)
		search = yt.streams.filter(file_extension='mp4', resolution='720p').first()
		
		defname = search.default_filename
		new_filename = defname.replace(".mp4",".mp3")
		if(os.path.exists(new_filename)):
			print("Este archivo ya existe!")
		else:
			if(search.download(output_path=path + "/mp3")):
				print("[+] {} succesfully downloaded".format(search.default_filename))
				print("Converting MP4 into MP3...")
				try:
					subprocess.call(['ffmpeg','-i', os.path.join(path+ "/mp3", defname), os.path.join(path + "/mp3", new_filename)], stdout=subprocess.DEVNULL)
					print("[+] Video converted succesfully.")
				except:
					print("[-] Could not convert the video")


				f = pathlib.Path(path + "/mp3/" + defname)
				f.unlink()	
			else:
				print("[-] Could not download the video")


		
	except:
		print("[-] Invalid URL")

def mp3Playlist(url):
	try: 

		p = Playlist(url)
		for url in p.video_urls:
			print("Link: " + url)
			yt = pytube.YouTube(url)
			search = yt.streams.filter(file_extension='mp4', resolution='720p').first()
			defname = search.default_filename
			new_filename = defname.replace(".mp4",".mp3")

			if(os.path.exists(new_filename)):
				print("Este archivo ya existe!")
			else:
				if(search.download(output_path=path + "/mp3")):
					print("[+] {} succesfully downloaded".format(search.default_filename))
					print("Converting MP4 into MP3...")
					try:
						subprocess.call(['ffmpeg','-i', os.path.join(path+ "/mp3", defname), os.path.join(path + "/mp3", new_filename)], stdout=subprocess.DEVNULL)
						print("[+] Video converted succesfully.")
					except:
						print("[-] Could not convert the video")


					f = pathlib.Path(path + "/mp3/" + defname)
					f.unlink()	
				else:
					print("[-] Could not download the video")
	except:
		print("[-] Invalid URL")








if __name__ == '__main__':
	main()


 
