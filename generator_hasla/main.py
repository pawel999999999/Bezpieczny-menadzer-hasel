import customtkinter
import customtkinter as ctk

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
class MainWindow:
    def __init__(self):
        self.main = ctk.CTk()
        self.main.geometry("350,500")
        self.main.resizable(width=False, height=False)
        self.main.title("Generator hasla")
        self.adds()
        self.main.mainloop()
    def adds(self):
        self.frame = ctk.CTkFrame(self.main)
        self.val, self.special, self.num = ctk.IntVar(), ctk.IntVar(), ctk.IntVar()
        self.optionsFrame = ctk.CTkScrollableFrame(self.frame, label_text="Opcje", label_text_color="Blue")
        self.uppercase = ctk.CTkCheckBox(self.optionsFrame, text="Wielkie litery", onvalue=1, offvalue=0, variable=self.val, text_color="White")
        self.specialChar = ctk.CTkCheckBox(self.optionsFrame, text="Specjalne znaki", onvalue=1, offvalue=0, variable=self.special)
        self.number = ctk.CTkCheckBox(self.optionsFrame, text="Number", onvalue=1, offvalue=0, variable=self.num)
        self.length = ctk.IntVar()
        self.lengthFrame = ctk.CTkLabel(self.frame,text="Dlugosc hasla")
        self.widgetsInFrame = [self.uppercase, self.specialChar, self.number]
        for item in self.widgetsInFrame: item.pack(pady=2, anchor="w")
        self.optionsFrame.grid(row=0, column=0)
        self.lengthFrame.grid(row=0, column=1)
        self.mainWidgets = [self.frame]
        for widget in self.mainWidgets: widget.pack(pady=2)
if __name__ == '__main__':
    MainWindow()