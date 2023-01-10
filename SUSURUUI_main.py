import sys
import os
import tkinter as tk
from tkinter import messagebox as tkMessageBox
from tkinter import filedialog as tkFileDialog


# 実行
root = tk.Tk()        
root.title("SUSURU.DB [ SUSURUTV 訪問ラーメン店検索 ]") # タイトル
root.configure(bg='papaya whip')
root.geometry("500x800")
root.resizable(width=False, height=False)

#-----------------
label1 = tk.Label(root, text='調べたい動画を絞り込んでください',fg='black', bg='papaya whip')
label1.place(x=10, y=10,)

label2 = tk.Label(root, text='動画の回',fg='black', bg='papaya whip')
label2.place(x=10, y=50)

txt1 = tk.Entry(width=20,fg='black', bg='white')
txt1.place(x=150, y=50)

label3 = tk.Label(root, text='店名',fg='black', bg='papaya whip')
label3.place(x=10, y=100)

txt2 = tk.Entry(width=20,fg='black', bg='white')
txt2.place(x=150, y=100)

label4 = tk.Label(root, text='場所',fg='black', bg='papaya whip')
label4.place(x=10, y=150)

txt3 = tk.Entry(width=20,fg='black', bg='white')
txt3.place(x=150, y=150)

label5 = tk.Label(root, text='ラーメンの種類',fg='black', bg='papaya whip')
label5.place(x=10, y=200)

txt4 = tk.Entry(width=20,fg='black', bg='white')
txt4.place(x=150, y=200)

#-----------------
root.mainloop()