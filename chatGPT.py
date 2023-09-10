#from tkinter import *
import customtkinter
import openai
import os
import pickle

# genel ayarlar
root=customtkinter.CTk()
root.titlr("My AI Bot")
root.geometry('600x600')
root.icon

# renklendirme özellikleri
customtkinter.set_apperance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root.mainLoop()
