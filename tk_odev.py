import tkinter as tk
from tkinter import ttk
import sqlite3 as sql
from time import strftime
# cinsiyet logo resimlerini göstermek için gerekli kütüphane
from PIL import ImageTk,Image

# Hocam database'i oluşturduğu yeri ayarlamazsanız göremeyebilirsiniz alttaki sql.connect("DataBase.db", isolation_level=None)
# kısmında istediğiniz path'i yazabilirsiniz iyi günler :)

# kaydet tuşuna basıldığında gerçekleşecek işlemlerin gerçekleştiği fonksiyon
def kaydet():
    kilo_deger = int(kilov.get())
    boy_deger = int(boyv.get())
    sek_deger = int(sekV.get())
    bmi_seker(boy_deger, kilo_deger)
    hasta_mi(sek_deger)
    db_kaydet()

# veri tabanına kaydetme için kullanılacak fonksiyon
def db_kaydet():
    if cinsVar.get() == 1:
        cins = "erkek"
    elif cinsVar.get() == 2:
        cins = "kadın"
    else:
        cins = "belirtilmedi"

    # ekranda yazılan verilerin gösterilmesi
    on_goster.config(state="normal")
    on_goster.insert(tk.END, ad_entry.get() + " | " + soyad_entry.get() + " | " + cins + " | "+ boy_entry.get() +" | "+ kilo_entry.get() +" | "
                     + seker_entry.get() + " | " + tel_entry.get() + " | " + email_entry.get() + " |kayıt saati: " + saat["text"]+"\n")
    # veri tabanı kayıtlama
    conn.execute("INSERT INTO Insan VALUES(?, ?, ?)", [ad_entry.get(), soyad_entry.get(),cins])
    conn.execute("INSERT INTO Fiziksel_Ozellik VALUES(?, ?, ?)", [boy_entry.get(), kilo_entry.get(), seker_entry.get()])
    conn.execute("INSERT INTO Iletisim VALUES(?, ?, ?)", [tel_entry.get(), email_entry.get(),saat["text"]])
    on_goster.config(state="disabled")

# şeker hastası mı kontrol edilecek
def hasta_mi(deger):
    if deger > 126:
        bmiT.insert(tk.END,"  |  şeker hastasısınız")
    else:
        bmiT.insert(tk.END,"  |  şeker hastası değilsiniz")

    bmiT.config(state="disabled")
# bmi kontrol edilecek değer yazılacak
def bmi_seker(boy,kilo):
    bmiT.config(state="normal")
    boy = boy / 100
    bmi = (float(kilo) / (boy*boy))
    bmiT.delete('1.0', tk.END)
    if bmi < 18.5:
        bmiT.insert(tk.END,"zayıfsınız")
    elif 18.5 < bmi < 24.9:
        bmiT.insert(tk.END,"normal kilodasınız")
    elif 24.9 < bmi < 29.9:
        bmiT.insert(tk.END,"fazla kilolusunuz")
    elif 29.9 < bmi < 39.9:
        bmiT.insert(tk.END, "obezsiniz")
    else:
        bmiT.insert(tk.END, "morbid obezsiniz")

#ekranda saati gösterelim
def time():
    string = strftime('%H:%M:%S %p')
    saat.config(text = string)
    saat.after(1000, time)
# ______________________________________________
#       Data base ayarlamaları
# ______________________________________________

conn = sql.connect("DataBase.db", isolation_level=None)
conn.execute("CREATE TABLE IF NOT EXISTS Insan(Ad, Soyad, Cinsiyet)")
conn.execute("CREATE TABLE IF NOT EXISTS Fiziksel_Ozellik(Boy, Kilo, AclikSeker)")
conn.execute("CREATE TABLE IF NOT EXISTS Iletisim(tel_no, email, kayit_saati)")
#--------------------------------------------------------
#                   ANA EKRANI OLUŞTURALIM
#----------------------------------------------------------
window = tk.Tk()
window.geometry("900x700")
window.configure(bg='grey')
window.title("Ahmet Fehim Örnek Data Base")


frame = tk.Frame(window, relief="ridge", borderwidth=5, bg="grey")
frame.pack()
saat = tk.Label(frame, font="Calibri 20", bg="grey")
saat.grid(row=0, column=9)
time()
frame1 = tk.Frame(window, background="grey", borderwidth=5, relief="ridge")
frame1.pack()
ad = tk.Label(frame1, text="isim: ", font="Times 15", background="grey").grid(row=0, column=0, padx=10, pady=10)
soyad = tk.Label(frame1, text="soyisim: ", font="Times 15", background="grey").grid(row=1, column=0, padx=10,pady=10)

ad_entry = tk.Entry(frame1, font="Times 15")
ad_entry.grid(row=0, column=1, padx=10, pady=10)
soyad_entry = tk.Entry(frame1, font="Times 15")
soyad_entry.grid(row=1, column=1, padx=10, pady=10)
cinsVar = tk.IntVar()
cinsiyet = tk.Label(frame1, text="cinsiyet: ", font="Times 15", background="grey").grid(row=4, column=0, padx=10,pady=10)

boyut = (30, 30)
im1 = Image.open('man_tr.png').resize(boyut)
img1 = ImageTk.PhotoImage(im1)
R2 = ttk.Radiobutton(frame1, image=img1, variable=cinsVar, value=1).grid(row=4, column=1, sticky="w")
im2 = Image.open('woman_tr.png').resize(boyut)
img2 = ImageTk.PhotoImage(im2)
R3 = ttk.Radiobutton(frame1, image=img2, variable=cinsVar, value=2).grid(row=4, column=1, columnspan=1)
email = tk.Label(frame1, text="email: ", font="Times 15", background="grey").grid(row=0, column=3, padx=10, pady=10)
tel_no = tk.Label(frame1, text="telefon no:", font="Times 15", background="grey").grid(row=1, column=3, padx=10,pady=10)

email_entry = tk.Entry(frame1, font="Times 15")
email_entry.grid(row=0, column=4, padx=10, pady=10)
okul = tk.Label(frame1, text="okul: ", font="Times 15", background="grey").grid(row=3, column=3, padx=10, pady=10)
okul_entry = tk.Entry(frame1, font="Times 15")
okul_entry.grid(row=3, column=4, padx=10, pady=10)
tel_entry = tk.Entry(frame1, font="Times 15")
tel_entry.grid(row=1, column=4, padx=10, pady=10)
boyv = tk.StringVar()
kilov = tk.StringVar()
sekV = tk.StringVar()
boy = tk.Label(frame1, text="boy: ", font="Times 15", background="grey").grid(row=2, column=0, padx=10, pady=10)
boy_entry = tk.Entry(frame1, font="Times 15", textvariable=boyv)
boy_entry.grid(row=2, column=1, padx=10, pady=10)
kilo = tk.Label(frame1, text="kilo: ", font="Times 15", background="grey").grid(row=2, column=3, padx=10, pady=10)
kilo_entry = tk.Entry(frame1, font="Times 15", textvariable=kilov)
kilo_entry.grid(row=2, column=4, padx=10, pady=10)
seker = tk.Label(frame1, text="açlık kan şekeri(mg / dL): ", font="Times 15", background="grey").grid(row=3,column=0,padx=10,pady=10)

seker_entry = tk.Entry(frame1, font="Times 15", textvariable=sekV)
seker_entry.grid(row=3, column=1, padx=10, pady=10)
kayitB = tk.Button(frame1, text="kişiyi kaydet", font="Times 15", command=kaydet).grid(row=4, column=4, padx=10,pady=10)

frame2 = tk.Frame(window, bg="grey")
frame2.pack()
bmiT = tk.Text(frame2, width=36, height=1, font="Times 15", relief="flat", bg="grey")
bmiT.config(state="disabled")
bmiT.grid(row=0, column=0, padx=10, pady=10)
onizle = tk.Label(frame2, text="VERİ TABANI BÖYLE GÖZÜKECEK: ", font="Times 13", background="grey")
onizle.grid(row=1, column=0, padx=10,pady=10)
on_goster = tk.Text(frame2, height=10,width=100)
on_goster.grid(row=2, column=0, padx=10, pady=10)
on_goster.config(state="disabled")

window.mainloop()