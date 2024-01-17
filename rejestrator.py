import customtkinter 
import hashlib 
import subprocess  
import hmac
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from CTkMessagebox import CTkMessagebox

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")
gui = customtkinter.CTk()
gui.geometry("400x400")
uzytkownik = ""
haslo = ""
tajnyKlucz = "Moj_tajny_klucz"


def generator():

    try:
        subprocess.Popen(["generator.exe"], creationflags = subprocess.CREATE_NO_WINDOW, shell=True )
    except subprocess.CalledProcessError as e:
        print('Błąd')

def savePasswords(deta):
    print(deta)
    with open("hasla.txt", 'a') as file:
        file.write(deta)

def zajerestruj():
    uzytkownik = button1.get()
    haslo = button2.get()
    print("Zarejestrowano")
    print("Uzytkownik: " + uzytkownik)
    with open("uzytkownicy.txt", 'r') as file:
        zawartosc = file.read()
        if uzytkownik in zawartosc:
            CTkMessagebox(title="Błąd", message="Już jest ten użytkownik")
        else:
            with open("uzytkownicy.txt", 'a') as file:
                file.write(uzytkownik + "\n")
            print("Haslo " + haslo)
            state1 = hmac.new(tajnyKlucz.encode('utf-8'), uzytkownik.encode('utf-8'), hashlib.sha256)
            hashed = hmac.new(tajnyKlucz.encode('utf-8'), haslo.encode('utf-8'), hashlib.sha256)
            state=state1.hexdigest()+hashed.hexdigest()
            savePasswords(state + "\n")
            
        
   

frame = customtkinter.CTkFrame(master=gui)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Rejestracja")
label.pack(pady=1, padx=1)

label1 = customtkinter.CTkLabel(master=frame, text="Nowego Użytkownika")
label1.pack(pady=1, padx=1)

button1 = customtkinter.CTkEntry(master=frame, placeholder_text="uzytkownik")
button1.pack(pady=15, padx=10)

button2 = customtkinter.CTkEntry(master=frame, placeholder_text="haslo", show="*")
button2.pack(pady=15, padx=10)

button3 = customtkinter.CTkButton(master=gui, state="normal", text="Generator hasel", command=generator)
button3.pack(pady=12, padx=10)

button4 = customtkinter.CTkButton(master=gui, state="normal", text="zarejestruj", command=zajerestruj)
button4.pack(pady=12, padx=10)



gui.mainloop()