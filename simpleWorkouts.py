# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 11:46:29 2019

@author: Gerardo Sandoval
"""

import os
import pygame
import tkinter as tk
from tkinter.filedialog import askdirectory, askopenfilename
from shutil import copy


root = tk.Tk()
root.minsize(500,500)

redSong = []

songPaths = {}


def DirectoryChooser(color):
    color = color.title()
    songPath = askopenfilename()
    songExtension = songPath.endswith(('.wav', '.mp3', 'm4a'))
    if songExtension:
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
    else:
        print('Audio Type not supported.')

DirectoryChooser(color='Red')
print(songPaths)

pygame.mixer.init()
pygame.mixer.music.load(songPaths['Red'])
pygame.mixer.music.play()

print(redSong)

tk.mainloop()

pygame.mixer.music.stop()
pygame.mixer.quit()