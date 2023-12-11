import customtkinter as ctk
import tkinter.messagebox as tkmb
import tkinter as tk
import sqlite3
import Login


class Main():
    def main(self, login):
        self.login = login

        ctk.set_default_color_theme("green") 

        def rules_click_open():
            if rules_frame.winfo_manager():
                rules_frame.place_forget()
                label.place_forget()
            else:
                rules_frame.place(x=40, y=10)
                label.place(x=15, y=0)

        with sqlite3.connect('bank.db') as sqlite_connection:
            cursor = sqlite_connection.cursor()   

            cursor.execute("SELECT balance FROM Accounts WHERE login=?", ((self.login[0])[0],))           
            self.balance = cursor.fetchall()

            cursor.execute("SELECT card_number FROM Accounts WHERE login=?", ((self.login[0])[0],))           
            self.card_number = cursor.fetchall()


        


    

        self.root = ctk.CTk()
        self.root.title("Bank")
        self.root.geometry("400x600")
        self.root.resizable(width=False, height=False)

        self.lbl = ctk.CTkLabel(master=self.root, text='Welcome', font=ctk.CTkFont(family='Times', size=34), text_color='green')
        self.lbl.pack(pady=12,padx=10)

        rules_frame = ctk.CTkFrame(self.root, width=60, height=20, corner_radius=10)

        label = ctk.CTkLabel(rules_frame, text=str((self.balance[0])[0]) + '$', text_color='green')
        label.pack(pady=12,padx=10)

        rules_btn_open = ctk.CTkButton(self.root, text="View balance", width=20, height=20, command=rules_click_open)
        rules_btn_open.pack(pady=12,padx=8)

        self.user_email_confirm = ctk.CTkButton(master=self.root, text='Deposit', command=self.deposit)
        self.user_email_confirm.pack(pady=12,padx=10)

        self.user_email_confirm = ctk.CTkButton(master=self.root, text='Withdraw', command=self.withdraw)
        self.user_email_confirm.pack(pady=12,padx=10)

        self.user_email_confirm = ctk.CTkButton(master=self.root, text='Transaction', command=self.transaction)
        self.user_email_confirm.pack(pady=12,padx=10)

        self.user_email_confirm = ctk.CTkButton(master=self.root, text='History', command=self.history)
        self.user_email_confirm.pack(pady=12,padx=10)

        self.root.mainloop()


    def deposit(self):
        self.root.destroy()
        
        self.rt = ctk.CTk()
        self.rt.title("Deposit")
        self.rt.geometry("300x450")

        btn_to_main = ctk.CTkButton(self.rt, text="←", width=35, height=35, command=self.back_to_main)
        btn_to_main.pack(side=tk.LEFT, anchor=tk.NW)

        self.lbl = ctk.CTkLabel(master=self.rt, text='Choose amount to deposit', font=ctk.CTkFont(family='Times', size=18))
        self.lbl.pack(pady=12,padx=10)

        self._amount = ctk.CTkEntry(master=self.rt, placeholder_text="$ $ $ $ $ $ $ $ $") 
        self._amount.pack(pady=12,padx=10)

        self.btn_apply = ctk.CTkButton(master=self.rt,text='Apply',command=self.dep_apply) 
        self.btn_apply.pack(pady=12,padx=10)


        self.rt.mainloop()

    def dep_apply(self):
        transaction_type = "Deposit"
        self.bal = int((self.balance[0])[0]) + int(self._amount.get())

        with sqlite3.connect('bank.db') as sqlite_connection:
            cursor = sqlite_connection.cursor()   

            cursor.execute("update Accounts set balance=? where login=?", (self.bal, (self.login[0])[0],))

            cursor.execute("""
                        CREATE TABLE IF NOT EXISTS transactions (
                            card_number INTEGER,
                            transaction_type TEXT,
                            amount INTEGER
                        )
                        """)
            cursor.execute("INSERT INTO transactions VALUES (?, ?, ?)", ((self.card_number[0])[0], transaction_type, self._amount.get()))       

            

        self.rt.destroy()
        self.main(self.login)



    def withdraw(self):
        self.root.destroy()
        
        self.rt = ctk.CTk()
        self.rt.title("Withdraw")
        self.rt.geometry("300x450")

        btn_to_main = ctk.CTkButton(self.rt, text="←", width=35, height=35, command=self.back_to_main)
        btn_to_main.pack(side=tk.LEFT, anchor=tk.NW)

        self.lbl = ctk.CTkLabel(master=self.rt, text='Choose amount to withdraw', font=ctk.CTkFont(family='Times', size=18))
        self.lbl.pack(pady=12,padx=10)

        self._amount = ctk.CTkEntry(master=self.rt, placeholder_text="$ $ $ $ $ $ $ $ $") 
        self._amount.pack(pady=12,padx=10)

        self.btn_apply = ctk.CTkButton(master=self.rt,text='Apply',command=self.withdraw_apply) 
        self.btn_apply.pack(pady=12,padx=10)

        self.rt.mainloop()


    def withdraw_apply(self):
        transaction_type = "Withdraw"
        if int((self.balance[0])[0]) >= int(self._amount.get()):
            self.bal = int((self.balance[0])[0]) - int(self._amount.get())
            with sqlite3.connect('bank.db') as sqlite_connection:
                cursor = sqlite_connection.cursor()
                cursor.execute("update Accounts set balance=? where login=?", (self.bal, (self.login[0])[0],))

                cursor.execute("""
                        CREATE TABLE IF NOT EXISTS transactions (
                            card_number INTEGER,
                            transaction_type TEXT,
                            amount INTEGER
                        )
                        """)
                cursor.execute("INSERT INTO transactions VALUES (?, ?, ?)", ((self.card_number[0])[0], transaction_type, self._amount.get()))
        else:
            tkmb.showerror('Error', 'There are not enough funds')

    

        self.rt.destroy()
        self.main(self.login)


    def transaction(self):
        self.root.destroy()
       
        self.rt = ctk.CTk()
        self.rt.title("Transaction")
        self.rt.geometry("300x450")

        btn_to_main = ctk.CTkButton(self.rt, text="←", width=35, height=35, command=self.back_to_main)
        btn_to_main.pack(side=tk.LEFT, anchor=tk.NW)

        self.lbl = ctk.CTkLabel(master=self.rt, text="Enter the recipient's card number", font=ctk.CTkFont(family='Times', size=18))
        self.lbl.pack(pady=12,padx=10)

        self._card_num = ctk.CTkEntry(master=self.rt, placeholder_text="# # # # # # # # # ") 
        self._card_num.pack(pady=12,padx=10)
        
        self.lbl1 = ctk.CTkLabel(master=self.rt, text='Choose amount to transfer', font=ctk.CTkFont(family='Times', size=18))
        self.lbl1.pack(pady=12,padx=10)

        self._amount = ctk.CTkEntry(master=self.rt, placeholder_text="$ $ $ $ $ $ $ $ $") 
        self._amount.pack(pady=12,padx=10)

        self.btn_apply = ctk.CTkButton(master=self.rt,text='Apply',command=self.trans_apply) 
        self.btn_apply.pack(pady=12,padx=10)


        self.rt.mainloop()


    def trans_apply(self):
        ctk.set_default_color_theme("blue")

        self.chck = ctk.CTk()
        self.chck.title("Confirm")
        self.chck.geometry("250x150")

        with sqlite3.connect('bank.db') as sqlite_connection:
                cursor = sqlite_connection.cursor()
                cursor.execute("SELECT name FROM Accounts where card_number=?", (self._card_num.get(),))
                name_check = cursor.fetchall()

        txt = "You confirm the transfer of " + str(self._amount.get()) + "$ to " + str((name_check[0])[0]) + "?"

        self.lbl = ctk.CTkLabel(master=self.chck, text=txt, font=ctk.CTkFont(family='Times', size=12))
        self.lbl.pack(pady=12,padx=10)

        self.btn_yes = ctk.CTkButton(master=self.chck,text='Yes',command=self.trans_apply_fin) 
        self.btn_yes.pack(pady=12,padx=10)

        self.btn_no = ctk.CTkButton(master=self.chck,text='No',command=self.trans_back) 
        self.btn_no.pack(pady=12,padx=10)
        
        self.chck.mainloop()
    
    def trans_back(self):
        self.chck.destroy()
        ctk.set_default_color_theme("green")

    def trans_apply_fin(self):
        self.chck.destroy()

        transaction_type = "Transaction"

        if int((self.balance[0])[0]) >= int(self._amount.get()):
            with sqlite3.connect('bank.db') as sqlite_connection:
                cursor = sqlite_connection.cursor()
                cursor.execute("SELECT balance FROM Accounts where card_number=?", (self._card_num.get(),))
                self.recipient_bal= cursor.fetchall()
            
            self.bal = int((self.balance[0])[0]) - int(self._amount.get())
            self.recipient_bal = int((self.recipient_bal[0])[0]) + int(self._amount.get())
            
            with sqlite3.connect('bank.db') as sqlite_connection:
                cursor = sqlite_connection.cursor()
                cursor.execute("update Accounts set balance=? where login=?", (self.bal, (self.login[0])[0],))
                cursor.execute("update Accounts set balance=? where card_number=?", (self.recipient_bal, self._card_num.get(),))

                cursor.execute("""
                            CREATE TABLE IF NOT EXISTS transactions (
                                card_number INTEGER,
                                transaction_type TEXT,
                                amount INTEGER
                            )
                            """)
                cursor.execute("INSERT INTO transactions VALUES (?, ?, ?)", ((self.card_number[0])[0], transaction_type, self._amount.get()))

        else:
            tkmb.showerror('Error', 'There are not enough funds')


    def history(self):
        self.root.destroy()

        
        
        self.rt = ctk.CTk()
        self.rt.title("History")
        self.rt.geometry("350x500")

        btn_to_main = ctk.CTkButton(self.rt, text="←", width=35, height=35, command=self.back_to_main)
        btn_to_main.pack(side=tk.LEFT, anchor=tk.NW)

        self.lbl = ctk.CTkLabel(master=self.rt, text='History of transactions', font=ctk.CTkFont(family='Times', size=18))
        self.lbl.pack(pady=12,padx=10)


        self.rt.mainloop()

    
    def back_to_main(self):
        self.rt.destroy()

        Main().main(self.login)


if __name__ == '__main__':
    Main().main()