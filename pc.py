import tkinter as tk
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk

logs = Tk()
logs.geometry("730x400")
logs.title("Datoru noma")
logs.configure(background="purple")

foto_frame=tk.Frame(logs)
foto_frame.grid(row=1,column=1,columnspan=2,padx=10,pady=10)
foto_image=Image.open("s-l1200.jpg")
resized_foto=foto_image.resize((500,333))
foto = ImageTk.PhotoImage(resized_foto)
foto_label=ttk.Label(foto_frame,image=foto)
foto_label.grid(row=1,column=1,columnspan=2,padx=10,pady=10)

def pasutijums():
    logs1=Toplevel()
    logs1.geometry("400x400")
    logs1.title("Pasūtījums")
    logs1.configure(background="purple")

    ttk.Label(logs1,text="Izvēlieties darbinieku:").grid(row=1,column=1,pady=30,padx=10)
    ttk.Label(logs1,text="Izvēlieties priekšmetu").grid(row=2,column=1,pady=30,padx=10)
    ttk.Label(logs1,text="Norādiet cenu:").grid(row=3,column=1,pady=30,padx=10)
    ttk.Label(logs1,text="Nomas dienu skaits:").grid(row=4,column=1,pady=30,padx=10)

    vardsuzvards=tk.StringVar()
    prieksmets=tk.StringVar()
    cena=tk.StringVar()
    dienas=tk.StringVar()







btn=Button(logs, text="Pasūtījums", bd="8", command=lambda: pasutijums())
btn1=Button(logs, text="Aizvērt", bd="8", command=logs.destroy)

btn.grid(row=1, column=4, pady=10, padx=10)
btn1.grid(row=1, column=5, pady=10, padx=10)



logs.mainloop()