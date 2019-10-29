from ProgFile.MyMusicFuncs import *
import tkinter as tk


def MiMusica():
    print('running MiMusica')
    root = tk.Tk()
    root.minsize(350,420)
    root.configure(bg='white')
    root.title('My Music Player')
    app = Application(master=root)
    app.mainloop()

if __name__=='__main__':
    MiMusica()

else:
    print('not running as main')
    print(__name__)