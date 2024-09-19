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
    logs1.geometry("800x600")
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

    darbinieki=ttk.Combobox(logs1, textvariable=vardsuzvards)
    prieksmets1=ttk.Combobox(logs1, textvariable=prieksmets)
    cena1=ttk.Combobox(logs1, textvariable=cena)
    dienas1=ttk.Entry(logs1,textvariable=dienas)

    darbinieki["values"] = ("Mareks Bahmnais","Deniss Stepanovs", "Raimonds Leja", "Juris Kalniņš")
    prieksmets1["values"] = ("Monitors","Tastatūra", "Pele", "Austiņas", "Mikrofons", "Webcam")
    cena1["values"] = ("5","10","20")

    darbinieki.grid(row=1, column=2,pady=30, padx=10)
    prieksmets1.grid(row=2,column=2,pady=30, padx=10)
    cena1.grid(row=3,column=2,pady=30, padx=10)
    dienas1.grid(row=4, column=2,pady=30,padx=10)
        

    def rezultats():
        selected_item3=cena1.get()
        value = int(dienas1.get())
        values = {"15":15, "55":55, "10":10}
        cena = values[selected_item3]
        result = value*cena
        result_label.config(text=f"Result: {result} €")


    result_label = tk.Label(logs1)
    result_label.grid(row=5, column=2)


    btn2=tk.Button(logs1,text="Aprēķināt nomas cenu", bd="5", command= rezultats)
    btn2.grid(row=5,column=1)

    btn3=Button(logs1, text="Aizvērt", bd="5" ,command= logs1.destroy)
    btn3.grid(row=5,column=3, pady=10, padx=10)

    


btn=Button(logs, text="Pasūtījums", bd="5", command=lambda: pasutijums())
btn1=Button(logs, text="Aizvērt", bd="5", command=logs.destroy)

btn.grid(row=1, column=4, pady=10, padx=10)
btn1.grid(row=1, column=5, pady=10, padx=10)



logs.mainloop()