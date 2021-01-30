import tkinter as tk
from tkinter import ttk
import sqlite3 as sql
from time import strftime
from PIL import ImageTk,Image

def kaydet():
    # db kaydettpien önce if kullanıp her entry dolmuş mu kontrol et uygun uyarı mesajı göster
    db_kaydet()
    kitle_indeks()
    hasta_mi(sek_deger)

def db_kaydet():
    pass

def hasta_mi(deger):
    if deger.get() > 126:
        pass
    else:
        pass

def kitle_indeks():
    pass

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

def time():
    string = strftime('%H:%M:%S %p')
    saat.config(text = string)
    saat.after(1000, time)

#--------------------------------------------------------
#                   ANA EKRANI OLUŞTURALIM
#----------------------------------------------------------
window = tk.Tk()
window.geometry("900x700")
window.configure(bg='grey')
window.title("Ahmet Fehim Örnek Data Base")

frame = tk.Frame(window,relief="ridge",borderwidth=5,bg="grey")
frame.pack()
saat = tk.Label(frame, font = "Calibri 20",bg="grey")
saat.grid(row=0,column=9)
time()


frame1 = tk.Frame(window,background="grey",borderwidth=5,relief="ridge")
frame1.pack()

ad = tk.Label(frame1,text="isim: ", font="Times 15", background="grey").grid(row=0, column=0, padx=10, pady=10)
soyad = tk.Label(frame1,text="soyisim: ", font="Times 15", background="grey").grid(row=1, column=0, padx=10, pady=10)
ad_entry = tk.Entry(frame1,font="Times 15").grid(row=0, column=1, padx=10, pady=10)
soyad_entry = tk.Entry(frame1,font="Times 15").grid(row=1, column=1, padx=10, pady=10)

cinsiyet = tk.Label(frame1,text="cinsiyet: ",font="Times 15", background="grey").grid(row=4, column=0, padx=10, pady=10)
boyut=(30,30)
im1 = Image.open('man_tr.png').resize(boyut)
img1 = ImageTk.PhotoImage(im1)
R2 = ttk.Radiobutton(frame1, image=img1,value=2).grid(row=4, column=1,sticky="w")
im2 = Image.open('woman_tr.png').resize(boyut)
img2 = ImageTk.PhotoImage(im2)
R3 = ttk.Radiobutton(frame1,image=img2,value=2).grid(row=4, column=1,columnspan=1)



email = tk.Label(frame1,text="email: ", font="Times 15", background="grey").grid(row=0, column=3, padx=10, pady=10)
tel_no = tk.Label(frame1,text="telefon no:", font="Times 15", background="grey").grid(row=1, column=3, padx=10, pady=10)
email_entry = tk.Entry(frame1,font="Times 15").grid(row=0, column=4, padx=10, pady=10)
okul = tk.Label(frame1,text="okul: ", font="Times 15", background="grey").grid(row=3, column=3, padx=10, pady=10)
okul_entry = tk.Entry(frame1,font="Times 15").grid(row=3, column=4, padx=10, pady=10)
tel_entry = tk.Entry(frame1,font="Times 15").grid(row=1, column=4, padx=10, pady=10)
boy = tk.Label(frame1,text="boy: ", font="Times 15", background="grey").grid(row=2,column=0, padx=10, pady=10)
boy_entry = tk.Entry(frame1,font="Times 15").grid(row=2,column=1, padx=10, pady=10)
kilo = tk.Label(frame1,text="kilo: ", font="Times 15", background="grey").grid(row=2,column=3, padx=10, pady=10)
kilo_entry = tk.Entry(frame1,font="Times 15").grid(row=2,column=4, padx=10, pady=10)
seker = tk.Label(frame1,text="açlık kan şekeri(mg / dL): ", font="Times 15", background="grey").grid(row=3,column=0, padx=10, pady=10)
sek_deger = tk.IntVar()
seker_entry = tk.Entry(frame1,font="Times 15",textvariable=sek_deger).grid(row=3,column=1, padx=10, pady=10)
kayitB = tk.Button(frame1,text="kişiyi kaydet",font="Times 15", command=kaydet).grid(row=4, column=4, padx=10, pady=10)

window.mainloop()