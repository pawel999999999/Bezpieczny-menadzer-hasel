import customtkinter
import hashlib #hashowanie
import uuid #tworzenie sniegu
import subprocess  #otworzenie innego programu py
import sys
import time

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
gui = customtkinter.CTk()
gui.geometry("700x400")
uzytkownik = ""
haslo = ""
sciezka = "hasla.txt"
a=0

class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Menedżer Haseł")
        self.root.geometry("700x400")

        # Utwórz etykietę
        label = customtkinter.CTkLabel(root, text="Menedżer Haseł", font=("Arial", 16))
        label.pack(pady=10)

        # Utwórz ramkę do umieszczenia przycisków
        frame = customtkinter.CTkFrame(root)
        frame.pack(pady=20)

        # Utwórz przyciski
        button_dodaj = customtkinter.CTkButton(frame, text="Dodaj hasło", command=self.dodaj_haslo)
        button_dodaj.grid(row=0, column=0, padx=10)

        button_edytuj = customtkinter.CTkButton(frame, text="Edytuj hasło", command=self.edytuj_haslo)
        button_edytuj.grid(row=0, column=1, padx=10)

        button_usun = customtkinter.CTkButton(frame, text="Usuń hasło", command=self.usun_haslo)
        button_usun.grid(row=0, column=2, padx=10)

        # Utwórz miejsce na wyświetlanie haseł (np. tekstowe pole lub lista)
        self.password_display = customtkinter.CTkTextbox(root, height=10, width=60)
        self.password_display.pack(pady=10)

    def dodaj_haslo(self):
        nazwaUz = sys.stdin.read()
        print(nazwaUz)
    def edytuj_haslo(self):
       return False
    def usun_haslo(self):
        return False
        
if __name__ == "__main__":
    root = customtkinter.CTk()
    app = PasswordManagerApp(root)
    root.mainloop()