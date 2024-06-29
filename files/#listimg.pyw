import os
import tkinter as tk
from tkinter import *
tk=tk.Tk()
Label(tk,text='工具说明：列出所有图片').pack(fill='x')
sb=Scrollbar(tk)
sb.pack(side='right',fill='y')
lb=Listbox(tk,yscrollcommand=sb.set)
files=os.listdir("./img")
with open("images.txt",'w+') as f:
    for x in files:
        f.write(x.split('.')[0]+r"=load('"+x+r"')"+"\n")
        lb.insert(-1,x)
lb.pack(side='left',fill='both')
sb.config(command=lb.yview)
tk.mainloop()
