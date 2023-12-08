import customtkinter as ctk
import tkinter.messagebox as tkmb
from PIL import Image, ImageTk
import Register, Login




class Start():
    def start(self):
        
        # Выбор темы(светлая, темная, системная)
        ctk.set_appearance_mode("dark") 

        # Выбор цвета темы
        ctk.set_default_color_theme("blue") 

        # Создание окна
        self.Root = ctk.CTk() 
        self.Root.geometry("400x400")
        self.Root.title("Bank System")

        self.main_img = Image.open("bank.png")
        self.main_img = self.main_img.resize((150, 150))
        self.main_img = ImageTk.PhotoImage(self.main_img)

        self.main_label = ctk.CTkLabel(master=self.Root, image=self.main_img)
        self.main_label.pack(pady=12,padx=10)

        self.button_login = ctk.CTkButton(master=self.Root,text='Login',command=self.start_log) 
        self.button_login.pack(pady=12,padx=10)

        self.button_register = ctk.CTkButton(master=self.Root,text='Registration',command=self.start_reg) 
        self.button_register.pack(pady=12,padx=10)
        self.Root.mainloop()


    def start_reg(self):
        self.Root.destroy()
        Register.Register().reg()

        
        
    def start_log(self):
        self.Root.destroy()
        Login.Login().log()



if __name__ == '__main__':
    Start().start()

