from tkinter import *
from tkinter import messagebox
import requests
import json
type = 'sports'
apiKey = '6c2ae8915e2946fc9da93547c6578250'
BASE_URL = f'http://newsapi.org/v2/top-headlines?country=in&category={type}&apiKey='+apiKey
file1 = open('myfile.txt', 'w')

class NewsApp:
	global apiKey, type

	def __init__(self, root):
		self.root = root
		self.root.geometry('1350x700+0+0')
		self.root.title("ZF news")

		
		self.newsCatButton = []
		self.newsCat = ["general", "entertainment",
						"business", "sports", "technology", "health"]

		
		bg_color = "#2340cb"
		text_area_bg = "#feffff"
		basic_font_color = "#feffff"
		title = Label(self.root, text="ZF NEWSapp", font=("times new roman", 30, "bold"),
					pady=2, bd=12, relief=GROOVE, bg=bg_color, fg=basic_font_color).pack(fill=X)

		F1 = LabelFrame(self.root, text="Category", font=(
			"times new roman", 20, "bold"), bg=bg_color, fg=basic_font_color, bd=10, relief=GROOVE)
		F1.place(x=0, y=80, width=300, relheight=0.88)

		for i in range(len(self.newsCat)):
			b = Button(F1, text=self.newsCat[i].upper(
			), width=20, bd=7, font="arial 15 bold")
			b.bg = basic_font_color,
			b.grid(row=i, column=0, padx=10, pady=5)
			b.bind('<Button-1>', self.Newsarea)
			self.newsCatButton.append(b)

		
		F2 = Frame(self.root, bd=7, relief=GROOVE)
		F2.place(x=320, y=80, relwidth=0.7, relheight=0.8)
		news_title = Label(F2, text="News Area", font=(
			"arial", 20, "bold"), bd=7, relief=GROOVE).pack(fill=X)
		scroll_y = Scrollbar(F2, orient=VERTICAL)
		self.txtarea = Text(F2, yscrollcommand=scroll_y.set, font=(
			"times new roman", 15, "bold"), bg=text_area_bg, fg="#7d5d5f")
		scroll_y.pack(side=RIGHT, fill=Y)
		scroll_y.config(command=self.txtarea.yview)
		self.txtarea.insert(
			END, "PLEASE SELECT ANY CATEGORY TO SHOW HEADLINES")
		self.txtarea.pack(fill=BOTH, expand=1)

	def Newsarea(self, event):
		type = event.widget.cget('text').lower()
		BASE_URL = f'http://newsapi.org/v2/top-headlines?country=in&category={type}&apiKey='+apiKey
		self.txtarea.delete("1.0", END)
		self.txtarea.insert(END, f"\n Welcome to ZF news paper\n")
		self.txtarea.insert(
			END, "--------------------------------------------------------------------\n")
		try:
			articles = (requests.get(BASE_URL).json())['articles']
			if(articles != 0):
				for i in range(len(articles)):
					self.txtarea.insert(END, f"{articles[i]['title']}\n")
					self.txtarea.insert(
						END, f"{articles[i]['description']}\n\n")
					self.txtarea.insert(END, f"{articles[i]['content']}\n\n")
					self.txtarea.insert(
						END, f"read more...{articles[i]['url']}\n")
					self.txtarea.insert(
						END, "--------------------------------------------------------------------")
					self.txtarea.insert(
						END, "--------------------------------------------------------------------\n\n")
			else:
				self.txtarea.insert(END, "Sorry no news available")
		except Exception as e:
			messagebox.showerror(
				'ERROR', "Sorry cant connect to internet or some issues with newsapp :'(")


root = Tk()
obj = NewsApp(root)
root.mainloop()
