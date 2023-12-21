import customtkinter
import hashlib
import uuid

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
gui = customtkinter.CTk()
gui.geometry("700x400")
uzytkownik = ""
haslo = ""


def _hash(password):
    print(hashlib.sha512(password.encode()))
    return hashlib.sha512(password.encode())

def login():
    state1 = button1.get()
    state2 = button2.get()
    print("Sprawdzam dane:")
    print(state1)
    print(state2)
    _hash(state2)


def button_event():
   print("button pressed")


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
button4 = customtkinter.CTkButton(master=gui, state="normal", text="zarejestruj", command=login)
button4.pack(pady=12, padx=10)



gui.mainloop()