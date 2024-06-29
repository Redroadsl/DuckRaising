import os
files=os.listdir(r"./img")
with open(r"images.txt",r'w+',encoding='utf-8') as f:
    for x in files:
        f.write(x.split('.')[0]+r"=load('"+x+r"')"+'\n')
