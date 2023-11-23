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

        

        conf = ctk.CTk()
        conf.title("Bank")

        lbl = ctk.CTkLabel(master=conf, text='Registration')
        lbl.pack(pady=12,padx=10)

        lbl_inf = ctk.CTkLabel(master=conf, text='Code was sent to ' + email)
        lbl_inf.pack(pady=12,padx=10)

        user_code = ctk.CTkEntry(master=conf,placeholder_text="Your code") 
        user_code.pack(pady=12,padx=10)

        user_code_confirm = ctk.CTkButton(master=conf, text='Confirm', command=acc_confirm)
        user_code_confirm.pack(pady=12,padx=10)

        conf.mainloop()

        try:
            with sqlite3.connect('bank.db') as sqlite_connection:
                cursor = sqlite_connection.cursor()
                cursor.execute("""
                                    CREATE TABLE IF NOT EXISTS registration (
                                        name TEXT,
                                        address TEXT,
                                        acc_no INTEGER,
                                        balance REAL
                                    )
                                    """)
                cursor.execute("INSERT INTO registration VALUES (?, ?, ?)", (email, code, user_code))
                sqlite_connection.commit()

        except Exception as e:
            tkmb.showerror("Error", str(e))



        

    def acc_confirm():
        sqlite_connection = sqlite3.connect('bank.db')
        cursor = sqlite_connection.cursor()
        cursor.execute("SELECT code_conf FROM registration WHERE mail=?", (user_email))
        code_conf1 = cursor.fetchone()
        cursor.execute("SELECT user_code FROM registration WHERE mail=?", (user_email))
        user_code1 = cursor.fetchone()

        if code_conf1 == user_code1:
            print('победа')
        else:
            print(':(')

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



