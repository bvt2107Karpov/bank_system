import customtkinter as ctk
import tkinter.messagebox as tkmb
import sqlite3
import random
import code_confirm





def reg():
    def create_account():
        code = random.randint(100000, 999999)
        email = user_email.get()

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

        conf = ctk.CTk()
        conf.title("Bank")

        lbl = ctk.CTkLabel(master=conf, text='Registration')
        lbl.pack(pady=12,padx=10)

        lbl_inf = ctk.CTkLabel(master=conf, text='Code was sent to ' + email)
        lbl_inf.pack(pady=12,padx=10)

        user_code = ctk.CTkEntry(master=conf,placeholder_text="Your code") 
        user_code.pack(pady=12,padx=10)

        user_code_confirm = ctk.CTkButton(master=conf, text='Confirm', command=lambda: acc_confirm(email, user_code.get()))
        user_code_confirm.pack(pady=12,padx=10)

        conf.mainloop()

        return user_code

        

    def acc_confirm(user_email, user_code):
        
        sqlite_connection = sqlite3.connect('bank.db')
        cursor = sqlite_connection.cursor()
        cursor.execute("SELECT code FROM registration WHERE mail=?", (user_email,))
        code_conf1 = cursor.fetchone()

        if int(code_conf1[0]) == int(user_code):
            print('победа')
        else:
            print(':(', user_code, int(code_conf1[0]))

    def card_number_generate():
        card_num = "2202" + str(random.randint(1000000000000, 999999999999)) 
        return card_num


    root = ctk.CTk()
    root.title("Bank")

    lbl = ctk.CTkLabel(master=root, text='Registration')
    lbl.pack(pady=12,padx=10)

    user_email = ctk.CTkEntry(master=root,placeholder_text="Email") 
    user_email.pack(pady=12,padx=10)

    user_email_confirm = ctk.CTkButton(master=root, text='Confirm', command=create_account)
    user_email_confirm.pack(pady=12,padx=10)




    root.mainloop()


reg()


