import pygame as pg
import threading as _t
def play_music(music_file):
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music_file)
    except pygame.error:
        return False
    pg.mixer.music.play()
    #while pg.mixer.music.get_busy():
        #clock.tick(30)
music_file = r"files/Parasyte - Next to You.mid"
freq = 192000  # audio CD quality_44100
bitsize = -16  # unsigned 16 bit_-16
channels = 2  # 1 is mono, 2 is stereo_2
buffer = 4096  # number of samples (experiment to get right sound)_2048
pg.mixer.init(freq, bitsize, channels, buffer)
pg.mixer.music.set_volume(1.0)
try:
    _t.Thread(target=play_music,args=[music_file]).start()
except KeyboardInterrupt:
    pg.mixer.music.fadeout(1000)
    pg.mixer.music.stop()
    raise SystemExit
