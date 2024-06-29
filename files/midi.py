import time
import tkinter as tk
import pygame.midi as Midi
import pygame as pg
from Settings import Settings as St

Midi.init()
try:
    if St.b==1:
        m=Midi.Output(0)
##    m.set_instrument(0)
except Exception as e:
    print(e)
    t=tk.Tk()
    tk.Label(t,text="Exception From \n"+__name__+":\n"+str(e)).pack(fill="both")
    t.mainloop()
def b(key=108):
    try:
        m.write_short(0x90,key,127)#0xc9:program change
    except:
        return
def b_(sK=1,eK=108,stime=0.01):
    '''Start key, end key, delay time(second)'''
    if sK<=eK:
        for key in range(sK,eK,1):
            b(key)
            time.sleep(stime)
    else:
        for key in range(sK,eK,-1):
            b(key)
            time.sleep(stime)
if __name__=='__main__':
    print('请配合主程序index使用，请勿单独运行')
    input('Enter...')
