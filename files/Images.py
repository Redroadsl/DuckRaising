import pygame
from subprocess import Popen,PIPE
import tkinter as tk
class Images(object):
    def load(img):
        return pygame.image.load(r"./img/"+img)
    try:
        with open(r"./images.txt",'r',encoding='utf-8') as f:
            for line in f.readlines():
                exec(line)
    except Exception as e:
        Popen(r'python ./listimg.py',shell=True,stdout=PIPE)
        t=tk.Tk()
        tk.Label(t,text="Exception From \n"+__name__+":\n"+str(e)+"\nPlease Try Again.").pack(fill="both")
        t.mainloop()
if __name__=='__main__':
    print('请配合主程序index使用，请勿单独运行')
    input('Enter...')
