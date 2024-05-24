from tkinter import *
from tkinter import messagebox, ttk
import subprocess
import random


pencere1=Tk()




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
        def degistir():
            try:
                arayuz = combo.get()
                subprocess.run(["macchanger", "--random", arayuz], capture_output=True, text=True, check=True)
                messagebox.showinfo("Başarılı", f"{arayuz} arabirimi için MAC adresi otomatik olarak değiştirildi.")
            except subprocess.CalledProcessError:
                messagebox.showerror("Hata", f"{arayuz} arabirimi için MAC adresi değiştirilirken bir hata oluştu.")


        label1=Label(pencere1,text="İNTERFACE SEÇİN")
        label1.pack()
        combo=ttk.Combobox(pencere1,values=arayuzler)
        combo.pack()
        Buton=Button(pencere1,text="DEĞİŞTİRMEK İÇİN TIKLAYINIZ",command=degistir)
        Buton.pack()
        return arayuzler

    except subprocess.CalledProcessError:
        print("ifconfig komutu çalıştırılırken bir hata oluştu.")

mac_adresi_cekme()
pencere1.title("macchanger")
pencere1.geometry("500x500")

pencere1.mainloop()