import os
import pygame
# from mutagen.id3 import ID3
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename
from shutil import copy


class Application(tk.Frame):
    savedSongs = {}

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.config(height=300, width=300, bg='white')
        self.grid(column=0, row=0, sticky='nsew')
        self.grid(column=1, row=1, sticky='nsew')
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.MenuBar()
        self.SpaceLabel(row=0, column=0)

        # Blue Button
        self.blueSong = tk.StringVar()
        self.blueSongLabel = tk.Label(self, textvariable=self.blueSong,
                                      padx=20, bg='white')
        self.blueSongLabel.grid(row=2, column=1)
        self.ChooseSongButton('Blue', row=2, column=0)
        self.PlayButton('Blue', row=3, column=1)
        self.SpaceLabel(row=4, column=0)

        # Red Button
        self.redSong = tk.StringVar()
        self.redSongLabel = tk.Label(self, textvariable=self.redSong,
                                     padx=20, bg='white')
        self.redSongLabel.grid(row=5, column=1)
        self.ChooseSongButton('Red', row=5, column=0)
        self.PlayButton('Red', row=6, column=1)
        self.SpaceLabel(row=7, column=0)

        # Yellow Button
        self.yellowSong = tk.StringVar()
        self.yellowSongLabel = tk.Label(self, textvariable=self.yellowSong,
                                        padx=20, bg='white')
        self.yellowSongLabel.grid(row=8, column=1)
        self.ChooseSongButton('Yellow', row=8, column=0)
        self.PlayButton('Yellow', row=9, column=1)
        self.SpaceLabel(row=10, column=0)

        # Stop Music
        self.StopMusicButton(row=11, column=0)
        #self.SpaceLabel(row=12, column=0)

        # Close
        self.QuitButton(row=11, column=1)
        self.SpaceLabel(row=15, column=0)

    # Start of Functions Section

    def MenuBar(self):
        # Menu Bar (file and help sit within)
        self.menuBar = tk.Menu(self, bg='ivory2')
        # File Menu
        self.fileMenu = tk.Menu(self.menuBar, tearoff=0, relief='sunken')
        self.fileMenu.add_command(label='Menu Option 1', command=None)
        self.fileMenu.add_command(label='Menu Option 2', command=None)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label='Close', command=self.master.destroy)
        self.menuBar.add_cascade(label='File', menu=self.fileMenu)
        # help menu
        self.helpMenu = tk.Menu(self.menuBar, tearoff=0)
        self.helpMenu.add_command(label='Contact Us', command=None)
        self.menuBar.add_cascade(label='Help', menu=self.helpMenu)
        self.master.config(menu=self.menuBar)

    def ListBox(self):
        listBox = tk.Listbox(self)
        listBox.insert()
        listBox.grid(row=2, column=2)


    def SelectSong(self, color):
        self.color = color.title()
        self.songPath = askopenfilename()
        self.songExtension = self.songPath.endswith(('.wav', '.mp3', '.m4a'))
        if len(self.songPath) < 1:
            return None
        elif self.songExtension:
            self.songTitle = ''
            self.unitPath = os.getcwd()
            self.musicFilePath = os.path.join(self.unitPath, 'MusicFiles')
            self.musicFilePath = os.path.join(self.musicFilePath, str(color))
            for song in os.listdir(self.musicFilePath):
                self.fileToDelete = os.path.join(self.musicFilePath, song)
                os.remove(self.fileToDelete)
            self.musicFilePath = copy(self.songPath, self.musicFilePath,
                                      follow_symlinks=True)
            self.savedSongs[color] = self.musicFilePath
            for song in os.listdir(f'MusicFiles\{color}'):
                self.songTitle = song
            if color == 'Blue':
                self.blueSong.set(self.songTitle)
            elif color == 'Red':
                self.redSong.set(self.songTitle)
            else:
                self.yellowSong.set(self.songTitle)
        else:
            self.message = 'Sorry but that is an unsuported audio type.\nPlease chose one of the following: .wav, .mp3, .m4a'
            self.messagebox.showinfo('Unsuported Audio', self.message)
            self.SelectSong(color)

    def ChooseSongButton(self, color, row, column):
        self.chooseSongButton = tk.Button(self, text=f'Select Song for {color} Button',
                                          command=lambda: self.SelectSong(color))
        self.chooseSongButton.config(padx=15, pady=10)
        self.chooseSongButton.grid(row=row, column=column, sticky='we')
        self.grid_columnconfigure(column, minsize=200, pad=1, weight=1)

    def PlaySong(self, color):
        pygame.mixer.init()
        pygame.mixer.music.load(self.savedSongs[color])
        pygame.mixer.music.play()

    def PlayButton(self, color, row, column):
        self.playButton = tk.Button(self, text=f'Play {color} Button',
                                    command=lambda: self.PlaySong(color))
        self.playButton.config(padx=10, pady=5)
        self.playButton.grid(row=row, column=column, columnspan=2, rowspan=1,
                             sticky='we')

    def QuitButton(self, row, column):
        self.quitButton = tk.Button(self, text='Close',
                                    command=lambda: self.CloseActions())
                                    #command=self.master.destroy)
        self.quitButton.config()
        self.quitButton.grid(row=row, column=column, sticky='nsew', rowspan=2,
                             columnspan=2)
        self.grid_columnconfigure(column, weight=2)
        self.quitButton.grid_rowconfigure(row, weight=1)

    def StopMusicButton(self, row, column):
        self.stopMusicButton = tk.Button(self, text='Stop Music', height=5,
                                         command=lambda: pygame.mixer.music.stop())
        self.stopMusicButton.grid(row=row, column=column, sticky='wnse', rowspan=2)
        self.grid_columnconfigure(column, weight=1)

    def CloseMusic(self):
        try:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
        except:
            print('There was no pygame initiated')
            pass

    def Close(self):
        self.master.destroy()

    def CloseActions(self):
        self.CloseMusic()
        self.Close()

    def SpaceLabel(self, row, column):
        self.spaceLabel = tk.Label(self, bg='white')
        self.spaceLabel.grid(row=row, column=column)
        self.spaceLabel.grid_columnconfigure(column, weight=1)
        self.spaceLabel.grid_rowconfigure(row, weight=1)


root = tk.Tk()
root.minsize(350,420)
root.configure(bg='white')
root.title('My Music Player')
app = Application(master=root)
app.mainloop()

