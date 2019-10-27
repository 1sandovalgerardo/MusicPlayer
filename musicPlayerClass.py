import os
import pygame
from mutagen.id3 import ID3
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename
from shutil import copy


class Application(tk.Frame):
    savedSongs = {}
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.config(height=300, width=300)
        self.pack()
        self.MenuBar()
        #self.savedSongs = {}
        # Blue Button
        self.blueSong = tk.StringVar()
        self.blueSongLabel = tk.Label(self, textvariable=self.blueSong)
        self.blueSongLabel.pack()
        self.blueSongLabel.pack()
        self.ChooseSongButton('Blue')
        self.PlayButton('Blue')

        # Red Button
        self.redSong = tk.StringVar()
        self.redSongLabel = tk.Label(self, textvariable=self.redSong)
        self.redSongLabel.pack()
        self.ChooseSongButton('Red')
        self.PlayButton('Red')

        # Yellow Button
        self.yellowSong = tk.StringVar()
        self.yellowSongLabel = tk.Label(self, textvariable=self.yellowSong)
        self.yellowSongLabel.pack()
        self.ChooseSongButton('Yellow')
        self.PlayButton('Yellow')

        # Stop Music
        self.StopMusicButton()

        # Close
        self.QuitButton()

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
        listBox.pack()


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
                self.songTitle=song
            if color=='Blue':
                self.blueSong.set(self.songTitle)
            elif color=='Red':
                self.redSong.set(self.songTitle)
            else:
                self.yellowSong.set(self.songTitle)
        else:
            self.message = 'Sorry but that is an unsuported audio type.\nPlease chose one of the following: .wav, .mp3, .m4a'
            self.messagebox.showinfo('Unsuported Audio', self.message)
            self.SelectSong(color)

    def ChooseSongButton(self, color):
        chooseSongButton = ttk.Button(self, text=f'{color} Button',
                                     command=lambda: self.SelectSong(color))
        chooseSongButton.pack()

    def PlaySong(self, color):
        pygame.mixer.init()
        pygame.mixer.music.load(self.savedSongs[color])
        pygame.mixer.music.play()

    def PlayButton(self, color):
        playButton = ttk.Button(self, text=f'Play {color} Button',
                               command=lambda: self.PlaySong(color))
        playButton.pack()

    def QuitButton(self):
        self.quitButton = ttk.Button(self, text='Close',
                                    command=lambda: self.CloseActions())
                                    #command=self.master.destroy)
        self.quitButton.pack()

    def StopMusicButton(self):
        self.stopMusicButton = ttk.Button(self, text='Stop Music',
                                         command=lambda: pygame.mixer.music.stop())
        self.stopMusicButton.pack()

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





root = tk.Tk()
root.minsize(300,300)
root.title('My Music Player')
app = Application(master=root)
print(app.savedSongs)
app.mainloop()

