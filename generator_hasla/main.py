import customtkinter as ctk

class MainWindow:
    def __init__(self):
        self.main = ctk.CTk()
        self.main.geometry("250x350")
        self.main.resizable(width=False, height=False)
        self.main.title("Generator hasla")
        self.main.mainloop()

if __name__ == '__main__':
    MainWindow()