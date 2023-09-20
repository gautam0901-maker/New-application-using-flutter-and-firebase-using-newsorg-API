import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import *
from tkinter import messagebox
import requests
import json
import webbrowser
#from tkHyperLinkManager import HyperlinkManager
type = 'sports'
apiKey = '6c2ae8915e2946fc9da93547c6578250'
BASE_URL = f'http://newsapi.org/v2/top-headlines?country=in&category=general&apiKey='+apiKey

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    global apiKey, type
    def __init__(self):
        super().__init__()

        # configure window
        self.title("ZF News")
        self.geometry(f"{1100}x{580}")
        self.attributes('-alpha',1.0)

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="ZF News", font=customtkinter.CTkFont(size=25, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.method1,text= 'New Joiners')
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.new_method,text='News')
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.method1,text='Notes')
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        
        # create main entry and button
        # self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        # self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        # self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        # self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox

        # self.method1() 
        self.new_method()
    def method1(self):
        self.textbox1 = customtkinter.CTkTextbox(self,height= 1500, width=100)
        self.textbox1.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
        type = 'technology'
        BASE_URL = f'www.google.com'
        self.textbox1.insert(END, 'text1')
        self.textbox1.delete("1.0", END)
        # try:
        #     articles = (requests.get(BASE_URL).json())['articles']
        #     if(articles != 0):
        #         for i in range(len(articles)):
        #             self.textbox1.insert(END, f'News : {i+1}\n\n')
        #             self.textbox1.insert(END, f"{articles[i]['title']}\n")
        #             self.textbox1.insert(END, f"{articles[i]['description']}\n\n")
        #             self.textbox1.insert(END, f"{articles[i]['content']}\n\n")

        #             self.textbox1.insert(END, f"link : {articles[i]['url']}\n")
        #             self.textbox1.insert(END, "\n\n")
                    
        #     else:
        #         self.textbox1.insert(END, "Sorry no news available")
        # except Exception as e:
        #     messagebox.showerror('ERROR', "Sorry cant connect to internet or some issues with ZF newsapp")    


    def new_method(self):
        self.textbox = customtkinter.CTkTextbox(self,height= 1500, width=100)
        self.textbox.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
        type1 = 'general'
        BASE_URL = f'http://newsapi.org/v2/top-headlines?country=in&category={type1}&apiKey='+apiKey
        self.textbox.delete("1.0", END)
        try:
            articles = (requests.get(BASE_URL).json())['articles']
            if(articles != 0):
                for i in range(len(articles)):
                    self.textbox.insert(END, f'News : {i+1}\n\n')
                    self.textbox.insert(END, f"{articles[i]['title']}\n")
                    self.textbox.insert(END, f"{articles[i]['description']}\n\n")
                    self.textbox.insert(END, f"{articles[i]['content']}\n\n")

                    self.textbox.insert(END, f"link : {articles[i]['url']}\n")
                    self.textbox.insert(END, "\n\n")
            else:
                self.textbox.insert(END, "Sorry no news available")
        except Exception as e:
            messagebox.showerror('ERROR', "Sorry cant connect to internet or some issues with ZF newsapp")               
       

    # def open_input_dialog_event(self):
    #     dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
    #     print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event1(self):
        print("sidebar_button click")
    def sidbar_event_2(self):
        print("Second event clicked")    


if __name__ == "__main__":
    app = App()

    app.mainloop()
