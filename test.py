from tkinter import *
from tkinter.ttk import Button

# tkinter penceresi oluştur
root = Tk()

root.geometry('600x600')

# text area oluştur
text_area = Text(root, height=5, width=52)

#test arae üstüne label oluştur
text_label = Label(root, text='Sohbete başla')
text_label.config(font=("Arial", 16))

# Tkinter çalıştır
root.mainloop()