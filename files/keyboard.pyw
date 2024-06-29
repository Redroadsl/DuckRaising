import pygame
import tkinter as tk
from pygame.locals import *
import pygame.midi as midi
import winsound
pygame.init()
pygame.display.init()
pygame.display.set_caption('Keyboard',"KKKKKKKey")
screen=pygame.display.set_mode((854,480),0)
midi.init()
m=midi.Output(0)
ins=0
m.set_instrument(ins)
def se(i=0):
    global t
    ins=int(i)
    m.set_instrument(ins)
    t.destroy()
RUN=True
keys={
    K_a:57,
    K_s:58,
    K_d:60,
    K_f:62,
    K_v:64,
    K_SPACE:65,
    K_b:67,
    K_h:69,
    K_j:70,
    K_k:72,
    K_l:74,
    K_7:76,
    K_8:77}
while RUN:
    for event in pygame.event.get():
            if event.type==QUIT:
                RUN=False
            if event.type==KEYDOWN:
                if event.key ==K_BACKSPACE:
                    t=tk.Tk()
                    tk.Label(t,text="Set Instrument<0-127>").pack(fill='x')
                    entry=tk.Entry(t)#,validate="focusout",validatecommand=lambda:test(entry.get())
                    entry.pack(fill='x')
                    entry.insert(0,"0")
                    tk.Button(t,text='[OK]',command=lambda:se(entry.get())).pack(fill='both')
                    t.mainloop()
                elif event.key in keys:
                    m.write_short(0x90,keys.get(event.key),127)
                    #winsound.Beep(keys.get(event.key)*80,500)
m.close()
pygame.quit()
