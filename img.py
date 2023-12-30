from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import font
from tkinter import filedialog as fd
import os
import googletrans as gt
from googletrans import Translator

'''root=tk.Tk()
cut_image = tk.PhotoImage(file='ssl.PNG')
print(cut_image)
Label(root,image=cut_image).pack()
print(font.families())
print(font.names())'''
print(gt. LANGUAGES)
tt=Translator()
d=tt.translate("how are you",dest='hi')
print(d.text)

#root.mainloop()
