import customtkinter as ctk
import tkinter as tk
import tkinter.ttk as ttk
import sqlite3, main

class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)

        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings
  
        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)
  
        for row in rows:
            table.insert('', tk.END, values=tuple(row))
  
        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)
    

    
  
    def start_history(self, login):
        self.login = login

        with sqlite3.connect('bank.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT card_number FROM Accounts where login=?", (str((self.login[0])[0]),))
            self.card_number = cursor.fetchall()



        data = ()

        with sqlite3.connect('bank.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM transactions where card_number=?", ((self.card_number[0])[0],))
            data = (row for row in cursor.fetchall())

        self.root = ctk.CTk()

        btn_to_main = ctk.CTkButton(self.root, text="←", width=35, height=35, hover_color='purple', command=self.back_to_main)
        btn_to_main.pack(side=tk.LEFT, anchor=tk.NW)

        lb = ctk.CTkLabel(self.root, text='History of transactions', font=ctk.CTkFont(family='Times', size=18))
        lb.pack(pady=12,padx=10)

        table = Table(self.root, headings=('Card number', 'Transaction Type', 'Amount'), rows=data)
        table.pack(expand=tk.YES, fill=tk.BOTH)

        self.root.mainloop()


    def back_to_main(self):
        self.root.destroy()
        main.Main(self.login).main()