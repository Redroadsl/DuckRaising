养鸭子游戏    使用Python、Pygame编写。
DuckRaising Game Using Python & Pygame

代码、绘画：Redroadsl，部分图片来自Mojang。
Code & Paint by Redroadsl, Some images are from Mojang.

完成任务将鸭子养大（升级）
Raise the duck and upgrade!

● 操作 CONTROL:
  使用WASD移动鸭子，移动鼠标改变视野范围，触摸鸭子获取信息和任务
  WASD to move the duck, move mouse to view the map, touch the duck to get tips.
  按下N可以暂停或播放音乐，按下M可以切歌（随机）。
  PRESS N to Pause or Continue MUSIC.
  PRESS M to change to Next Song (Randomlized).

● 内容 Content：
 1.找食物。使用WASD移动鸭子，移动鼠标改变视野范围，触摸鸭子获取信息和任务，下同。
    鸭子碰到食物，加分。
    当食物全部被吃掉，进入下一关。
  Find food. WASD to move the duck, move mouse to explore the map, hover on duck to get tips.
    DUCK touches food: + 1 point
    EATEN all the food: Next level.

 2.打南京人（别吃盐水鸭）
    按E向鸭子面前发射信封，南京人碰到并消失。
    南京人全部消失后，进入下一关。
  Battle with Nanjing people (they like eating Nanjing boiled salted duck, yumm...?)
    PRESS E to shoot a letter against NJ people
    ALL cleared: Next level

 3.垃圾分类（现在只列出三种）
    按E拿起垃圾，带着垃圾到对应的垃圾桶上（里），再次按下E扔掉。
    分类正确加分，当全部分类完后，结束。
  Rubbish sorting. (3 types)
    PRESS E to pick up the rubbish, move it to correct bin, then press E again to discard.
    Nothing will happen if you make mistake. When rubbish is cleared, go to the END.

 4.结束（The End）
    按下Esc (Escape)键重新开始，q键结束
    PRESS Esc to back to Home. PRESS Q to quit.

●系统要求：
Windows7及以上，至少2GB运行内存，Intel Core i3及以上，最低核显
  System Requirement:
Above Windows7, RAM up to 2GB, Newer than Intel Core i3, little graphic requirement.

你知道吗：
如果没有游戏视觉体验，可以将窗口最大化或左下角全屏（有可能降低帧数）
用鼠标移动视野的速度与鸭子移动速度相同
如果images.txt丢失，游戏会自动重建并加载图片
#注：两个文件夹不可丢失！！#

requests: 
-pygame*

-random
-os
-sys
-threading
-subprocess