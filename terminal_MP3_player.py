#Importing all the libraries required

import os
import time as t
from pygame import *
from mutagen.mp3 import MP3

#Declaring the list of songs

songs=[]

#Get the list of songs from the current directory

for items in os.listdir(os.getcwd()):
    if items.endswith('.mp3'):
        songs.append(items)

print('Welcome to the Terminal Music Player...\n')
print('Below are the list of songs in this directory')

for index,song in enumerate(songs):
    print('{}. {}'.format(index+1,song))

#If there are any songs in the directory
if len(songs)>1:
    try:
        choice=int(input('Enter the song index which you want to play...'))
        assert choice>=1
    except AssertionError:
        print('Please select at least one song')
    else:
        choice-=1
        audio=MP3(songs[choice])
        print(audio.info.length)
        mixer.init()
        mixer.music.load(songs[choice])
        mixer.music.play()
        mixer.music.get_busy()
        while mixer.music.get_busy():
            print('Playing')
            key=''
            while key!='p':
                key=input()
            mixer.music.pause()
            while key!='r':
                key=input()
            mixer.music.unpause()

else:
    print('Sorry! There are no songs detected in your system')
