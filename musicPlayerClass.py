import os
import pygame
from mutagen.id3 import ID3
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.MenuBar()
        self.QuitButton()

    def MenuBar(self):
        self.menuBar = tk.Menu(self, bg='ivory2')
        self.fileMenu = tk.Menu(self.menuBar,tearoff=0, relief='sunken')
        self.fileMenu.add_command(label='Menu Option 1', command=None)
        self.fileMenu.add_command(label='Menu Option 2', command=None)
        #self.fileMenu.add_seperator()
        self.fileMenu.add_command(label='Close', command=self.master.destroy)
        self.helpMenu = tk.Menu(self.menuBar)
        self.menuBar.add_cascade(label='File', menu=self.fileMenu)
        self.menuBar.add_cascade(label='Help', menu=self.helpMenu)
        self.master.config(menu=self.menuBar)




    def QuitButton(self):
        self.quitButton = tk.Button(self, text='Close',
                                    command=self.master.destroy)
        self.quitButton.pack()





root = tk.Tk()
app = Application(master=root)
app.mainloop()
