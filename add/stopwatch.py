import tkinter as tk
import time
import threading

global roops , c
roops = False
c = 0

'''
時間のはかり方
変数
start : はかり始めた時間
now : はかり始めてから何秒か
h : 何時間
m : 何分間
s : 何秒間

時間 = now - start (秒.コンマ)
m = 時間 / 60
h = 時間 / (60**2)
'''
def __start():
    global roops
    roops = True
    startt = time.time()
    thread = threading.Thread(target = __changehourfont,args = (startt,))
    thread.start()


def __changehourfont(startt):
    global roops,c,stime
    s ,m,h = 0,0,0
    while roops:
        now = time.time()
        stime = (now - startt) + c
        s = stime % 60
        m = int((stime / 60) % 60)
        h = int(stime / (60**2))

        #print(stime,end = "\t")
        #print(m)
        if h > 0:
            text["text"] = f"{h:.0f}:{m:2.0f}:{s:5.2f}"
        elif m > 0:
            text["text"] = f"{m:2.0f}:{s:5.2f}"
        else:
            text["text"] = f"{s:5.2f}"
        time.sleep(0.001)


def __stop():
    global roops,c,stime
    roops = False
    c = stime

def __reset():
    global roops,text,c
    c = 0
    roops = False
    text["text"] = u"0.00"

def stopwatch(f,t):
    global frame,text
    frame = f
    text = t

    #ボタン作成
    btnr = tk.Button(frame,text = u"reset",command = __reset)
    btnr.grid(column = 0,row = 1)
    btns = tk.Button(frame,text = u"start",command = __start)
    btns.grid(column = 1,row = 1)
    btne = tk.Button(frame,text = u"stop",command = __stop)
    btne.grid(column = 2,row = 1)

    #リセットをかける
    __reset()
