# -*- coding: utf-8 -*-

import os
from tkinter.messagebox import showinfo
from tkinter import Tk



def CreateMusicFiles():
    currentDir = os.getcwd()
    existingFiles = os.listdir()
    if 'MusicFiles' not in existingFiles:
        os.mkdir('MusicFiles')
        os.chdir('MusicFiles')
        os.mkdir('Blue')
        os.mkdir('Red')
        os.mkdir('Yellow')
        os.chdir('..')
    elif 'MusicFiles' in existingFiles:
        return None

    else:
        root=Tk()
        showinfo('Error in Code', 'We apologize but there is an issue creating the neccessary supporting folders.\
                 \nError Code: 876')
        root.destroy()
