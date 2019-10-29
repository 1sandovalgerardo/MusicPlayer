# -*- coding: utf-8 -*-

import os


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
