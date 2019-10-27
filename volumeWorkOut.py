# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:21:35 2019

@author: Gerardo Sandoval
"""

import tkinter as tk
import pygame


root = tk.Tk()
volumeControl = tk.Scale(root, from_=0, to=100, orient='horizontal')
volumeControl.pack()

volumeLevel = {}

def GetVolume(control):
    print(control.get())
    volume = control.get()
    volumeLevel['volume'] = volume

button = tk.Button(root, text='Volumen Level', command=lambda: GetVolume(volumeControl))
button.pack()
print(volumeLevel)

root.mainloop()