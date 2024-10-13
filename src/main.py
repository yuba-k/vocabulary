import tkinter as tk
import ctypes
import csv
import random

class Aplication():
    def __init__(self,root):
        self.root = root
        self.root.geometry("760x500")
        self.root.title("単語テスト")
        self.root.resizable(False,False)

        self.file_path = "vocabulary.csv"

        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        
        self.window()

    def read(self):
        words = []
        with open(self.file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                words.append(row)
        return words

    def window(self):
        self.vocabulary_frame = tk.Frame(self.root,width=760,height=150)
        self.vocabulary_frame.place(x=0,y=0)

        self.celect_frame = tk.Frame(self.root,width=600,height=240)
        self.celect_frame.place(x=80,y=170)

        self.txt = tk.StringVar()
        self.words = self.read()
        self.ans_num = random.randint(0,len(self.words)-1)#答えの行番号(出題行番号)
        self.txt.set(self.words[self.ans_num][0])
        self.label = tk.Label(self.vocabulary_frame,textvariable=self.txt,font=("",80))
        self.label.place(relheight=1.0,relwidth=1.0)

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


def main():
    root = tk.Tk()
    app = Aplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()