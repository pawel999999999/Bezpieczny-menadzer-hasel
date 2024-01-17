import customtkinter
import random
import string
from cryptography.fernet import Fernet

import base64
key ="TOMETOMETOMETOMETOMETOMETOMETOME"
def encode_to_urlsafe_base64(input_string):
        input_bytes = input_string.encode('utf-8')
        urlsafe_base64_bytes = base64.urlsafe_b64encode(input_bytes)
        print(urlsafe_base64_bytes)
        print(Fernet.generate_key())
        return urlsafe_base64_bytes
key=encode_to_urlsafe_base64(key)
cipher = Fernet(key)
def zdeszyfruj():
    with open("hasla11.txt", 'rb') as file:
        zawartosc = file.read()
    file.close()
    if zawartosc:
        decrypted_message = cipher.decrypt(zawartosc).decode()
        return decrypted_message   
    else:
         return ""
def zaszyfruj(state):
    
    ciphertext = cipher.encrypt(state.encode())
    #print(ciphertext)
    return ciphertext
def dodaj():

    state=zdeszyfruj()
    print(state)

    state0 = button0.get()
    state1 = button1.get()
    state2 = button2.get()
    if (state == None):
        state = "::"+state+"::"+state0+"::"+state1+"::"+state2
    else:
        state = state+"::"+state0+"::"+state1+"::"+state2
    print("CHUJ " + state)
    state = zaszyfruj(state)
    with open("hasla11.txt", 'wb') as file:
        file.write(state)
    file.close()
    state= zdeszyfruj()
    print(state)
    return True

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
gui = customtkinter.CTk()
gui.geometry("500x500")
frame = customtkinter.CTkFrame(master=gui)
frame.pack(pady=20, padx=60, fill="both", expand=True)
label = customtkinter.CTkLabel(master=frame, text="Dodawanie konta \n ")
label.pack(pady=1, padx=1)
button0 = customtkinter.CTkEntry(master=frame, placeholder_text="Portal")
button0.pack(pady=15, padx=10)
button1 = customtkinter.CTkEntry(master=frame, placeholder_text="Uzytkownik")
button1.pack(pady=15, padx=10)

button2 = customtkinter.CTkEntry(master=frame, placeholder_text="Haslo", show="*")
button2.pack(pady=15, padx=10)
button3 = customtkinter.CTkButton(master=gui, state="normal", text="Dodaj", command=dodaj)
button3.pack(pady=12, padx=10)

gui.mainloop()