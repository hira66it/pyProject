# This program uses youtube-dl, ffmpeg.

# Import
import os
from subprocess import call
from time import sleep

t=[]
tt=''
P = os.listdir(os.getcwd())

for files in P:
    if files.endswith('.jpg'):
        t.append(files)
for tmp in t:
    tt = tt+''.join(tmp.split('.')[:-1]) +'////'+tmp+'\n'
with open('mp3tag.txt','wt') as f:
    f.write(tt)
    