# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 11:46:29 2019

@author: Gerardo Sandoval
"""

import os
import pygame
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from shutil import copy


root = tk.Tk()
root.minsize(500, 500)

redSong = []

songPaths = {}
songTitle = {}

def DirectoryChooser(color):
    color = color.title()
    songPath = askopenfilename()
    songExtension = songPath.endswith(('.wav', '.mp3', 'm4a'))
    print(f'inside func:{songPath}')
    print(f'type of songPath = {type(songPath)}')
    print(f'len of songpath = {len(songPath)}')
    if len(songPath) < 1:
        return None
    elif songExtension:
        print(f'songPath={songPath}')
        unitPath = os.getcwd()
        print(f'Unit Path = {unitPath}')
        musicFilePath = os.path.join(unitPath, 'MusicFiles')
        musicFilePath = os.path.join(musicFilePath, str(color))
        print('We will now delete the old song.')
        for song in os.listdir(musicFilePath):
            print(song)
            fileToDelete=musicFilePath
            fileToDelete = os.path.join(musicFilePath, song)
            print(f'Now deleting: {fileToDelete}')
            os.remove(fileToDelete)
            print('Deleted old song')
        print(f'Location of the song is being saved to: {musicFilePath}')
        musicFilePath = copy(songPath, musicFilePath, follow_symlinks=True)
        print('song copied')
        songPaths[color] = musicFilePath
        print(f'Path for song is now:{musicFilePath}')
        # redSong.append(musicFilePath)
        print(f'The song title will be: {songTitle}')
        for song in os.listdir(f'MusicFiles\{color}'):
            songTitle[color] = song
    else:
        message = 'Sorry but that is an unsuported audio type.\nPlease chose one of the following: .wav, .mp3, .m4a'
        messagebox.showinfo('Unsuported Audio', message)
        DirectoryChooser(color)

DirectoryChooser(color='Red')
print(f'outside func:{songPaths}')

#pygame.mixer.init()
#pygame.mixer.music.load(songPaths['Red'])
#pygame.mixer.music.play()

#print(redSong)

tk.mainloop()

#pygame.mixer.music.stop()
#pygame.mixer.quit()