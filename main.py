import customtkinter as ctk
import tkinter.messagebox as tkmb
from PIL import Image, ImageTk
import tkinter as tk
import sqlite3, Login, gen_password, history


class Main():
    def __init__(self, login):
        super().__init__()
        self.login = login

    def main(self):

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

        btn_settings = ctk.CTkButton(master=self.root, text="⚙️", width=25, height=25, hover_color='purple', command=self.settings)
        btn_settings.pack(side=tk.RIGHT, anchor=tk.NE)

        self.lbl = ctk.CTkLabel(master=self.root, text='Welcome', font=ctk.CTkFont(family='Times', size=34), text_color='green')
        self.lbl.pack(pady=12,padx=10)

        rules_frame = ctk.CTkFrame(self.root, width=60, height=20, corner_radius=10)

        label = ctk.CTkLabel(rules_frame, text=str((self.balance[0])[0]) + '$', text_color='green')
        label.pack(pady=12,padx=10)

        

        rules_btn_open = ctk.CTkButton(master=self.root, text="View balance", hover_color='purple', width=20, height=20, command=rules_click_open)
        rules_btn_open.pack(pady=12,padx=8)

        self.user_email_confirm = ctk.CTkButton(master=self.root, text='Deposit', hover_color='purple', command=self.deposit)
        self.user_email_confirm.pack(pady=12,padx=10)

        self.user_email_confirm = ctk.CTkButton(master=self.root, text='Withdraw', hover_color='purple', command=self.withdraw)
        self.user_email_confirm.pack(pady=12,padx=10)

        self.user_email_confirm = ctk.CTkButton(master=self.root, text='Transaction', hover_color='purple', command=self.transaction)
        self.user_email_confirm.pack(pady=12,padx=10)

        self.user_email_confirm = ctk.CTkButton(master=self.root, text='History', hover_color='purple', command=self.history)
        self.user_email_confirm.pack(pady=12,padx=10)

        self.root.mainloop()


    
    
    
    def deposit(self):
        self.root.destroy()
        
        self.rt = ctk.CTk()
        self.rt.title("Deposit")
        self.rt.geometry("300x450")

        btn_to_main = ctk.CTkButton(self.rt, text="←", width=35, height=35, hover_color='purple', command=self.back_to_main)
        btn_to_main.pack(side=tk.LEFT, anchor=tk.NW)

        self.lbl = ctk.CTkLabel(master=self.rt, text='Choose amount to deposit', font=ctk.CTkFont(family='Times', size=18))
        self.lbl.pack(pady=12,padx=10)

        self._amount = ctk.CTkEntry(master=self.rt, placeholder_text="$ $ $ $ $ $ $ $ $") 
        self._amount.pack(pady=12,padx=10)

        self.btn_apply = ctk.CTkButton(master=self.rt,text='Apply', hover_color='purple',command=self.dep_apply) 
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
        self.main()



    def withdraw(self):
        self.root.destroy()
        
        self.rt = ctk.CTk()
        self.rt.title("Withdraw")
        self.rt.geometry("300x450")

        btn_to_main = ctk.CTkButton(self.rt, text="←", width=35, height=35, hover_color='purple', command=self.back_to_main)
        btn_to_main.pack(side=tk.LEFT, anchor=tk.NW)

        self.lbl = ctk.CTkLabel(master=self.rt, text='Choose amount to withdraw', font=ctk.CTkFont(family='Times', size=18))
        self.lbl.pack(pady=12,padx=10)

        self._amount = ctk.CTkEntry(master=self.rt, placeholder_text="$ $ $ $ $ $ $ $ $") 
        self._amount.pack(pady=12,padx=10)

        self.btn_apply = ctk.CTkButton(master=self.rt,text='Apply', hover_color='purple',command=self.withdraw_apply) 
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
        self.main()


    def transaction(self):
        self.root.destroy()
       
        self.rt = ctk.CTk()
        self.rt.title("Transaction")
        self.rt.geometry("300x450")

        btn_to_main = ctk.CTkButton(self.rt, text="←", width=35, height=35, hover_color='purple', command=self.back_to_main)
        btn_to_main.pack(side=tk.LEFT, anchor=tk.NW)

        self.lbl = ctk.CTkLabel(master=self.rt, text="Enter the recipient's card number", font=ctk.CTkFont(family='Times', size=18))
        self.lbl.pack(pady=12,padx=10)

        self._card_num = ctk.CTkEntry(master=self.rt, placeholder_text="# # # # # # # # # ") 
        self._card_num.pack(pady=12,padx=10)
        
        self.lbl1 = ctk.CTkLabel(master=self.rt, text='Choose amount to transfer', font=ctk.CTkFont(family='Times', size=18))
        self.lbl1.pack(pady=12,padx=10)

        self._amount = ctk.CTkEntry(master=self.rt, placeholder_text="$ $ $ $ $ $ $ $ $") 
        self._amount.pack(pady=12,padx=10)

        self.btn_apply = ctk.CTkButton(master=self.rt,text='Apply', hover_color='purple',command=self.trans_apply) 
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
                cursor.execute("update Accounts set balance=? where login=?", (self.bal, str((self.login[0])[0]),))
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

        history.Table().start_history(self.login)

    
    def back_to_main(self):
        self.rt.destroy()

        Main(self.login).main()

    
    def settings(self):
        self.root.destroy()

        self.rt = ctk.CTk()
        self.rt.protocol("WM_DELETE_WINDOW", lambda: None)
        self.rt.geometry("250x500")
        self.rt.title("Bank System")
        
        self.lbl_switch_theme = ctk.CTkLabel(master=self.rt, text='Choose Theme', font=ctk.CTkFont(family='Times', size=14))
        self.lbl_switch_theme.pack(pady=12,padx=10)

        self.switch_theme = ctk.CTkOptionMenu(master=self.rt, values=["Light", "Dark", "System"], command=self.appearance_mode_option_event)
        self.switch_theme.pack(pady=12,padx=10)
        
        self.btn_change_password = ctk.CTkButton(master=self.rt, text='Press to change your password', width=25, height=25, font=ctk.CTkFont(family='Times', size=14), hover_color='purple', command=self.change_password)
        self.btn_change_password.pack(pady=12,padx=10)
        
        self.btn_log_out = ctk.CTkButton(master=self.rt, text='Log Out', width=25, height=25, font=ctk.CTkFont(family='Times', size=14), hover_color='purple', command=self.log_out)
        self.btn_log_out.pack(pady=12,padx=10)

        self.btn_close_settings = ctk.CTkButton(self.rt, text="Close", width=25, height=25, hover_color='purple', command=self.back_to_main)
        self.btn_close_settings.pack(pady=12,padx=10, side=tk.BOTTOM)
        
        self.rt.mainloop()


    def log_out(self):
        self.rt.destroy()

        Login.Login().log()


    def appearance_mode_option_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)
        self.switch_theme.set(str(new_appearance_mode))


    def change_password(self):
        self.password_root = ctk.CTk()
        self.password_root.protocol("WM_DELETE_WINDOW", lambda: None)
        self.password_root.geometry('350x200')


        self.lbl_password_change = ctk.CTkLabel(master=self.password_root, text="Choose options to change password", font=ctk.CTkFont(family='Times', size=18))
        self.lbl_password_change.pack(pady=12, padx=10)

        self.btn1_password = ctk.CTkButton(master=self.password_root, text='Enter the password yourself', width=28, height=28, font=ctk.CTkFont(family='Times', size=18), hover_color='purple', command=self.option1)
        self.btn1_password.pack(pady=10, padx=12)

        self.btn2_password = ctk.CTkButton(master=self.password_root, text='Password generator', width=28, height=28, font=ctk.CTkFont(family='Times', size=18), hover_color='purple', command=self.option2)
        self.btn2_password.pack(pady=10, padx=12)

        self.password_root.mainloop()

    def option1(self):
        self.set_password = ctk.CTk()

        self.old_password = ctk.CTkEntry(self.set_password, placeholder_text="Enter your old password")
        self.old_password.pack(pady=12, padx=10)

        self.new_password = ctk.CTkEntry(self.set_password, placeholder_text="Enter your new password")
        self.new_password.pack(pady=12, padx=10)

        self.btn_confirm = ctk.CTkButton(self.set_password, text='Confirm', width=24, height=24, font=ctk.CTkFont(family='Times', size=18), hover_color='purple', command=self.option1_step2)
        self.btn_confirm.pack(pady=12, padx=10)

        self.set_password.mainloop()

        
        
    def option1_step2(self):
        with sqlite3.connect('bank.db') as sqlite_connection:
            cursor = sqlite_connection.cursor()
            cursor.execute("SELECT password FROM Accounts WHERE login=?", (str((self.login[0])[0]),))
            self.old_password_bd = cursor.fetchall()
            
            if self.old_password.get() == (self.old_password_bd[0])[0]:
                    cursor.execute("update Accounts set password=? where login=?", (str(self.new_password.get()), str((self.login[0])[0]),))

                    tkmb.showinfo('', 'Now your password is ' + str(self.new_password.get()) + '!')
                    sqlite_connection.commit()
                    self.set_password.destroy()
                    self.password_root.destroy()
                    self.rt.destroy()

                    Main(self.login).main()


                
            else:
                tkmb.showerror('Failed', 'Changing password was failed!')


    def option2(self):
        self.rt.destroy()
        self.password_root.destroy()

        gen_password.App(self.login).start_gen()



        
    def option2_step2(self, password):
        self.password = password

        with sqlite3.connect('bank.db') as sqlite_connection:
            cursor = sqlite_connection.cursor()
            cursor.execute("update Accounts set password=? where login=?", (str(self.password), str((self.login[0])[0]),))
            sqlite_connection.commit()
            tkmb.showinfo('', 'Now your password is ' + str(self.password) + '!')

            Main(self.login).main()


    

        