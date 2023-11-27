import customtkinter as ctk
import tkinter.messagebox as tkmb
from PIL import Image, ImageTk
import time
import sqlite3
import random
import code_confirm


class Main():
    

    def start(self):
        # Выбор темы(светлая, темная, системная)
        ctk.set_appearance_mode("dark") 

        # Выбор цвета темы
        ctk.set_default_color_theme("blue") 

        # Создание окна
        self.app = ctk.CTk() 
        self.app.geometry("400x400")
        self.app.resizable(False, False)
        self.app.title("Bank System")

        self.main_img = Image.open("bank.png")
        self.main_img = self.main_img.resize((150, 150))
        self.main_img = ImageTk.PhotoImage(self.main_img)

        self.main_label = ctk.CTkLabel(master=self.app, image=self.main_img)
        self.main_label.pack(pady=12,padx=10)

        self.button_login = ctk.CTkButton(master=self.app,text='Login',command=Login().log) 
        self.button_login.pack(pady=12,padx=10)

        self.button_register = ctk.CTkButton(master=self.app,text='Registration',command=Register().reg) 
        self.button_register.pack(pady=12,padx=10)
        self.app.mainloop()


        

    #def skit(self):
        a = 'TOXA'
        sqlite_connection = sqlite3.connect('bank.db')
        cursor = sqlite_connection.cursor()
        cursor.execute("SELECT name FROM Accounts WHERE login=?", (a,))
        skit_name = cursor.fetchone()

        self.app = ctk.CTk() 
        self.app.geometry("600x600")
        self.app.title("Bank System")

        self.main_label = ctk.CTkLabel(master=self.app, text='Hello, ' + (skit_name[0][0]))
        self.main_label.pack(pady=12,padx=10)

        self.app.mainloop()





        

class Login():
    def log(self):

        self.root = ctk.CTk()
        self.root.title("Bank")


        self.lbl = ctk.CTkLabel(master=self.root, text='Log in')
        self.lbl.pack(pady=12,padx=10)


        self.user_login = ctk.CTkEntry(master=self.root,placeholder_text="Username") 
        self.user_login.pack(pady=12,padx=10) 

        self.user_password = ctk.CTkEntry(master=self.root,placeholder_text="Password",show="*") 
        self.user_password.pack(pady=12,padx=10)

        self.button_login = ctk.CTkButton(master=self.root,text='Login',command=self.check) 
        self.button_login.pack(pady=12,padx=10)

        self.checkbox = ctk.CTkCheckBox(master=self.root,text='Remember Me') 
        self.checkbox.pack(pady=12,padx=10)

        self.root.mainloop()


    def check(self):

        with sqlite3.connect('bank.db') as sqlite_connection:
            cursor = sqlite_connection.cursor()   
            cursor.execute("SELECT login FROM Accounts WHERE login=?", (self.user_login.get(),))           
            _login = cursor.fetchall()            
            cursor.execute("SELECT password FROM Accounts WHERE login=?", (self.user_login.get(),))            
            _password = cursor.fetchall()


            if (_login[0])[0] == self.user_login.get() and (_password[0])[0] == self.user_password.get():
                tkmb.showinfo("Login", "Login successful!")
                self.root.destroy()
                Main().skit()
            else:
                tkmb.showerror("Login", "Login failed!")


class Register():
    def reg(self):
        self.regis = ctk.CTk()
        self.regis.title("Bank")

        self.lbl = ctk.CTkLabel(master=self.regis, text='Registration')
        self.lbl.pack(pady=12,padx=10)

        self.user_email = ctk.CTkEntry(master=self.regis,placeholder_text="Email") 
        self.user_email.pack(pady=12,padx=10)

        self.user_email_confirm = ctk.CTkButton(master=self.regis, text='Confirm', command=self.create_account)
        self.user_email_confirm.pack(pady=12,padx=10)

        self.regis.mainloop()


    def create_account(self):
        code = random.randint(100000, 999999)
        email = self.user_email.get()
    
        code_confirm.send_email_code(email, code)

        with sqlite3.connect('bank.db') as sqlite_connection:
            cursor = sqlite_connection.cursor()
            cursor.execute("""
                        CREATE TABLE IF NOT EXISTS registration (
                            mail TEXT PRIMARY KEY,
                            code INTEGER
                        )
                        """)
            cursor.execute("INSERT INTO registration VALUES (?, ?)", (email, code))

        self.conf = ctk.CTk()
        self.conf.title("Bank")

        self.lbl = ctk.CTkLabel(master=self.conf, text='Registration')
        self.lbl.pack(pady=12,padx=10)

        self.lbl_inf = ctk.CTkLabel(master=self.conf, text='Code was sent to ' + email)
        self.lbl_inf.pack(pady=12,padx=10)

        self.user_code = ctk.CTkEntry(master=self.conf,placeholder_text="Your code") 
        self.user_code.pack(pady=12,padx=10)

        self.user_code_confirm = ctk.CTkButton(master=self.conf, text='Confirm', command=self.acc_confirm)
        self.user_code_confirm.pack(pady=12,padx=10)

        self.conf.mainloop()


    def acc_confirm(self):
        sqlite_connection = sqlite3.connect('bank.db')
        cursor = sqlite_connection.cursor()
        cursor.execute("SELECT code FROM registration WHERE mail=?", (self.user_email.get(),))
        code_conf1 = cursor.fetchone()

        if int(code_conf1[0]) == int(self.user_code.get()):
            self.full_reg()
        else:
            tkmb.showerror("Error", "Incorrect code")


    def full_reg(self):

        self.full_conf = ctk.CTk()
        self.full_conf.title("Bank")

        self.user_name = ctk.CTkEntry(master=self.full_conf,placeholder_text="Your name") 
        self.user_name.pack(pady=12,padx=10)

        self.user_login = ctk.CTkEntry(master=self.full_conf,placeholder_text="Your login") 
        self.user_login.pack(pady=12,padx=10)

        self.user_passdword = ctk.CTkEntry(master=self.full_conf,placeholder_text="Your password", show="*") 
        self.user_passdword.pack(pady=12,padx=10)

        self.okk = ctk.CTkButton(master=self.full_conf,text='Confirm', command=self.full_reg_final)
        self.okk.pack(pady=12,padx=10)

        self.full_conf.mainloop()


    def full_reg_final(self):
        name = self.user_name.get()
        email = self.user_email.get()
        card_number = int("2202" + str(random.randint(1000, 9999)))
        login = self.user_login.get()
        password = self.user_passdword.get()
        balance = 0.0

        with sqlite3.connect('bank.db') as sqlite_connection:
            cursor = sqlite_connection.cursor()
            cursor.execute("""
                        CREATE TABLE IF NOT EXISTS Accounts (
                            email TEXT PRIMARY KEY,
                            name TEXT,
                            card_number INTEGER,
                            login TEXT,
                            password TEXT,
                            balance FLOAT
                        )
                        """)
            cursor.execute("INSERT INTO Accounts VALUES (?, ?, ?, ?, ?, ?)", (email, name, card_number, login, password, balance))
            tkmb.showinfo("Successful", "Registration completed!")

        self.regis.destroy()
        self.conf.destroy()
        self.full_conf.destroy()

if __name__ == "__main__":
        Main().start()