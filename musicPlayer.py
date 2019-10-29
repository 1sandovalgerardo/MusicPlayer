from ProgFile.MyMusicFuncs import *
from ProgFile.FolderCreator import *
import tkinter as tk


def myMusic():
    print('running My Music')
    root = tk.Tk()
    root.minsize(350,420)
    root.configure(bg='white')
    root.title('My Music Player')
    app = Application(master=root)
    app.mainloop()

if __name__=='__main__':
    CreateMusicFiles()
    myMusic()

else:
    print('not running as main')
    print(__name__)