import tkinter as tk
import sqlite3 as sql

def db_kaydet():
    frame1 = tk.Frame(window)

    ad = tk.Label(text="isim: ",font="Times 15",bg="grey")
    soyad = tk.Label(text="soyisim: ",font="Times 15",bg="grey")
    ad_entry = tk.Entry(font="Times 15")
    soyad_entry = tk.Entry(font="Times 15")
    email = tk.Label(text="email: ",font="Times 15",bg="grey")
    tel_no = tk.Label(text="telefon no:",font="Times 15",bg="grey")
    email_entry = tk.Entry(font="Times 15")
    tel_entry = tk.Entry(font="Times 15")
    kayitB = tk.Button(text="kaydet",font="Times 15")


    ad.grid(row=0,column=0,padx=10,pady=10)
    soyad.grid(row=1,column=0,padx=10,pady=10)
    ad_entry.grid(row=0,column=1,padx=10,pady=10)
    soyad_entry.grid(row=1,column=1,padx=10,pady=10)
    email.grid(row=0, column=3,padx=10,pady=10)
    tel_no.grid(row=1, column=3,padx=10,pady=10)
    email_entry.grid(row=0, column=4,padx=10,pady=10)
    tel_entry.grid(row=1, column=4,padx=10,pady=10)
    kayitB.grid(row=4,column=3,padx=10,pady=10)

    frame1.mainloop()

def db_yukle():
    pass

def db_listele():
    pass

def db_sil():
    pass

def db_sifirla():
    pass

def frame_kilavuz():
    pass

window = tk.Tk()
window.geometry("700x700")
window.configure(bg='grey')
window.title("Ahmet Fehim Örnek Data Base")

menu1 = tk.Menu(window)
window.config(menu=menu1)
dosya = tk.Menu(menu1,tearoff=0)
kilavuzz = tk.Menu(menu1,tearoff=0)
menu1.add_cascade(label="Veri",menu=dosya)
menu1.add_cascade(label="kılavuz",menu=kilavuzz)
dosya.add_command(label="yeni kayit",command=db_kaydet)
dosya.add_command(label="kayit sorgula", command=db_listele)
dosya.add_command(label="kayit listele",command=db_listele)
dosya.add_command(label="kayit sil",command=db_sil)
dosya.add_separator()
dosya.add_command(label="çık")
window.mainloop()