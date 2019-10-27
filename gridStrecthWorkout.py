# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 09:59:14 2019

@author: Gerardo Sandoval
"""

import tkinter as tk

root = tk.Tk()
redframe = tk.Frame(root,bg='red4', width=50, height=50)
whiteframe = tk.Frame(root, bg='white', width=50, height=50)
blueframe = tk.Frame(root, bg='blue4', width=50, height=50)

redframe.grid(row=0, column=0, sticky='nsew')
whiteframe.grid(row=1, column=0, sticky='nsew')
blueframe.grid(row=2, column=0, sticky='nsew')

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

root.grid_columnconfigure(0, weight=1)

root.mainloop()