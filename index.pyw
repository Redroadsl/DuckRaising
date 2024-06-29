#encoding: utf-8
信息='''# DUCK RAISING GAME #
Author: Redroadsl
Bilibili: Redroadsl
QQ: 2020958753
EMAIL: Redroadsl@outlook.com & @qq.com & @163.com
PHONE: 17626021463(own) & 13636103549(father)
Version: 2.0'''
俺是中国人=信息
print(俺是中国人)
class Log():
    def __init__(self,file=None):
        self.file=file
        self.able=0
        self.r=0
    def Open(self,file=r"./latest.log"):
        if self.able:
            self.file=open(file,mode="a",encoding="utf-8")
    def New(self,file=r"./latest.log"):
        if self.able:
            try:
                self.file=open(file,mode='w',encoding='utf-8')
            except:
                self.able=0
    def log(self,info=None,end='\n'):
        if self.able:
            while self.r:
                pass
            try:
                self.file.write("{}{}".format(info,end))
            except:
                print('log error')
        print(info,end=end)
    def Close(self):
        if self.able:
            self.file.close()
    def Reload(self):
        if self.able:
            self.r=1
            self.Close()
            self.Open()
            self.r=0
log=Log()
log.able=1
log.New()
log.log(">>Game Started<<")

###--Initial--###
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']='1'
import sys
#from Fonts import Fonts
#from midi import *
import pygame
import random
import tkinter as tk
from threading import Thread
from pygame.locals import *
#from Images import Images as Img
#from Settings import Settings as St
from subprocess import Popen,PIPE
log.log(">>Initialed<<")

#tk window
t=tk.Tk()
#tk.Label(t,text="Duck Raising Game").pack(fill="both",expand=1)
#t.mainloop()
#Init Pygame
pygame.init()
clock=pygame.time.Clock()

#Main Settings Class
class St(object):
    b=1
    title='DuckRaising'
    icontitle='DuckDuckGo'
    videoDriver=''##windib,directx
    windowWidth=854
    windowHeight=480
    windowSize=(windowWidth,windowHeight)
    normalSize=854,480
    windowPos=50,50
    gamma=[1,1,1]
    gameTick=60
    state=pygame.display.get_active()
    GAME='MENU'
    title1_y=0
    titlep_x=28
    MAX=0
    M=pygame.display.list_modes()
St.state=1
pygame.display.set_caption(St.title,St.icontitle)
screen=pygame.display.set_mode(St.windowSize,RESIZABLE)
##if '-d' in sys.argv[1:]:
##    os.system("python %sindex.pyw" % (sys.argv))
#Init 
#os.environ['SDL_VIDEODRIVER']="%s" % (St.videoDriver)
#os.environ['SDL_VIDEO_WINDOW_POS']="%d,%d" % (St.windowPos)
#pygame.display.init()
#pygame.display.set_gamma(St.gamma[0],St.gamma[1],St.gamma[2])
#pygame.mouse.set_pos((St.windowWidth//2,St.windowHeight//2))
#pygame.mouse.set_visible(True)
#pygame.event.set_grab(True)#limite mouse input
log.log('#----------------#\n#VideoDriver: '+pygame.display.get_driver())
log.log('#VideoModes: '+str(pygame.display.list_modes())+'\n#----------------#\n')

def autolog():
    while St.state:
        log.Reload()
        pygame.time.delay(10000)
logger=Thread(target=autolog,name='AutoLogSaver')
logger.start()

#Exit&Quit Event#
def X():
    screen.fill((102,204,255))
    #b(104)
    pygame.display.flip()
    log.log('\n>>Game Closed<<')
    log.Close()
    St.state=0
    pygame.quit()
    sys.exit()


#VideoResize Event#
def V(func=None):
    if event.type==VIDEORESIZE:
        log.log('>Size< {}'.format(event.size))
        St.windowWidth,St.windowHeight=event.size
        St.windowSize=event.size
        if not St.MAX:
            screen=pygame.display.set_mode(event.size,RESIZABLE)
        if func != None:
            exec(func+'()')


#WindowMaximize Event#
def M(func=None):
    if not St.MAX:
        log.log('>MAX< {}'.format(St.M[0]))
        St.MAX=1
        St.windowPos=0,0
        os.environ['SDL_VIDEO_WINDOW_POS']="%d,%d" % (St.windowPos)
        screen=pygame.display.set_mode(St.M[0],FULLSCREEN|HWSURFACE)
        St.windowWidth,St.windowHeight=St.M[0]
    else:
        log.log('>Normal< {}'.format(St.normalSize))
        St.MAX=0
        St.windowPos=50,50
        os.environ['SDL_VIDEO_WINDOW_POS']="%d,%d" % (St.windowPos)
        screen=pygame.display.set_mode(St.normalSize,RESIZABLE)
        St.windowWidth,St.windowHeight=St.normalSize
        if func != None:
            exec(func+'()')


##--IMAGE CLASS--##
class Img(object):
    def loadin():
        try:
            files=os.listdir(r"./img")
            with open(r"images.txt",r'w',encoding='utf-8') as f:
                for x in files:
                    f.write(x.split('.')[0]+r"=load('"+x+r"')"+'\n')
        except Exception as e:
            log.log(e)
        
    def load(img):
        #log.log('''load image "{}"'''.format(img))
        return pygame.image.load(r"./img/"+img)
    
    try:
        with open(r"./images.txt",'r',encoding='utf-8') as f:
            for line in f.readlines():
                exec(line)
    except Exception as e:
        log.log('{}'.format(e))
        loadin()
        #Popen(r'python ./listimg.py',shell=True,stdout=PIPE)
        t=tk.Tk()
        tk.Label(t,text="Exception From \n"+__name__+":\n"+str(e)+"\nPlease Try Again.").pack(fill="both")
        t.mainloop()
        X()


##transform images
try:
    Img.background=pygame.transform.scale(Img.background,(250,180))
    Img.dirt=pygame.transform.scale(Img.dirt,(30,30))
    Img.i=pygame.transform.scale(Img.i,(50,50))
    Img.max=pygame.transform.scale(Img.max,(30,38))
    Img.duck1=pygame.transform.scale(Img.duck1,(64,64))
    Img.duck1b=pygame.transform.scale(Img.duck1b,(64,64))
    Img.duck2=pygame.transform.scale(Img.duck2,(64,64))
    Img.duck2b=pygame.transform.scale(Img.duck2b,(64,64))
    Img.room1=pygame.transform.scale(Img.room1,(64,64))
    Img.floor1=pygame.transform.scale(Img.floor1,(64,64))
    Img.floor2=pygame.transform.scale(Img.floor2,(64,64))
    Img.ducks=[None,Img.duck1,Img.duck2,Img.duck3]
    Img.ducksb=[None,Img.duck1b,Img.duck2b,Img.duck3b]
    Img.egg=pygame.transform.scale(Img.egg,(32,32))
    Img.bat=pygame.transform.scale(Img.bat,(32,32))
    Img.hui=pygame.transform.scale(Img.hui,(24,24))
    Img.book=pygame.transform.scale(Img.book,(32,32))
    Img.bins=[]
    #Img.bullet=pygame.transform.scale(Img.bullet,(32,32))
    Img.food=pygame.transform.scale(Img.food,(64,64))
except Exception as e:
    Img.loadin()
    log.log(e)
    t=tk.Tk()
    tk.Label(t,text="Exception From \n"+__name__+":\n"+str(e)+"\nPlease Try Again.").pack(fill="both")
    t.mainloop()
    X()


##--Main Font Class--##
class Fonts(object):
    title=pygame.font.Font(r"./files/Mojangles.ttf",140)
    title2=pygame.font.Font(r"./files/Mojangles.ttf",35)
    text=pygame.font.Font(r"./files/Mojangles.ttf",25)
    button=pygame.font.Font(r"./files/Mojangles.ttf",80)
    button2=pygame.font.Font(r"./files/Mojangles.ttf",40)
    

#-Bullet Object-#
class Bullet():
    def __init__(self,to,x,y):
        self.to=to
        self.x=x
        self.y=y
    def d(self):
        screen.blit(Img.bullet,(self.x+game.wx,self.y+game.wy))
        if self.to==0:
            self.x-=1
        elif self.to==1:
            self.x+=1
#-Rubbish Object-#
class Rubbish():
    def __init__(self,img,t,x,y):
        self.img=img
        self.type=t
        self.onduck=0
        self.x=x
        self.y=y
    def d(self):
        if self.onduck:
            self.x=game.duckx
            self.y=game.ducky
            screen.blit(self.img,(game.duckx+16+game.wx,game.ducky+16+game.wy))
        else:
            screen.blit(self.img,(self.x+game.wx,self.y+game.wy))
########################
###--MAIN_GAME_CLASS--###
########################
class Game():
    def __init__(self):
        self.level=1
        self.room=16*self.level
        self.drawlist=[]
        self.wx=0
        self.wy=0
        self.duckx=64
        self.ducky=64
        self.duckspeed=4
        self.duckto=0
        self.duckface=1
        self.foods=0
        self.food=0
        self.bullets=[]
        self.rubbish=[]
    def d_room(self):
        self.drawlist=[]
        for x in range(self.room):
            self.drawlist.append([])
            for y in range(self.room):
                self.drawlist[x].append(0)
        for x in range(self.room):
            self.drawlist[0][x]=1
            self.drawlist[-1][x]=1
            self.drawlist[x][0]=1
            self.drawlist[x][-1]=1
    def d_duck(self):
        return Img.ducks[self.level]
    def movekey(self):
        if event.key==K_d:
            self.duckto=4
            self.duckface=1
        if event.key==K_a:
            self.duckto=3
            self.duckface=0
        if event.key==K_w:
            self.duckto=1
        if event.key==K_s:
            self.duckto=2
    def duckmove(self):
        if self.duckto != 0:
            if self.duckto==1 and self.ducky-self.duckspeed >= 64:
                self.ducky-=self.duckspeed
            if self.duckto==2 and self.ducky+self.duckspeed <= self.room*64-128:
                self.ducky+=self.duckspeed
            if self.duckto==3 and self.duckx-self.duckspeed >= 64:
                self.duckx-=self.duckspeed
            if self.duckto==4 and self.duckx+self.duckspeed <= self.room*64-128:
                self.duckx+=self.duckspeed
    def ducktouch(self):
        if self.level==1:
            showinfo(['How are U?','I am your duck.','Find food for me!','FOOD NOW !!!','move around to','find food(W,A,S,D)'])
            showtask(msgs=['Task: ','1. Find Food {}/{}'.format(game.food-game.foods,game.food),'Then you can upgrade'])
        if self.level==2:
            showinfo(['Let me tell you:','NanJing people like','eating ducks,','Please STOP them!','Press E to attack'])
            showtask(['Task:','1.Tell them not to eat ducks {}/{}'.format(game.food-game.foods,game.food),'''("write" to them)'''])
    def v1_food(self,f=2):
        self.foods=0
        self.food=0
        for x in self.drawlist[1:-1]:
            foodpos=random.randint(1,self.room-2)
            if x[foodpos] == 0:
                x[foodpos]=f
        for x in self.drawlist:
            for y in x:
                if y==f:
                    self.foods+=1
        self.food=self.foods
    def v1_findfood(self):
        for y in range(game.room):#Y
            for x in range(game.room): #X
                if game.drawlist[y][x]==2:
                    if (self.duckx >= x*64 and self.duckx<= (x+1)*64 and self.ducky >= y*64 and self.ducky <= (y+1)*64) or\
                       (self.duckx+64<=(x+1)*64 and self.duckx+64>=x*64 and self.ducky+64>=y*64 and self.ducky+64<=(y+1)*64):
                        showtask(msgs=['Task: ','1. Find Food {}/{}'.format(game.food-game.foods,game.food),'Then you can upgrade'])
                        showmsg(['Got one FOOD !!!','( {}/{} )'.format(game.food-game.foods+1,game.food)])
                        self.foods-=1
                        game.drawlist[y][x]=0
        if self.foods==0:
            self.level+=1
            self.room=32
            self.d_room()
            self.v1_food(f=3)
            self.duckspeed+=1
            self.wx,self.wy=-300,-300
            self.duckx,self.ducky=65,65
    def v2_man(self):
        if self.foods==0:
            self.level+=1
            self.room=9
            self.d_room()
            self.duckspeed=4
            self.wx,self.wy=200,600
            self.duckx,self.ducky=65,65
            self.foods,self.food=3,3
            #self.drawlist[2][-2],self.drawlist[4][-2],self.drawlist[6][-2]=4,4,4
            self.rubbish.append(Rubbish(Img.bat,"YH",64*3,64*5))
            self.rubbish.append(Rubbish(Img.hui,"QT",64*3,64*5))
            self.rubbish.append(Rubbish(Img.book,"KHS",64*3,64*5))
            game.rubbish.append(Rubbish(Img.egg,"CY",64*3,64*5))
    def v2_duckfire(self):
        self.bullets.append(Bullet(self.duckface,self.duckx,self.ducky))
    def v3_rubbish(self):
        if len(self.rubbish)==1:
            self.level==0
            St.GAME='END'
            pygame.event.set_grab(0)
    def v3_take(self):
        if self.rubbish[0].x >= self.duckx and self.rubbish[0].y >= self.ducky and self.rubbish[0].x <=self.duckx+64 and self.rubbish[0].y<=self.ducky+64:
            if not self.rubbish[0].onduck:
                self.rubbish[0].onduck=1
            else:
                self.rubbish[0].onduck=0
                if self.rubbish[0].x>= 64*5:
                    if self.rubbish[0].type=="YH":
                        if self.rubbish[0].y >=64*2 and self.rubbish[0].y<=64*3:
                            self.foods-=1
                            self.rubbish.remove(self.rubbish[0])
                            print("YH++")
                    elif self.rubbish[0].type=="QT":
                        if self.rubbish[0].y >=64*6 and self.rubbish[0].y<=64*7:
                            self.foods-=1
                            self.rubbish.pop(0)
                            print('QT++')
                    elif self.rubbish[0].type=="KHS":
                        if self.rubbish[0].y >=64*4 and self.rubbish[0].y<=64*5:
                            self.foods-=1
                            self.rubbish.pop(0)
                            print('KHS++')
#Display Menu Function#
def start():
    screen.fill((102,min(204,St.title1_y),min(255,St.title1_y)))
    for x in range(0,St.windowWidth,32):
        for y in range(0,random.randint((St.windowHeight-St.title1_y)//2,St.windowHeight-St.title1_y),32):
            screen.blit(Img.dirt,(x,y))
    pygame.draw.rect(screen,(50,50,50),((St.windowWidth//3+4,St.title1_y+St.windowHeight//2+4),(St.windowWidth//3,St.windowHeight//5)))
    pygame.draw.rect(screen,(200,200,200),((St.windowWidth//3,St.title1_y+St.windowHeight//2),(St.windowWidth//3,St.windowHeight//5)))
    screen.blit(Fonts.button.render('Start',0,(0,0,0)),(St.windowWidth//3+22,St.title1_y+St.windowHeight//2+7))
    screen.blit(Fonts.button.render('Start',0,(100,100,100)),(St.windowWidth//3+20,St.title1_y+St.windowHeight//2+5))
    screen.blit(Fonts.title.render(St.title,0,(100,0,0)),(4,St.title1_y+4))
    screen.blit(Fonts.title.render(St.title,0,(200,0,0)),(0,St.title1_y))
    screen.blit(Img.i,(St.windowWidth-50,St.windowHeight-50))
    screen.blit(Img.max,(0,St.windowHeight-38))
    
##MESSAGE_FUNCTIONS----------------------------------------------------------------------------------------------------##
#Show Message Function__delay                                                                                                                           #
def showmsg(msgs=['']):                                                                                                                                         #
    s=screen.blit(Img.background,((St.windowWidth-248)//2-4,(St.windowHeight-166)//2))                                      #
    for x in range(len(msgs)):                                                                                                                                  #
        t=screen.blit(Fonts.text.render(msgs[x],0,(0,0,0)),((St.windowWidth-248)//2,(St.windowHeight-166)//2+x*25)) #
        pygame.display.update(t)                                                                                                                                #
    pygame.display.update(s)                                                                                                                                #
    pygame.time.delay(500)                                                                                                                                  #
#Show information Function                                                                                                                                  #
def showinfo(msgs=['']):                                                                                                                                        #
    screen.blit(Img.background,((St.windowWidth-248)//2-4,(St.windowHeight-166)//2))                                        #
    for x in range(len(msgs)):                                                                                                                                  #
        t=screen.blit(Fonts.text.render(msgs[x],0,(0,0,0)),((St.windowWidth-248)//2,(St.windowHeight-166)//2+x*25))#
#Show Tasks Function                                                                                                                                        #
def showtask(msgs=['Task:']):                                                                                                                               #
    pygame.draw.rect(screen,(50,50,50),((4,St.windowHeight-96),(500,75)))                                                           #
    pygame.draw.rect(screen,(200,200,200),((0,St.windowHeight-100),(500,75)))                                                       #
    for x in range(len(msgs)):                                                                                                                                  #
        t=screen.blit(Fonts.text.render(msgs[x],0,(0,0,0)),(0,St.windowHeight-100+x*25))                                            #
        pygame.display.update(t)                                                                                                                            #
#Show Story Function                                                                                                                                        #
def showstory(msgs=['Story:']):                                                                                                                             #
    pass                                                                                                                                                                #
#--------------------------------------------------------------------------------------------------------------------------------#




###################################################### Orz Orz
##--Display_GAME Function--##                                                       ||# Orz Orz Orz
###################################################### Orz Orz
def play():
    screen.fill((102,204,255))
    for y in range(game.room):
        for x in range(game.room):
            if game.drawlist[y][x]==1:
                screen.blit(Img.room1,(x*64+game.wx,y*64+game.wy))
            elif game.drawlist[y][x]==0:
                screen.blit(Img.floor1,(x*64+game.wx,y*64+game.wy))
            elif game.drawlist[y][x]==2:
                screen.blit(Img.floor1,(x*64+game.wx,y*64+game.wy))
                screen.blit(Img.food,(x*64+game.wx,y*64+game.wy))
            elif game.drawlist[y][x]==3:
                screen.blit(Img.floor2,(x*64+game.wx,y*64+game.wy))
                screen.blit(Img.man,(x*64+game.wx,y*64+game.wy))
                for b in game.bullets:
                    if b.x > x*64 and b.x< (x+1)*64 and b.y> y*64-32 and b.y< (y+1)*64+32:
                        game.bullets.remove(b)
                        showtask(['Task:','1.Tell them not to eat ducks {}/{}'.format(game.food-game.foods,game.food),'''("write" to them)'''])
                        showmsg(["Add ONE ! ","{}/{}".format(game.food-game.foods,game.food)])
                        game.drawlist[y][x]=0
                        game.foods-=1
        #pygame.draw.line(screen,(0,0,0),(x*64+game.wx,0+game.wy),(x*64,game.room*64))
        #pygame.draw.line(screen,(0,0,0),(0+game.wx,x*64+game.wy),(game.room*64,x*64))
    if game.duckface:
        screen.blit(Img.ducks[game.level],(game.duckx+game.wx,game.ducky+game.wy))
    else:
        screen.blit(Img.ducksb[game.level],(game.duckx+game.wx,game.ducky+game.wy))
    if game.level==3:
        screen.blit(Img.bin1,(5*64+game.wx,2*64+game.wy))
        screen.blit(Img.bin2,(5*64+game.wx,4*64+game.wy))
        screen.blit(Img.bin3,(5*64+game.wx,6*64+game.wy))
        game.rubbish[0].d()
    screen.blit(Fonts.title.render('By Redroadsl          To The Best You',0,(102,255,255)),(-200+game.wx,-200+game.wy))
    screen.blit(Fonts.text.render(r'Now playing: "{}"'.format(fi),0,(102,255,255)),(-200+game.wx,-200+game.wy))
    screen.blit(Fonts.title2.render('lvl:{}  RoomSize:{}  {}/{}'.format(game.level,game.room,game.food-game.foods,game.food),0,(63,63,0)),(4,4))
    screen.blit(Fonts.title2.render('lvl:{}  RoomSize:{}  {}/{}'.format(game.level,game.room,game.food-game.foods,game.food),0,(255,255,0)),(2,2))
    
    
pauselist=[' Gamimg Menu  Pause','  -Back to the MENU','  -Settings','  -Back to GAME']
def p():
    pygame.draw.rect(screen,(50,100,100),((St.titlep_x+4,54),(St.windowWidth-64,40)))
    pygame.draw.rect(screen,(200,255,255),((St.titlep_x,50),(St.windowWidth-56,40)))
    for i in range(100,260,54):
        pygame.draw.rect(screen,(50,50,50),((St.titlep_x+4,i+8),(St.windowWidth-64,40)))
        pygame.draw.rect(screen,(200,200,200),((St.titlep_x,i+4),(St.windowWidth-56,40)))
        for x in range(4):
            screen.blit(Fonts.button2.render(pauselist[x],0,(0,0,0)),(St.titlep_x,(x+1)*50+3*x))
    screen.blit(Img.max,(0,St.windowHeight-38))
    pygame.display.flip()

def end():
    screen.fill((0,55,55))
    for d in range(len(Img.ducks)-1):
        screen.blit(Img.ducks[d+1],(70*d,0))
    screen.blit(Img.max,(0,St.windowHeight-38))
    screen.blit(Fonts.title.render("The END",0,(0,255,0)),(70*4,0))
    pygame.display.flip()
fi=''
St.play=1
#Music-play Function
def play_music(music_file):
    global fi
    while St.state:
        if pygame.mixer.music.get_busy():
            pass
            #pygame.time.delay(4000)
        else:
            fi=music_file[random.randint(0,len(music_file)-1)]
            log.log('''#MusicReplay: "{}"#'''.format(fi))
            pygame.mixer.music.load("./files/music/"+fi)
            pygame.mixer.music.play()
def change_music():
    pygame.mixer.music.stop()
    #fi=music_file[random.randint(0,len(music_file)-1)]
    #pygame.mixer.music.load("./files/music/"+fi)
    #pygame.mixer.music.play()
def pause_music():
    if St.play:
        pygame.mixer.music.pause()
        St.play=0
        log.log("#>Paused Music<#")
    else:
        pygame.mixer.music.unpause()
        St.play=1
        log.log("#>Unpaused Music<#")
#Init music
music_file = os.listdir(r"./files/music")
#log.log("#Musics:{}\n#----------------#\n".format(music_file))
freq = 44100  # audio CD quality_44100#192000
bitsize = 16  # unsigned 16 bit_-16
channels = 2  # 1 is mono, 2 is stereo_2
buffer = 2048  # number of samples (experiment to get right sound)_2048


if St.b:
    try:
        pygame.mixer.init(freq, bitsize, channels, buffer)
        pygame.mixer.music.set_volume(1.0)
        Thread(target=play_music,args=[music_file]).start()
    except Exception as e:
        log.log(e)
        #if St.b:
        #    pygame.mixer.music.fadeout(1000)
        #    pygame.mixer.music.stop()

#Menu-->Game effect
def titleleave():
    y=0
    while St.title1_y+y<=St.windowHeight:
        St.title1_y+=y
        start()
        pygame.display.flip()
        y+=1
        clock.tick(60)
    St.GAME='PLAY'
    pygame.event.set_grab(True)

###########################_RRRRRRRRR   DDDDDDDD     _##Redroadsl####Redroadsl##
###--##WHILE_TRUE LOOP##--###_RR          RR   DD            DD  _##Redroadsl####Redroadsl##
###########################_RRRRRRRRR   DD             DD _##Redroadsl####Redroadsl##
while True:    ##Main GameLoop##_RR         RR    DD             DD _##Redroadsl####Redroadsl##
###########################_RR          RR   DD             DD _##Redroadsl####Redroadsl##
####GameMenuEvent##########_RR           RR  DD            DD  _##Redroadsl####Redroadsl##
###########################_RR            RR DDDDDDDD     _##Redroadsl####Redroadsl##
    if St.GAME=='MENU':
        start()
        posX,posY=pygame.mouse.get_pos()
        if posX>=St.windowWidth-50 and posY>=St.windowHeight-50:
                showinfo(['''1.WASD to control''',' the duck','2.move around the',' mouse to view','3.touch the ',' duck to get info',' or tasks'])
        for event in pygame.event.get():
            V()
            if event.type==KEYDOWN:
                if event.key==K_m:
                    change_music()
                if event.key==K_n:
                    pause_music()
            #posX,posY=pygame.mouse.get_pos()
            if event.type==QUIT:
                X()
            if event.type==MOUSEBUTTONDOWN:
                if posX>=0 and posX<=30 and posY>=St.windowHeight-39 and posY<=St.windowHeight:
                    M()
                if posX>=St.windowWidth//3 and posX<= (St.windowWidth//3)*2:
                    if posY>=St.windowHeight//2 and posY<=St.windowHeight//2+St.windowHeight//5:
                        #b(99)
                        y=0
                        t=Thread(target=titleleave)
                        t.start()
                        t.join()
                        game=Game()
                        game.d_room()
                        if game.level==1:
                            game.v1_food()
                        elif game.level==2:
                            game.room=32
                            game.d_room()
                            game.v1_food(f=3)
                            game.duckspeed+=1
                            game.wx,game.wy=-300,-300
                            game.duckx,game.ducky=65,65
                        elif game.level==3:
                            game.room=9
                            game.d_room()
                            game.duckspeed=4
                            game.wx,game.wy=200,600
                            game.duckx,game.ducky=65,65
                            game.foods,game.food=3,3
                            #game.drawlist[2][-2],game.drawlist[4][-2]=4,4
                            game.rubbish.append(Rubbish(Img.bat,"YH",64*3,64*5))
                            game.rubbish.append(Rubbish(Img.hui,"QT",64*3,64*5))
                            game.rubbish.append(Rubbish(Img.book,"KHS",64*3,64*5))
                            game.rubbish.append(Rubbish(Img.egg,"CY",64*3,64*5))
                        pygame.mouse.set_pos((St.windowWidth//2,St.windowHeight//2))
        pygame.display.flip()

    ######################
    ######################
    ###------------------------###
    ###--main game event--###
    ###------------------------###
    ######################
    ######################
    if St.GAME=='PLAY':
        play()
        mx,my=pygame.mouse.get_pos()
        if game.level==1:
            game.v1_findfood()
        elif game.level==2:
            game.v2_man()
            for b in game.bullets:
                b.d()
        if game.level==3:
            game.v3_rubbish()
        
        if 100 < mx < 180:
            game.wx+=1
        elif mx<100  or (game.duckx <32-game.wx):
            game.wx+=game.duckspeed
        if  St.windowWidth-100 > mx > St.windowWidth-180:
            game.wx-=1
        elif mx > St.windowWidth-100 or (game.duckx+64 >St.windowWidth-32-game.wx):
            game.wx-=game.duckspeed
        if 100 < my < 180:
            game.wy+=1
        elif my < 100 or (game.ducky <0-game.wy+32):
            game.wy+=game.duckspeed
        if St.windowHeight-100 > my > St.windowHeight-180:
            game.wy-=1
        elif my > St.windowHeight-100 or (game.ducky+64+game.wy >St.windowHeight-32):
            game.wy-=game.duckspeed
        game.duckmove()
        if mx> game.duckx+game.wx and mx< game.duckx+game.wx+64 and my> game.ducky+game.wy and my<game.ducky+game.wy+64:
            game.ducktouch()
        for event in pygame.event.get():
            V()
            if event.type==QUIT:
                X()
            if event.type==KEYDOWN:
                game.movekey()
                if event.key==K_m:
                    change_music()
                if event.key==K_n:
                    pause_music()
                if event.key==K_ESCAPE:
                    #b()
                    St.GAME='P'
                    pygame.event.set_grab(False)
                    game.duckto=0
                if game.level==2:
                    if event.key==K_e:
                        game.v2_duckfire()
                if game.level==3:
                    if event.key==K_e:
                        game.v3_take()
            if event.type==KEYUP:
                if (event.key==K_w and game.duckto==1) or \
                   (event.key==K_s and game.duckto==2) or \
                   (event.key==K_a and game.duckto==3) or \
                   (event.key==K_d and game.duckto==4):
                    game.duckto=0
        pygame.display.flip()
        if pygame.mouse.get_focused() == False:
            St.GAME='P'
            pygame.event.set_grab(False)
    
    ################
    ##--Pause event--##
    ################
    if St.GAME=='P':
        posX,posY=pygame.mouse.get_pos()
        for event in pygame.event.get():
            V(func='play')
            p()
            if event.type==MOUSEBUTTONDOWN:
                if posX >= 0 and posX <= 30 and posY >= St.windowHeight-39 and posY <= St.windowHeight:
                    M(func='play')
            if event.type==QUIT:
                X()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    #b(99)
                    St.GAME='PLAY'
                    pygame.event.set_grab(True)
                elif event.key==K_q:
                    X()
                if event.key==K_m:
                    change_music()
                if event.key==K_n:
                    pause_music()
    if St.GAME=='END':
        end()
        posX,posY=pygame.mouse.get_pos()
        for event in pygame.event.get():
            V(func='end')
            if event.type==MOUSEBUTTONDOWN:
                if posX >= 0 and posX <= 30 and posY >= St.windowHeight-39 and posY <= St.windowHeight:
                    M(func='end')
            if event.type==QUIT:
                X()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    St.GAME='MENU'
                    St.title1_y=0
                    
                elif event.key==K_q:
                    X()
                if event.key==K_m:
                    change_music()
                if event.key==K_n:
                    pause_music()
    #Game Tick
    clock.tick(St.gameTick)
