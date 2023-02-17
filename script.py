import pytube
from pytube.cli import on_progress
import os

option = -1

def resolusi():
    global link
    global reso
    link = input("Enter Your link here : ")
    print("Select Resolution : 1. 144p")
    print("                    2. 240p")
    print("                    3. 360p")
    print("                    4. 480p")
    print("                    5. 720p")
    print("                    6. Highest")
    reso = int(input("Your Choise : "))

def firstReso():
    yt = pytube.YouTube(link,on_progress_callback=on_progress)
    yt.streams.filter(res="144p").first().download()
    
    print(f"Downloaded {link} 144p")

def secondReso():
    yt = pytube.YouTube(link)
    yt.streams.filter(res="240p").first().download()
    print(f"Downloaded {link} 240p")

def thirdReso():
    yt = pytube.YouTube(link)
    yt.streams.filter(res="360p").first().download()
    print(f"Downloaded {link} 360p")

def fourthReso():
    yt = pytube.YouTube(link)
    yt.streams.filter(res="480p").first().download()
    print(f"Downloaded {link} 480p")

def fifthReso():
    yt = pytube.YouTube(link)
    yt.streams.filter(res="720p").first().download()
    print(f"Downloaded {link} 720p")
    
def highestReso():
    yt = pytube.YouTube(link)
    yt.streams.filter(res="1080p").first().download()
    print(f"Downloaded {link} highest")


def unduh():
    yt = pytube.YouTube(link)
    yt.streams.get_lowest_resolution().download()
    print("Downloaded", link)

def menuEng():
    global option
    print("           Menu")
    print("          ------")
    print()
    print("1. Download YouTube Video")
    print("2. Download Music from YouTube (Audio Only)")
    print("0. Exit")
    option = int(input("Choose Your Option : "))


while (option != 0):
    os.system('cls')
    menuEng()
    if (option == 1):
        print()
        resolusi()
        if (reso == 1):
            firstReso()
            os.system("pause")
        elif (reso == 2):
            secondReso()
            os.system("pause")
        elif (reso == 3):
            thirdReso()
            os.system("pause")
        elif (reso == 4):
            fourthReso()
            os.system("pause")
        elif (reso == 5):
            fifthReso()
            os.system("pause")
        elif (reso == 6):
            highestReso()
            os.system("pause")
        else:
            print("Must be 1-6")