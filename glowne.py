import customtkinter
import hashlib #hashowanie
import uuid #tworzenie sniegu
import subprocess  #otworzenie innego programu py
import sys
import time
from cryptography.fernet import Fernet
import base64
from tkinter import *
import numpy
from CTkMessagebox import CTkMessagebox
#from main import *
#from dodaj_haslo import *

text_received = sys.argv[1]
print("tomek" + text_received)
text_received=text_received[:32]
file_name = text_received[:7] + ".txt"
key ="TOMETOMETOMETOMETOMETOMETOMETOME"
def encode_to_urlsafe_base64(input_string):
        input_bytes = input_string.encode('utf-8')
        urlsafe_base64_bytes = base64.urlsafe_b64encode(input_bytes)
        #print(urlsafe_base64_bytes)
        #print(Fernet.generate_key())
        return urlsafe_base64_bytes
def upozadkuj(text):
    elements = text.split('::')
    domeny =[]
    uzytkownicy= []
    current_label= ""
    hasla =[]
    i = 0
    Wartosciprzerwa = text.split('::')
    print(Wartosciprzerwa[i])
    for i in range(0, len(elements)-1):
        if i%3==0:
            domeny.append(Wartosciprzerwa[i+1])
        if i%3==1:
            uzytkownicy.append(Wartosciprzerwa[i+1])
        if i%3==2:
            hasla.append(Wartosciprzerwa[i+1])         

    print(domeny,uzytkownicy,hasla)
    tablica=[domeny,uzytkownicy,hasla]
    print(tablica)
    return tablica
key = encode_to_urlsafe_base64(key)
print(key)
key = encode_to_urlsafe_base64(text_received)
print(key)
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
gui = customtkinter.CTk()
gui.geometry("700x400")
uzytkownik = ""
haslo = ""
sciezka = "hashe.txt"
a=0
cipher = Fernet(key)
class PasswordManagerApp:
    #CTkMessagebox(title="Faza beta programu", message="Program jest w fazie beta! Przed wcisniecie 'ok' wstaw do pliku glownego swoj zaszfrowany plik z haslami pod nazwa hasla11.txt, po skorzystaniu z aplikacji zapisz go na bezpiecznym nosniku i usun z komputera")
    passwords = []
    
    def dodaj_haslo(self):
        try:
            subprocess.Popen(["python","dodaj_haslo.py", text_received], shell=True)
        except subprocess.CalledProcessError as e:
            print('Błąd')
    def edytuj_haslo(self):
        return False
    def usun_haslo(self):
        return False
    def generator(self):
        try:
            subprocess.Popen(["python","generator.py"],creationflags=subprocess.CREATE_NO_WINDOW, shell=True )
        except subprocess.CalledProcessError as e:
            print('Błąd')
    def wyswietlanie(self, tablica,j):
        a=""
        self.side_display.configure(state=NORMAL)  
        self.username_display.configure(state=NORMAL)  
        self.password_display.configure(state=NORMAL) 
        
        for i in tablica:
            a=a+i+"\n"
        if(j==0):
            self.side_display.delete(0.0,"end")
            self.side_display.insert(0.0,a)
        if(j==1):
           self.username_display.delete(0.0,"end")
           self.username_display.insert(0.0,a) 
        if(j==2):
           self.password_display.delete(0.0,"end")
           self.password_display.insert(0.0,a)
        self.side_display.configure(state=DISABLED)  
        self.username_display.configure(state=DISABLED)  
        self.password_display.configure(state=DISABLED) 
    def zdeszyfruj(self):
        with open(file_name, 'rb') as file:
            zawartosc = file.read()
        file.close()
        if zawartosc:
            decrypted_message = cipher.decrypt(zawartosc).decode()
            print(decrypted_message)
            tablica=upozadkuj(decrypted_message)
            self.wyswietlanie(tablica[0],0)
            self.wyswietlanie(tablica[1],1)
            self.wyswietlanie(tablica[2],2)
            return decrypted_message   
        else:
            return ""
        
    def __init__(self, root):
        self.root = root
        self.root.title("Menedżer Haseł")
        self.root.geometry("750x400")
        my_font = customtkinter.CTkFont(family="Helvetica", size= 26, weight="bold")

        label = customtkinter.CTkLabel(root, text="Menedżer Haseł", font=my_font)
        label.pack(pady=10)

        frame = customtkinter.CTkFrame(root)
        frame.pack(pady=20)

        button_dodaj = customtkinter.CTkButton(frame, text="Dodaj hasło", command=self.dodaj_haslo)
        button_dodaj.grid(row=0, column=0, padx=10)
        my_framemy_frame= customtkinter.CTkScrollableFrame(root, height=700, width=702)
        my_framemy_frame.pack(pady=5)
        button_edytuj = customtkinter.CTkButton(frame, text="Edytuj hasło", command=self.edytuj_haslo)
        button_edytuj.grid(row=0, column=1, padx=10)
        button_usun = customtkinter.CTkButton(frame, text="Usuń hasło", command=self.usun_haslo)
        button_usun.grid(row=0, column=2, padx=10)
        button_pokaz = customtkinter.CTkButton(frame, text="Odswiez", command=self.zdeszyfruj)
        button_pokaz.grid(row=0, column=2, padx=10)
        button_generator = customtkinter.CTkButton(frame, text="Generator haseł", command=self.generator)
        button_generator.grid(row=0, column=3, padx=10)
        self.side_display = customtkinter.CTkTextbox(my_framemy_frame, height=1800, width=234,font=my_font,corner_radius=5,border_width=4,activate_scrollbars=False,wrap=NONE)
        self.side_display.pack(side="left")
        self.username_display = customtkinter.CTkTextbox(my_framemy_frame, height=1800, width=234,font=my_font,corner_radius=2,border_width=4,activate_scrollbars=False,wrap=NONE)
        self.username_display.pack(side="left")
        self.password_display = customtkinter.CTkTextbox(my_framemy_frame, height=1800, width=234,font=my_font,corner_radius=2,border_width=4,activate_scrollbars=False,wrap=NONE)
        self.password_display.pack(side="left")
        self.side_display.configure(state=DISABLED)  
        self.username_display.configure(state=DISABLED)  
        self.password_display.configure(state=DISABLED)  

        
if __name__ == "__main__":
    root = customtkinter.CTk()
    app = PasswordManagerApp(root)
    root.mainloop()