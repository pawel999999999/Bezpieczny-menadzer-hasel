import customtkinter
import hashlib #hashowanie
import uuid #tworzenie sniegu
import subprocess  #otworzenie innego programu py
import sys
import time
from cryptography.fernet import Fernet
import base64
from tkinter import *


key ="TOMETOMETOMETOMETOMETOMETOMETOME"
def encode_to_urlsafe_base64(input_string):
        input_bytes = input_string.encode('utf-8')
        urlsafe_base64_bytes = base64.urlsafe_b64encode(input_bytes)
        #print(urlsafe_base64_bytes)
        #print(Fernet.generate_key())
        return urlsafe_base64_bytes
key = encode_to_urlsafe_base64(key)
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
gui = customtkinter.CTk()
gui.geometry("700x400")
uzytkownik = ""
haslo = ""
sciezka = "hasla.txt"
a=0
cipher = Fernet(key)
class PasswordManagerApp:
    passwords = []
    def dodaj_haslo(self):
        try:
            subprocess.Popen(['python', "dodaj_haslo.py" ])
        except subprocess.CalledProcessError as e:
            print('Błąd')
    def edytuj_haslo(self):
        try:
            subprocess.Popen(['python', "dodaj_haslo.py" ])
        except subprocess.CalledProcessError as e:
            print('Błąd')
    def usun_haslo(self):
        return False
    def generator(self):
        try:
            subprocess.Popen(['python', "generator.py" ])
        except subprocess.CalledProcessError as e:
            print('Błąd')
    def zdeszyfruj(self):
        with open("hasla11.txt", 'rb') as file:
            zawartosc = file.read()
        file.close()
        if zawartosc:
            print("CHHUJ")
            decrypted_message = cipher.decrypt(zawartosc).decode()
            print(decrypted_message)
            platform,user,password = []
            
            return decrypted_message   
        else:
            return ""
    def __init__(self, root):
        self.root = root
        self.root.title("Menedżer Haseł")
        self.root.geometry("750x400")

        label = customtkinter.CTkLabel(root, text="Menedżer Haseł", font=("Arial", 16))
        label.pack(pady=10)

        frame = customtkinter.CTkFrame(root)
        frame.pack(pady=20)

        button_dodaj = customtkinter.CTkButton(frame, text="Dodaj hasło", command=self.dodaj_haslo)
        button_dodaj.grid(row=0, column=0, padx=10)
        my_framemy_frame= customtkinter.CTkScrollableFrame(root, height=700, width=702)
        my_framemy_frame.pack(pady=5)
        button_edytuj = customtkinter.CTkButton(frame, text="Edytuj hasło", command=self.edytuj_haslo)
        button_edytuj.grid(row=0, column=1, padx=10)
        my_font = customtkinter.CTkFont(family="Helvetica", size= 26, weight="bold")
        button_usun = customtkinter.CTkButton(frame, text="Usuń hasło", command=self.usun_haslo)
        button_usun.grid(row=0, column=2, padx=10)
        button_pokaz = customtkinter.CTkButton(frame, text="Odswiez", command=self.zdeszyfruj)
        button_pokaz.grid(row=0, column=2, padx=10)
        button_generator = customtkinter.CTkButton(frame, text="Generator haseł", command=self.generator)
        button_generator.grid(row=0, column=3, padx=10)
        self.side_display = customtkinter.CTkTextbox(my_framemy_frame, height=600, width=234,font=my_font,corner_radius=5,border_width=4,activate_scrollbars=True)
        self.side_display.pack(side="left")
        self.username_display = customtkinter.CTkTextbox(my_framemy_frame, height=600, width=234,font=my_font,corner_radius=2,border_width=4,activate_scrollbars=True)
        self.username_display.pack(side="left")
        self.password_display = customtkinter.CTkTextbox(my_framemy_frame, height=600, width=234,font=my_font,corner_radius=2,border_width=4,activate_scrollbars=True)
        self.password_display.pack(side="left")
        

        
if __name__ == "__main__":
    root = customtkinter.CTk()
    app = PasswordManagerApp(root)
    root.mainloop()