import tkinter as tk
import ctypes
import csv
import random
from tkinter import messagebox
import sys
import os
from absolute_path import resource_path

class Aplication():
    def __init__(self,root):
        self.root = root
        self.root.geometry("760x500")
        self.root.title("単語テスト")
        self.root.resizable(False,False)

        self.file_path = resource_path("vocabulary.csv")

        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        
        self.window()

    def read(self):
        words = []
        with open(self.file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                words.append(row)
        return words

    def cheaker(self,num):
        self.buttons[num]["bg"]="gray"
        for i in range(4):
            self.buttons[i]["state"] = tk.DISABLED
        if self.words[self.ans_num][2] == self.choices[num]:
            self.label["bg"] = "red"
            self.txt.set("正解")
        else:
            self.label["bg"] = "blue"
            self.buttons[self.choices.index(self.words[self.ans_num][2])]["bg"] = "red"#正解の選択肢を赤色に変更
            self.txt.set("不正解")
        next_frame = tk.Frame(width=760,height=80)
        next_frame.place(x=0,y=420)
        tk.Button(next_frame,text="NEXT",bg="gold",font=("",40),command=self.window).place(relheight=1.0,relwidth=1.0)

    def finish(self):
        ret = messagebox.askyesno('確認', 'ウィンドウを閉じますか？')
        if ret:
            self.root.destroy()

    def window(self):
        #各フレーム設定
        self.vocabulary_frame = tk.Frame(self.root,width=760,height=150)
        self.vocabulary_frame.place(x=0,y=0)

        self.celect_frame = tk.Frame(self.root,width=600,height=240)
        self.celect_frame.place(x=80,y=170)

        #メニューバー
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        # menubarを親として設定メニューを作成と表示
        setting_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='設定', menu=setting_menu)

        # menubarを親としてヘルプメニューを作成と表示
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='ヘルプ', menu=help_menu)

        # 設定メニューにプルダウンメニューを追加
        setting_menu.add_command(label='環境設定')
        setting_menu.add_command(label='終了',command=self.finish)

        # ヘルプメニューにプルダウンメニューを追加
        help_menu.add_command(label='FAQ')

        #英単語表示
        self.txt = tk.StringVar()
        self.words = self.read()
        self.ans_num = random.randint(0,len(self.words)-1)#答えの行番号(出題行番号)
        self.txt.set(self.words[self.ans_num][0])
        self.label = tk.Label(self.vocabulary_frame,textvariable=self.txt,font=("",80))
        self.label.place(relheight=1.0,relwidth=1.0)

        #答え、選択肢
        self.choices = []
        for i in range(3):
            self.choices.append(self.words[random.randint(0,len(self.words)-1)][2])
        self.choices.append(self.words[self.ans_num][2])
        random.shuffle(self.choices)
        self.buttons = []
        for i in range(4):
            button = tk.Button(self.celect_frame,text=self.choices[i],font=("Helvetica",30),command=lambda choices = i : self.cheaker(choices))
            button.place(x=0,y=60*i,relheight=0.25,relwidth=1.0)
            self.buttons.append(button)

def main():
    root = tk.Tk()
    app = Aplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()