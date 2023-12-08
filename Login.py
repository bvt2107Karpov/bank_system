import customtkinter as ctk
import tkinter.messagebox as tkmb
import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
import random
import main, start


class Login():
    def _back(self):
        self.root.destroy()

        start.Start().start()

    def log(self):
        self.root = ctk.CTk()
        self.root.title("Bank")

        back = ctk.CTkButton(self.root, text="←", width=35, height=35, command=self._back)
        back.pack(side=tk.LEFT, anchor=tk.NW)

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
                main.Main().main()
                

            else:
                tkmb.showerror("Login", "Login failed!")

    def return_crd_num(self):
        with sqlite3.connect('bank.db') as sqlite_connection:
            cursor = sqlite_connection.cursor()   

            cursor.execute("SELECT card_number FROM Accounts WHERE login=?", (self.user_login.get(),)) 
            crd_num = cursor.fetchall()

        return crd_num

            
    #def skit(self):
        path = r"E:\VSC\Bank_system\img_skit"

        random_filename = random.choice([
            x for x in os.listdir(path)
            if os.path.isfile(os.path.join(path, x))
        ])

        random_filename1 = "img_skit/" + random_filename

        self.skit_root = ctk.CTk()

        self.skit_root.geometry("400x400")
        self.skit_root.title("Bank System")

        self.main_img = Image.open(random_filename1)
        self.main_img = self.main_img.resize((400, 400))
        self.main_img = ImageTk.PhotoImage(self.main_img)

        self.main_label = ctk.CTkLabel(master=self.skit_root, image=self.main_img, text='Hello, ' + str((self.skit_name[0])[0]))
        self.main_label.pack(pady=12,padx=10)

        self.skit_root.mainloop()
    
if __name__ == '__main__':
    Login().log()