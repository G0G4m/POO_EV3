import tkinter as tk
import sys

class redirect_text():
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self,string):
        self.text_widget.insert(tk.END,string)
        self.text_widget.see(tk.END)

    def terminal_text(subtab):
        terminal_text = tk.Text(subtab,wrap="word",highlightthickness=2,font=("arial",10))
        terminal_text.place(x=12,y=570,height=40,width=518)
        terminal_text.config(tk.END,)

        redir = terminal_text
        sys.stdout = redir