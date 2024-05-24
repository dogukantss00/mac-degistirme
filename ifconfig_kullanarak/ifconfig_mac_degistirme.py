from tkinter import *
from tkinter import messagebox, ttk
import subprocess
import random

# Rastgele MAC adresi oluşturan fonksiyon
def rastgele_mac():
    my_list = []
    eleman_liste=[0,1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f"]
    for i in range(12):
        eleman=random.choice(eleman_liste)
        my_list.append(eleman)

    eklenen_sayilar =":" 
    for i in range(2, len(my_list)+3, 3):
        my_list[i:i] = eklenen_sayilar

    return ''.join(map(str, my_list))  # Listeyi birleştirerek bir dize oluştur

# Sistemdeki ağ arayüzlerini tespit eden fonksiyon
def mac_adresi_cekme():
    try:
        ifconfig_cikti = subprocess.run(['ifconfig'], capture_output=True, text=True, check=True)
        ifconfig_cikti = ifconfig_cikti.stdout

        arayuzler = []
        lines = ifconfig_cikti.split('\n')
        for line in lines:
            if 'flags=' in line:
                arayuz_ad = line.split(':')[0]
                arayuzler.append(arayuz_ad)

        return arayuzler
    except subprocess.CalledProcessError:
        print("ifconfig komutu çalıştırılırken bir hata oluştu.")

# Otomatik MAC adresi değiştirme fonksiyonu
def otomatik():
    
    def oto_degis():
        try:
            interface = text5.get()
            mac = rastgele_mac()
            subprocess.run(['ifconfig', interface, 'hw', 'ether', mac], capture_output=True, text=True, check=True)
            messagebox.showinfo("Başarılı", f"{interface} arabirimi için MAC adresi {mac} olarak değiştirildi.")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Hata", f"{interface} arabirimi için MAC adresi değiştirilirken bir hata oluştu.")

    buton1.destroy()  # Otomatik değiştirme butonunu kaldır
    buton2.destroy()  # Manuel değiştirme butonunu kaldır
    text1 = Label(pencere1, text="Interface seçiniz:")
    text1.pack()
    interfaces = mac_adresi_cekme()  
    text5 = ttk.Combobox(pencere1, values=interfaces)
    text5.pack()
    text3 = Button(pencere1, text="DEĞİŞTİR", command=oto_degis)
    text3.pack()

# Manuel MAC adresi değiştirme fonksiyonu
def manuel():
    def man_degis():
        try:
            interface = text5.get()
            mac = text8.get()
            subprocess.run(['ifconfig', interface, 'hw', 'ether', mac], capture_output=True, text=True, check=True)
            messagebox.showinfo("Başarılı", f"{interface} arabirimi için MAC adresi {mac} olarak değiştirildi.")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Hata", f"{interface} arabirimi için MAC adresi değiştirilirken bir hata oluştu.")
    
        
    buton1.destroy()  # Otomatik değiştirme butonunu kaldır
    buton2.destroy()  # Manuel değiştirme butonunu kaldır
    text1 = Label(pencere1, text="Interface seçiniz:")
    text1.pack()
    interfaces = mac_adresi_cekme()  
    text5 = ttk.Combobox(pencere1, values=interfaces)
    text5.pack()
    text6 = Label(pencere1, text="Mac adresini giriniz:")
    text6.pack()
    text8 = Entry(pencere1)
    text8.pack()
    text7 = Button(pencere1, text="DEĞİŞTİR", command=man_degis)
    text7.pack()


pencere1 = Tk()  # Tkinter penceresini oluştur
pencere1.title("MAC Adresi Değiştirme")  # Pencere başlığını ayarla
pencere1.geometry("500x500")  # Pencere boyutunu ayarla

buton1 = Button(pencere1, text="OTOMATİK DEĞİŞTİRME", width=20, height=5, command=otomatik)
buton1.pack()  # Otomatik değiştirme butonunu ekle
buton2 = Button(pencere1, text="MANUEL DEĞİŞTİRME", width=20, height=5, command=manuel)
buton2.pack()  # Manuel değiştirme butonunu ekle

pencere1.mainloop()  # Pencereyi çalıştır
