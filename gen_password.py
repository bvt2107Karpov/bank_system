import tkinter
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import customtkinter as ctk
import password, main


class App():
    def __init__(self, login):
        super().__init__()
        self.login = login

        self.root = ctk.CTk()
        
        self.root.geometry("460x370")
        self.root.title("Password generator")
        self.root.resizable(False, False)

        self.password_frame = ctk.CTkFrame(master=self.root, fg_color="transparent")
        self.password_frame.grid(row=1, column=0, padx=(20, 20), sticky="nsew")

        self.entry_password = ctk.CTkEntry(master=self.password_frame, width=300)
        self.entry_password.grid(row=0, column=0, padx=(0, 20))

        self.btn_generate = ctk.CTkButton(master=self.password_frame, text="Generate", width=100,hover_color='purple',command=self.set_password)
        self.btn_generate.grid(row=0, column=1)

        self.settings_frame = ctk.CTkFrame(master=self.root)
        self.settings_frame.grid(row=2, column=0, padx=(20,20), pady=(20, 0), sticky="nsew")

        self.password_length_slider = ctk.CTkSlider(master=self.settings_frame, from_=0, to=100, number_of_steps=100, command=self.slider_event)
        self.password_length_slider.grid(row=1, column=0, columnspan=3, pady=(20,20), sticky="ew")

        self.password_length_entry = ctk.CTkEntry(master=self.settings_frame, width=50)
        self.password_length_entry.grid(row=1, column=3, padx=(20,10), sticky="we")

        self.cb_digits_var = tkinter.StringVar()
        self.cb_digits = ctk.CTkCheckBox(master=self.settings_frame, text="0-9", variable=self.cb_digits_var, onvalue=digits, offvalue="")
        self.cb_digits.grid(row=2, column=0, padx=10)

        self.cb_lower_var = tkinter.StringVar()
        self.cb_lower = ctk.CTkCheckBox(master=self.settings_frame, text="a-z", variable=self.cb_lower_var, onvalue=ascii_lowercase, offvalue="")
        self.cb_lower.grid(row=2, column=1)

        self.cb_upper_var = tkinter.StringVar()
        self.cb_upper = ctk.CTkCheckBox(master=self.settings_frame, text="A-Z", variable=self.cb_upper_var, onvalue=ascii_uppercase, offvalue="")
        self.cb_upper.grid(row=2, column=2)

        self.cb_symbol_var = tkinter.StringVar()
        self.cb_symbol = ctk.CTkCheckBox(master=self.settings_frame, text="@#$%", variable=self.cb_symbol_var, onvalue=punctuation, offvalue="")
        self.cb_symbol.grid(row=2, column=3)

        self.appearance_mode_option_menu = ctk.CTkOptionMenu(master=self.settings_frame, values=["Light", "Dark", "System"], command=self.appearance_mode_option_event)
        self.appearance_mode_option_menu.grid(row=3, column=0, columnspan=4, pady=(10,10))

        self.next = ctk.CTkButton(master=self.settings_frame, text='NEXT', width=50, height=40,hover_color='purple', command=self.go_next)
        self.next.grid(row=6, column=0, columnspan=7, pady=(10,10))

        self.password_length_slider.set(10)
        self.password_length_entry.insert(0, 10)
        self.appearance_mode_option_menu.set("System")



    def set_password(self):
        self.entry_password.delete(0, "end")
        self.passw = password.create_new(length=int(self.password_length_slider.get()), characters=self.get_characters())
        self.entry_password.insert(0, self.passw)


    def go_next(self):
        self.root.destroy()
        
        main.Main(self.login).option2_step2(self.passw)
        

        
    def slider_event(self, value):
        self.password_length_entry.delete(0, "end")
        self.password_length_entry.insert(0, int(value))
    
    def get_characters(self):
        chars = "".join(self.cb_digits_var.get() + self.cb_lower_var.get() + self.cb_upper_var.get() + self.cb_symbol_var.get())
        return chars


    def appearance_mode_option_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)


    def start_gen(self):
        self.root.mainloop()

