'''
進捗メモ
'''
import tkinter as tk
import threading
import time
from tkinter import ttk
from add.timea import *
import add.stopwatch as sw
from add.stopwatch import *

global root
root = tk.Tk()

roops = True


class ComboboxOption():
    global frame
    def __init__(self):
        super().__init__()
        self.create_widgets()
    def create_widgets(self):
        valuelist = ["Today","StopWatch","Nothing"]
        self.combo = ttk.Combobox(root,values = valuelist)
        self.combo.place(x = 150,y = 150)
        button = ttk.Button(root,text = "OK",command = self.value)
        button.place(x = 300,y = 150)
    def value(self):
        sw.roops = False
        print(self.combo.get())
        print(sw.roops)
        frame.destroy()
        frame_create()
        selectmode(self.combo.get())

def selectmode(mode):
    global framelabel,frame
    if mode == "Today":
        framelabel["text"] = day()

    elif mode == "StopWatch":
        stopwatch(frame,framelabel)
        
    else:
        framelabel["text"] = "Nothing"
    

def changehourfont():
    while roops:
        hourfont["text"] = hour()
        time.sleep(0.1)

class ButtonC:
    global framelabel
    def btns():
        global s
        if s >10:
            s -= 5
        
        hourfont["font"] = (u"Times New Roman",s)
        framelabel["font"] = (u"Times New Roman",s)

    def btnb():
        global s
        if s < 70:
            s += 5
        hourfont["font"] = (u"Times New Roman",s)
        framelabel["font"] = (u"Times New Roman",s)

def on_closing():
    global roops
    roops = False
    sw.roops = False
    root.destroy()

def frame_create():
    global frame
    frame = tk.Frame(root,bd = 5,relief = "ridge")
    frame.grid(column = 1,row = 0)
    global framelabel
    framelabel = tk.Label(frame)
    framelabel["text"] = "Nothing"
    framelabel["font"] = (u"Times New Roman",s)
    framelabel.grid(column = 0,row = 0)

if __name__ == "__main__":
    root.title(u"Current time")
    root.geometry("250x100")

    # 時間
    global s
    s = 50 # フォントサイズ
    hourfont = tk.Label(root)
    hourfont["font"] = (u"Times New Roman",s)
    threadh = threading.Thread(target = changehourfont)
    threadh.start()
    hourfont.grid(column = 0,row = 0)

    #文字サイズ変更ボタン
    btnlabel = tk.Label(root)
    btnlabel["text"] = u"Change Font Size"
    btnlabel.place(x = 20, y = 130)
    btns = tk.Button(root,text = u"Small",command = ButtonC.btns) # 小さくするボタン
    btns.place(x = 20,y = 150)
    btnb = tk.Button(root,text = u"Big",command = ButtonC.btnb) # 大きくするボタン
    btnb.place(x = 80,y = 150)

    frame_create()

    # 選択肢
    combolabel = tk.Label(root)
    combolabel["text"] = u"SelectMode"
    combolabel.place(x = 150,y = 130)
    ComboboxOption()
    
    root.protocol("WM_DELETE_WINDOW",on_closing)
    root.wm_attributes('-topmost',1)
    root.mainloop()
