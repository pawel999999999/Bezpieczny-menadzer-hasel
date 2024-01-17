import customtkinter #gui
import hashlib #hashowanie
import uuid #tworzenie sniegu
import subprocess  #otworzenie innego programu py
import sys
import time
import hmac
import cryptography.hazmat

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
gui = customtkinter.CTk()
gui.geometry("700x400")
uzytkownik = ""
haslo = ""
sciezka = "hasla.txt"
a=0
tajnyKlucz = "Moj_tajny_klucz"
tajnyKlucz2 = b'Nowt_tajny_klucz'
textOdszyfrowany = " "

def sprawdz(szukany):
    with open(sciezka, 'r') as plik:
        zawartosc = plik.read()
        print(szukany)
        if szukany in zawartosc:
            return True
        else:
            return False
def oszyfrowanie(file):
    return 0

def hash(password):
    hashed = hmac.new(tajnyKlucz.encode('utf-8'), password.encode('utf-8'), hashlib.sha256)
    print(password.encode('utf-8'))
    print(hashed.hexdigest())
    return hashed.hexdigest()

def login():
    state1 = button1.get()
    nazwaUz = button1.get()
    state2 = button2.get()
    print("Sprawdzam dane:")
    state1 = hmac.new(tajnyKlucz.encode('utf-8'), state1.encode('utf-8'), hashlib.sha256)
    state2 = hmac.new(tajnyKlucz.encode('utf-8'), state2.encode('utf-8'), hashlib.sha256)
    state=state1.hexdigest()+state2.hexdigest()
    print(state)
    if(sprawdz(state)):
        try:
            gui2 = subprocess.Popen([ "glowne.exe"],creationflags=subprocess.CREATE_NO_WINDOW, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
            gui2.stdin.write("Tomek")
            gui2.stdin.close()
            gui.destroy()
            while gui2:
                time.sleep(1)
        except subprocess.CalledProcessError as e:
            print('Błąd')

def zajerestruj():
   
    try:
        subprocess.Popen(["rejestrator.exe"],creationflags=subprocess.CREATE_NO_WINDOW)
    except subprocess.CalledProcessError as e:
        print('Błąd')
    



frame = customtkinter.CTkFrame(master=gui)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Haslo nr")
label.pack(pady=1, padx=1)

label1 = customtkinter.CTkLabel(master=frame, text="Do portalu:")
label1.pack(pady=1, padx=1)

button1 = customtkinter.CTkEntry(master=frame, placeholder_text="uzytkownik")
button1.pack(pady=15, padx=10)

button2 = customtkinter.CTkEntry(master=frame, placeholder_text="haslo", show="*")
button2.pack(pady=15, padx=10)

button3 = customtkinter.CTkButton(master=gui, state="normal", text="zaloguj", command=login)
button3.pack(pady=12, padx=10)
button4 = customtkinter.CTkButton(master=gui, state="normal", text="zarejestruj", command=zajerestruj)
button4.pack(pady=12, padx=10)



gui.mainloop()
