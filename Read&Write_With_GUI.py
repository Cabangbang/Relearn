import tkinter as tk
from tkinter import *


root = tk.Tk()
root.geometry("500x450")
root.title("write file")


def open_text():
  text_file = open('Read&Write.txt', 'r')
  content = text_file.read()


  my_text.insert(END, content)
  text_file.close()

def save_text():
  text_file = open('Read&Write.txt', 'w')
  text_file.write(my_text.get(1.0, END))
                  


my_text = Text(root, width=30, height=10)
my_text.pack(pady=20)

open_button = tk.Button(root, text="Open File", command=open_text)
open_button.pack(pady=20)

save_button = tk.Button(root, text='Save file', command=save_text)
save_button.pack(pady=20)

root.mainloop()
