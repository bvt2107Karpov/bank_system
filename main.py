import customtkinter as ctk
import tkinter.messagebox as tkmb
import tkinter as tk
import sqlite3
import Login


class Main():
    def main(self):
        ctk.set_default_color_theme("green") 

        def rules_click_open():
            if rules_frame.winfo_manager():
                rules_frame.place_forget()
                label.place_forget()
            else:
                rules_frame.place(x=40, y=10)
                label.place(x=15, y=0)

        

        self.root = ctk.CTk()
        self.root.title("Bank")
        self.root.geometry("400x600")
        self.root.resizable(width=False, height=False)

        self.lbl = ctk.CTkLabel(master=self.root, text='Welcome', font=ctk.CTkFont(family='Times', size=34))
        self.lbl.pack(pady=12,padx=10)

        rules_frame = ctk.CTkFrame(self.root, width=100, height=50, corner_radius=10)

        label = ctk.CTkLabel(rules_frame, text='Номер карты')
        label.pack(pady=12,padx=10)

        rules_btn_open = ctk.CTkButton(self.root, text="🙄", width=20, height=20, command=rules_click_open)
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

        self.lbl = ctk.CTkLabel(master=self.rt, text='Choose amount to depostit', font=ctk.CTkFont(family='Times', size=18))
        self.lbl.pack(pady=12,padx=10)


        self.rt.mainloop()

    def withdraw(self):
        self.root.destroy()
        
        self.rt = ctk.CTk()
        self.rt.title("Withdraw")
        self.rt.geometry("300x450")

        btn_to_main = ctk.CTkButton(self.rt, text="←", width=35, height=35, command=self.back_to_main)
        btn_to_main.pack(side=tk.LEFT, anchor=tk.NW)

        self.lbl = ctk.CTkLabel(master=self.rt, text='Choose amount to withdraw', font=ctk.CTkFont(family='Times', size=18))
        self.lbl.pack(pady=12,padx=10)


        self.rt.mainloop()


    def transaction(self):
        self.root.destroy()

        card_number = Login.Login().return_crd_num()
        card_number = int(card_number[0])

        transaction_type = 'test'
        amount = 1


        with sqlite3.connect('bank.db') as connection:
                cursor = connection.cursor()
                cursor.execute("""
                            CREATE TABLE IF NOT EXISTS Transactions (
                                card_number INTEGER PRIMARY KEY,
                                transaction_type TEXT,
                                amount INTEGER
                            )
                            """)
                cursor.execute("INSERT INTO registration VALUES (?, ?, ?)", (card_number, transaction_type, amount))
        
        self.rt = ctk.CTk()
        self.rt.title("Transaction")
        self.rt.geometry("300x450")

        btn_to_main = ctk.CTkButton(self.rt, text="←", width=35, height=35, command=self.back_to_main)
        btn_to_main.pack(side=tk.LEFT, anchor=tk.NW)

        self.lbl = ctk.CTkLabel(master=self.rt, text='Choose amount to depostit', font=ctk.CTkFont(family='Times', size=18))
        self.lbl.pack(pady=12,padx=10)


        self.rt.mainloop()


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

        Main().main()


if __name__ == '__main__':
    Main().main()