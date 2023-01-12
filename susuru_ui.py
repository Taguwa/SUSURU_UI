import sys
import os
import sqlite3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

# sqliteの初期設定
dbfile = "test.db"
conn = sqlite3.connect(dbfile)
cur = conn.cursor()#データベースを操作するカーソルを指定

# tkinter UIの初期設定
root = tk.Tk()
root.title("SUSURU.DB [ SUSURUTV 訪問ラーメン店検索 ]") # タイトル
root.configure(bg='papaya whip')#ウィンドウの設定 bg=背景色
root.geometry("600x800")#ウィンドウサイズ
root.resizable(width=False, height=False)#ウィンドウサイズを変更不可に

#-----------------1回のみ実行する郡 CREATEやINSERT,DELETE等を書く----------------
# テーブル作成処理
#cur.execute('CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT,name STRING)')

# 情報の追加
#cur.execute('INSERT INTO persons(name) values("Hanako")')
#cur.execute('INSERT INTO persons(name) values("Hiroki")')

# データベースへコミット
#conn.commit()
#----------------------------------------------------------------------------

for data in cur.execute("SELECT * FROM persons"):
    print(data)

# 関数
def search():
    cur.execute("SELECT name FROM persons WHERE id = '" + txt3.get() + "';");#入力された番号からid検索してnameを持ってくる
    label_ans = tk.Label(root, text = cur.fetchall(), fg='black', bg='papaya whip')
    label_ans.place(x=10, y=150)
    #検索条件に合う店舗数
    num = 0
    #message alertで出すメッセージを生成
    message = "以下の情報で検索しました。\n" + "ラーメンの種類 : " + select_ramen.get() + "\n" + "地域 : " + select_ramen.get() + "\n" + "動画の回 : " + select_ramen.get() + "\n\n\n条件に合う店舗が"+ str(num) +"件見つかりました"
    ret = messagebox.showinfo(  title = "検索",
                                message = message)
    _label = tk.Label(movie_frame, text='ここにdbから持ってきた情報を挿入',fg='black', bg='papaya whip')
    _label.place(x=10,y=10)


# UI
label1 = tk.Label(root, text='検索したいラーメンの種類を選択してください',fg='black', bg='papaya whip')
label1.place(x=10, y=50)
ramen = ["醤油", "味噌", "豚骨", "家系"]
select_ramen = ttk.Combobox(root, value=ramen, height=10, width=20)
select_ramen.place(x=300, y=50)

label2 = tk.Label(root, text='探したいお店の地域を入力してください',fg='black', bg='papaya whip')
label2.place(x=10, y=100)
select_place = tk.Entry(width=20,fg='black', bg='white')
select_place.place(x=300, y=100)

label3 = tk.Label(root, text='動画の回で直接検索',fg='black', bg='papaya whip')
label3.place(x=10, y=150)
txt3 = tk.Entry(width=20,fg='black', bg='white')
txt3.place(x=300, y=150)

botton_label = tk.Label(root, text='上記のボックスに入力した情報に合う、SUSURUTVが訪問したラーメンの店舗を検索できます。\n複数ある場合は複数、条件を細かく指定すればその条件に合った店舗が出てきます。',fg='black', bg='papaya whip')
botton_label.place(x=10, y=200)
button1 = tk.Button(root, text = '検索', command = search ,bg = "papaya whip")
button1.place(x=200, y=250)

movie_frame = tk.Frame(root, bd=2,bg="#455A64",relief='ridge' ,width=580,height=400)
movie_frame.place(x=10,y=300)

root.mainloop()#ウィンドウを更新

conn.close
