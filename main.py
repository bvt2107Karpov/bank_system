import customtkinter as ctk 
from PIL import Image, ImageTk
import time as t
import login, register, code_confirm

def start():
    # Выбор темы(светлая, темная, системная)
    ctk.set_appearance_mode("dark") 

    # Выбор цвета темы
    ctk.set_default_color_theme("blue") 

    # Создание окна
    app = ctk.CTk() 
    app.geometry("400x400")
    app.resizable(False, False)
    app.title("Bank System")

    frame = ctk.CTkFrame(master=app) 
    frame.pack(pady=20,padx=40,fill='both',expand=True)

    main_img = Image.open("bank.png")
    main_img = main_img.resize((150, 150))
    main_img = ImageTk.PhotoImage(main_img)

    main_label = ctk.CTkLabel(master=frame, image=main_img)
    main_label.pack(pady=12,padx=10)

    button_login = ctk.CTkButton(master=frame,text='Login',command=login.log) 
    button_login.pack(pady=12,padx=10)

    button_register = ctk.CTkButton(master=frame,text='Registration',command=register.reg) 
    button_register.pack(pady=12,padx=10)

    app.mainloop()


def main():
    pass

if __name__ == "__main__":
    start()