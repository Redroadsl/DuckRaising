import pygame
class Settings(object):
    b=0
    title='DuckRaising'
    icontitle='DuckDuckGo'
    videoDriver=''##windib,directx
    windowWidth=854
    windowHeight=480
    windowSize=(windowWidth,windowHeight)
    windowPos=50,50
    gamma=[1,1,1]
    gameTick=60
    state=pygame.display.get_active()
    GAME='MENU'
    title1_y=0
    titlep_x=28
if __name__=='__main__':
    print('请配合主程序index使用，请勿单独运行')
    input('Enter...')
