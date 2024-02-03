from pytube import YouTube
import os 
from sys import exit

def download_audio_or_video(yt, version='a'):
    if version == 'v':
        video = yt.streams.get_highest_resolution()
        video.download(r'C:\Users\Brian\OneDrive\Desktop\Kits\MyOwn\Downloaded Videos')
        print("Your request has been downloaded!")
    elif version == 'a':
        video = yt.streams.get_audio_only()
        path = r'C:\Users\Brian\OneDrive\Desktop\Kits\MyOwn\Downloaded Samples'
        video = video.download(path)
        video_to_audio(path)
        print("Your request has been downloaded!")
    else:
        print('That is not a valid version. Run the program again if this was not an error.')

def check_yt_link():
    link = input("Link: ")
    try:
        yt = YouTube(link)
        print(f"Downloading {link}...")
        return yt
    except:
        print(f"The URL '{link if len(link) > 0 else 'BLANK'}' doesn't work, sorry.")
        print('restarting the process...')
        main(input("action? (new/mp3/enter to pass)"))

def video_to_audio(path):
    os.chdir(path)
    for file in os.listdir():
        name, ext = os.path.splitext(file)
        if ext == '.mp4':
            ext = '.mp3'
            audio_file = f"{name}{ext}"
            os.rename(file, audio_file)

def main(action='new'):
    if action == 'new':
        download_audio_or_video(check_yt_link(), input("'a' for audio (default)| 'v' for video: "))
    elif action == 'mp3':
        path = r'C:\Users\Brian\OneDrive\Desktop\Kits\MyOwn\Downloaded Samples'
        video_to_audio(path)
        print("The samples are all converted to audio files :)")
    elif action == '':
        print('The program must have been ran by mistake. Have a great day! :)')
        exit()
    else:
        print('That is not a valid action. Run the program again and select the action you would like to complete')
        exit()

main(input("action? (new/mp3/enter to pass)"))