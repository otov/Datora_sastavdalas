import tkinter as tk
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk

logs = Tk()
logs.geometry("500x500")
logs.title("Instrumentu noma")
logs.configure(background="gray")

foto_frame=tk.Frame(logs)
foto_frame.grid(row=2,column=1,columnspan=2,padx=10,pady=10)
foto_image=Image.open("31-20190213203042-7.jpg")
logs.mainloop()