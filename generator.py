import customtkinter as ctk
import random
import string

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")


class MainWindow:
    textBox = ctk.CTkTextbox

    def __init__(self):
        self.main = ctk.CTk()
        self.main.geometry("350x500")
        self.main.resizable(width=False, height=False)
        self.main.title("Generator hasla")
        self.adds()
        self.main.mainloop()

    def generatePassword(self):
        self.textBox.delete("0.0", "end")
        if self.val.get() == 1:
            Up = random.choices(string.ascii_uppercase, k=6)
        else:
            Up = []
        if self.special.get() == 1:
            Sp = random.choices("~`!@#$%^&*()_-=}[]:;'\|<>?,./", k=4)
        else:
            Sp = []
        if self.num.get() == 1:
            Number = random.choices(string.digits, k=5)
        else:
            Number = []
        randomGen = random.sample(
            Up + Up + Sp + Number + random.choices(string.ascii_lowercase, k=24),
            k=int(self.length.get()))
        randomGen =''.join(randomGen)
        self.textBox.insert("0.0", randomGen)
        

    def adds(self):
        self.frame = ctk.CTkFrame(self.main)
        self.val, self.special, self.num = ctk.IntVar(), ctk.IntVar(), ctk.IntVar()
        self.optionsFrame = ctk.CTkScrollableFrame(self.frame, label_text="Opcje", label_text_color="White",
                                                   label_font=('Georgia', 18), width=160, height=100,
                                                   scrollbar_button_color="black",
                                                   scrollbar_button_hover_color="black", fg_color="black")
        self.uppercase = ctk.CTkCheckBox(self.optionsFrame, text="Wielkie litery", onvalue=1, offvalue=0,
                                         variable=self.val, text_color="White")
        self.specialChar = ctk.CTkCheckBox(self.optionsFrame, text="Specjalne znaki", onvalue=1, offvalue=0,
                                           variable=self.special)
        self.number = ctk.CTkCheckBox(self.optionsFrame, text="Cyfry", onvalue=1, offvalue=0, variable=self.num)
        self.length = ctk.IntVar()
        self.lengthFrame = ctk.CTkScrollableFrame(self.frame, label_text="Długość hasła", label_text_color="White",
                                                  label_font=('Georgia', 18), width=160, height=100,
                                                  scrollbar_button_color="black",
                                                  scrollbar_button_hover_color="black", fg_color="black")
        self.radioButton1 = ctk.CTkRadioButton(self.lengthFrame, text="12", value=12, variable=self.length)
        self.radioButton2 = ctk.CTkRadioButton(self.lengthFrame, text="18", value=18, variable=self.length)
        self.radioButton3 = ctk.CTkRadioButton(self.lengthFrame, text="24", value=24, variable=self.length)
        self.genPwd = ctk.CTkButton(self.main, text="Generuj Hasło", width=25)
        self.viewHistory = ctk.CTkButton(self.main, text="Jak mocne hasło", width=25, command=self.howStrong)
        self.textBox = ctk.CTkTextbox(self.main)
        self.widgetsInFrame = [self.uppercase, self.specialChar, self.number]
        for item in self.widgetsInFrame:
            item.pack(pady=5, anchor="w")
        self.radioButtons = [self.radioButton1, self.radioButton2, self.radioButton3]
        for radioButton in self.radioButtons:
            radioButton.grid()
        self.optionsFrame.grid(row=0, column=1)
        self.lengthFrame.grid(row=0, column=0)
        self.mainWidgets = [self.frame, self.genPwd, self.viewHistory, self.textBox]
        for widget in self.mainWidgets:
            widget.pack(pady=2)
        self.genPwd.configure(command=self.generatePassword)

    def howStrong(self):
       return False


if __name__ == '__main__':
    MainWindow()