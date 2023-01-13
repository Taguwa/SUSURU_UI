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

#
# 関数
#

def search():
    cur.execute("SELECT name FROM persons WHERE id = '" + txt3.get() + "';");#入力された番号からid検索してnameを持ってくる
    label_ans = tk.Label(root, text = cur.fetchall(), fg='black', bg='papaya whip')
    label_ans.place(x=10, y=150)
    #検索条件に合う店舗数
    result()

def result():
    #message alertで出すメッセージを生成
    num = 0
    message = "以下の情報で検索しました。\n" + "ラーメンの種類 : " + select_ramen.get() + "\n" + "地域 : " + select_ramen.get() + "\n" + "動画の回 : " + select_ramen.get() + "\n\n\n条件に合う店舗が"+ str(num) +"件見つかりました"
    ret = messagebox.showinfo(  title = "検索",
                                message = message)

    _label = tk.Label(movie_frame, text='ここにdbから持ってきた情報を挿入',fg='black', bg='papaya whip')
    _label.place(x=10,y=10)

    _label2 = tk.Label(movie_frame, text='ここにdbから持ってきた情報を挿入',fg='black', bg='papaya whip')
    _label2.place(x=10,y=10)


#
# UI
#

#種類のラベルとボックス
label1 = tk.Label(root, text='検索したいラーメンの種類を選択',fg='black', bg='papaya whip')
label1.place(x=10, y=50)
ramen = ["醤油", "味噌", "豚骨", "家系"]
select_ramen = ttk.Combobox(root, value=ramen, height=10, width=20)
select_ramen.place(x=300, y=50)

#地域のラベルとボックス
label2 = tk.Label(root, text='探したいお店の都道府県を選択',fg='black', bg='papaya whip')
label2.place(x=10, y=100)
pl= ["北海道","青森県","岩手県","宮城県","秋田県","山形県","福島県","茨城県","栃木県","群馬県","埼玉県","千葉県","東京都","神奈川県","新潟県","富山県","石川県","福井県","山梨県","長野県","岐阜県","静岡県","愛知県","三重県","滋賀県","京都府","大阪府","兵庫県","奈良県","和歌山県","鳥取県","島根県","岡山県","広島県","山口県","徳島県","香川県","愛媛県","高知県","福岡県","佐賀県","長崎県","熊本県","大分県","宮崎県","鹿児島県","沖縄県"]
select_place = ttk.Combobox(root,value=pl, height=10, width=20)
select_place.place(x=300, y=100)

#回のラベルとボックス
label3 = tk.Label(root, text='動画の回で直接指定',fg='black', bg='papaya whip')
label3.place(x=10, y=150)
txt3 = tk.Entry(width=20,fg='black', bg='white')
txt3.place(x=300, y=150)

#メッセージと検索ボタン
botton_label = tk.Label(root, text='上記のボックスに入力した情報に合う、SUSURUTVが訪問したラーメンの店舗を検索できます。\n複数ある場合は複数、条件を細かく指定すればその条件に合った店舗が出てきます。',fg='black', bg='papaya whip')
botton_label.place(x=10, y=200)
button1 = tk.Button(root, text = '検索', command = search ,bg = "papaya whip")
button1.place(x=200, y=250)

#表示フレーム
movie_frame = tk.Frame(root, bd=2,bg="#455A64",relief='ridge' ,width=580,height=400)
movie_frame.place(x=10,y=300)

#ウィンドウを更新
root.mainloop()
conn.close
