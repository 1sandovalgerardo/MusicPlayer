import os
import pygame
from mutagen.id3 import ID3
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory


root = tk.Tk()

songTitles = []
songList = []

songPlaying = tk.StringVar()
songPlayingLabel = tk.Label(root)
root = tk.Tk()