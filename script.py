from pytube.cli import on_progress
from pytube import YouTube
import os

menu = -1

def menuAll():
    global menu
    print("Menu")
    print("----")
    print()
    print("1. Download Video from Youtube")
    print("2. Download Audio from Youtube")
    print("0. Exit Menu")
    menu = int(input("Choose Your Option : "))

def downloadVideo():
    global videos
    global n
    videos = yt.streams.filter(type='video', progressive='True')
    s = 1
    for vid in videos:
        print(str(s)+". "+str(vid))
        s += 1
    n = int(input("Your Choise : "))

def downloadAudio():
    global audios
    global n
    audios = yt.streams.filter(only_audio="True")
    s = 1
    for audio in audios:
        print(str(s)+". "+str(audio))
        s += 1
    n = int(input("Your Choise : "))

def renameAudio():
    originalFile = audio.default_filename
    newFile = originalFile.replace(".webm", ".mp3")
    newFile = originalFile.replace(".mp4", ".mp3")
    os.rename(originalFile, newFile)

while(menu != 0):
    os.system('cls')
    menuAll()
    if(menu == 1):
        os.system('cls')
        print("Download Video from Youtube")
        link = str(input("Enter your link here : "))
        yt = YouTube(link, on_progress_callback=on_progress)
        downloadVideo()
        vid = videos[n-1]
        vid.download()
        print(f"{yt.title} \nDownload Completed")
        os.system('pause')
    elif(menu == 2):
        os.system('cls')
        print("Download Audio from Youtube")
        link = str(input("Enter your link here : "))
        yt = YouTube(link, on_progress_callback=on_progress)
        downloadAudio()
        audio = audios[n-1]
        audio.download()
        renameAudio()
        print(f"{yt.title} \nDownload Completed")
        os.system('pause')