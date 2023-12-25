import customtkinter as ctk
import tkinter.messagebox as tkmb
import tkinter as tk
import sqlite3
import random
import code_confirm, Login, start


class Register():
    def _back(self):
        self.regis.destroy()

        start.Start().start()

    def reg(self):
        self.regis = ctk.CTk()
        self.regis.title("Bank")

        back = ctk.CTkButton(self.regis, text="←", width=35, height=35, command=self._back)
        back.pack(side=tk.LEFT, anchor=tk.NW)

        self.lbl = ctk.CTkLabel(master=self.regis, text='Registration')
        self.lbl.pack(pady=12,padx=10)

        self.user_email = ctk.CTkEntry(master=self.regis,placeholder_text="Email") 
        self.user_email.pack(pady=12,padx=10)

        self.user_email_confirm = ctk.CTkButton(master=self.regis, text='Confirm', hover_color='purple', command=self.create_account)
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

        self.user_code_confirm = ctk.CTkButton(master=self.conf, text='Confirm',  hover_color='purple',command=self.acc_confirm)
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

        self.okk = ctk.CTkButton(master=self.full_conf,text='Confirm', hover_color='purple', command=self.full_reg_final)
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
        Login.Login().log()


if __name__ == '__main__':
    Register().reg()