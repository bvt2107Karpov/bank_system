import customtkinter as ctk
import tkinter.messagebox as tkmb
import sqlite3



def log():
    def acc_log():
        if user_entry and user_pass:
            try:
                # Establish a connection with the database
                connection = sqlite3.connect("banking_system.db")

                # Create a cursor object
                cursor = connection.cursor()

                # Execute the SQL query to check if the username and password exist in the database
                cursor.execute("SELECT * FROM account WHERE entry = ? AND passw = ?", (user_entry, user_pass))

                # Fetch all the rows from the last executed SQL query
                users = cursor.fetchall()

                # Close the connection with the database
                connection.close()

                # Display a message box based on the existence of the username and password in the database
                if users:
                    tkmb.showinfo("Login", "Login successful!")
                else:
                    tkmb.showerror("Login", "Login failed!")
            except sqlite3.Error as error:
                tkmb.showerror("Error", "Error")

        else:
            tkmb.showerror("Login", "Login failed!")
        

    root = ctk.CTk()
    root.title("Bank")


    lbl = ctk.CTkLabel(master=root, text='Log in')
    lbl.pack(pady=12,padx=10)


    user_entry = ctk.CTkEntry(master=root,placeholder_text="Username") 
    user_entry.pack(pady=12,padx=10) 

    user_pass = ctk.CTkEntry(master=root,placeholder_text="Password",show="*") 
    user_pass.pack(pady=12,padx=10)

    button_login = ctk.CTkButton(master=root,text='Login',command=acc_log) 
    button_login.pack(pady=12,padx=10)

    checkbox = ctk.CTkCheckBox(master=root,text='Remember Me') 
    checkbox.pack(pady=12,padx=10)

    root.mainloop()
