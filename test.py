import sys
import os
import sqlite3
import webbrowser
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

# sqliteの初期設定
dbfile = "susuru_test.db"
conn = sqlite3.connect(dbfile)
cur = conn.cursor()#データベースを操作するカーソルを指定

# tkinter UIの初期設定
root = tk.Tk()
root.title("SUSURU.DB [ SUSURUTV 訪問ラーメン店検索 ]") # タイトル
root.configure(bg='papaya whip')#ウィンドウの設定 bg=背景色
root.geometry("900x800")#ウィンドウサイズ
root.resizable(width=False, height=False)#ウィンドウサイズを変更不可に

def jump_to_link(url):
    webbrowser.open_new(url)

#-----------------1回のみ実行する郡 CREATEやINSERT,DELETE等を書く----------------

stores = [
    (2561,"【二郎系】お前がナンバーワンだ。千葉最強の二郎系ラーメンがウマスギィ！絶えない行列。をすする Boo Boo 太郎。","https://www.youtube.com/watch?v=UUXcdCDnNk0&ab_channel=SUSURUTV.","二郎系","千葉","中央区","Boo Boo 太郎"),
    (2566,"【家系】これ飲み干せる‥！今年オープンなのに完成度高すぎる家系ラーメンと、ご飯より肉が多いチャーシュー丼。をすする 【飯テロ】SUSURU TV.第2566回","https://www.youtube.com/watch?v=jDAxQV3rF3g","家系","神奈川県","横浜市","横浜ラーメン斎藤屋"),
    (2534,"【TKG】食べれば食べるだけ辛くなる濃厚味噌をライスと共に。をすする 濃厚味噌ラーメン 味噌道場 戸田支部【飯テロ】SUSURU TV.第2534回","https://www.youtube.com/watch?v=A8gywLMgFCE","味噌","埼玉県","戸田市","味噌道場戸田支部"),
  ]
# テーブル作成処理
#cur.execute('CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT,name STRING)')
#cur.execute('CREATE TABLE susurus(part INTEGER, videoname STRING, url STRING, type STRING, pre STRING, area STRING, storename STRING)')

# 情報の追加
#cur.execute('INSERT INTO persons(name) values("Hanako")')
#cur.execute('INSERT INTO persons(name) values("Hiroki")')
#sql = "INSERT INTO susurus (part, videoname, url, type, pre, area, storename) VALUES (?, ?, ?, ?, ?, ?, ?)"

#cur.executemany(sql, stores)

# データベースへコミット
#conn.commit()
#----------------------------------------------------------------------------

#for data in cur.execute("SELECT * FROM susurus"):
#    print(data)

def search():
    #検索SQLを形成
    sql_search = []
    sql_doc = "SELECT videoname, url FROM susurus"

    if txt_part.get() != "":#パート検索は1つのみなのでこっちを優先
        sql_doc += " WHERE part = " + txt_part.get() + " "

    else:
        if select_type.get() != "":#他3つは複数絞り込み
            sql_search.append("type like '%" + select_type.get() + "%'")

        if select_pre.get() != "":
            sql_search.append("pre like '%" + select_pre.get() + "%'")

        if txt_area.get() != "":
            sql_search.append("area like '%" + txt_area.get() + "%'")

        sql_doc += " WHERE " + " AND ".join(sql_search)

    print(sql_doc)

    search_data = []
    for i in cur.execute(sql_doc):#sqlの結果を保存
        search_data.append(i)

    search_data_length = len(search_data)
    result(str(search_data_length), search_data)

def result(length ,data):#結果を出力する
    #まずは検索結果数を表示
    if txt_part.get() == "":
        message = "以下の情報で検索しました。\n" + "ラーメンの種類 : " + select_type.get() + "\n" + "都道府県 : " + select_pre.get() + "\n" + "市区町村 : " + txt_area.get() + "\n\n\n条件に合う店舗が"+ length +"件見つかりました"

    else:
        message = "以下の情報で検索しました。\n" + "動画の回 : " + txt_part.get() + "\n\n\n条件に合う店舗が1件見つかりました"

    ret = messagebox.showinfo(  title = "検索",
                                message = message)
    Depreca = 10
    print("console : " + str(data))
    #検索結果配置
    for i in data:#座標は指定してるから関数化して
        label_moviename = tk.Label(movie_frame, text=i[0],fg='black', bg='papaya whip')
        label_moviename.place(x=10,y=Depreca)

        label_url = tk.Label(movie_frame, text="                URL                ",fg='black', bg='papaya whip')
        label_url.place(x=300,y=Depreca + 20,anchor=tk.NW)
        label_url.bind("<Button-1>", lambda e:jump_to_link(i[1]))

        Depreca = Depreca + 50
    

#
# UI
#

#種類のラベルとボックス
label_type = tk.Label(root, text='検索したいラーメンの種類を選択',fg='black', bg='papaya whip')
label_type.place(x=10, y=50)
ramen = ["醤油", "味噌", "豚骨", "家系", "二郎系", "塩", "蒙古タンメン", "中華そば", "つけ麺"]
select_type = ttk.Combobox(root, value=ramen, height=10, width=20)
select_type.place(x=300, y=50)

#地域のラベルとボックス
label_pre = tk.Label(root, text='探したいお店の都道府県を選択',fg='black', bg='papaya whip')
label_pre.place(x=10, y=100)
pl= ["北海道","青森県","岩手県","宮城県","秋田県","山形県","福島県","茨城県","栃木県","群馬県","埼玉県","千葉県","東京都","神奈川県","新潟県","富山県","石川県","福井県","山梨県","長野県","岐阜県","静岡県","愛知県","三重県","滋賀県","京都府","大阪府","兵庫県","奈良県","和歌山県","鳥取県","島根県","岡山県","広島県","山口県","徳島県","香川県","愛媛県","高知県","福岡県","佐賀県","長崎県","熊本県","大分県","宮崎県","鹿児島県","沖縄県"]
select_pre = ttk.Combobox(root,value=pl, height=10, width=20)
select_pre.place(x=300, y=100)

label_area = tk.Label(root, text='市区町村を入力',fg='black', bg='papaya whip')
label_area.place(x=10, y=150)
txt_area = tk.Entry(width=20,fg='black', bg='white')
txt_area.place(x=300, y=150)

#回のラベルとボックス
label_part = tk.Label(root, text='動画の回で直接指定',fg='black', bg='papaya whip')
label_part.place(x=10, y=200)
txt_part = tk.Entry(width=20,fg='black', bg='white')
txt_part.place(x=300, y=200)

#メッセージと検索ボタン
botton_label = tk.Label(root, text='上記のボックスに入力した情報に合う、SUSURUTVが訪問したラーメンの店舗を検索できます。\n複数ある場合は複数、条件を細かく指定すればその条件に合った店舗が出てきます。',fg='black', bg='papaya whip')
botton_label.place(x=10, y=250)
button1 = tk.Button(root, text = '検索', command = search ,bg = "papaya whip")
button1.place(x=200, y=300)

#表示フレーム
movie_frame = tk.Frame(root, bd=2,bg="#455A64",relief='ridge' ,width=880,height=400)
movie_frame.place(x=10,y=350)

#ウィンドウを更新
root.mainloop()
conn.close