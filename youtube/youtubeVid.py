# This program uses youtube-dl, ffmpeg.
# Import
import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2, error
from subprocess import call
from time import sleep

#for mac python 3
# youtube-dl -U  #update
# http://manpages.ubuntu.com/manpages/trusty/man1/youtube-dl.1.html

# well working
error_state=[]

templist = open(os.getcwd() + '/musiclist.txt', 'r')

musiclinklist = [line.strip() for line in templist]

print('Start downloding...')
sleep(0.5)
i = 0
# Download youtube
for link in musiclinklist:
    try:
        i += 1
        link = link.split("&")[0]
        print("####################Downloading######################")
        print(i, ' / ', len(musiclinklist))
        print("#####################################################")
        call("youtube-dl -F --embed-thumbnail --format mp4 " + link, shell=True)
        a = (input("which one do you want to download? ex) 137+140\n"))
        call("youtube-dl -f "+a+" --embed-thumbnail " + link, shell=True)
        # call('youtube-dl '+link+' -x --audio-format mp3 --audio-quality 0')
        print('Checking downloded files..')
        sleep(5)
    except:
        print("Error")
        error_state.append(i)
        continue
templist.close()
if error_state:
    print("###############Downloads have been Done#################")
    print("###############Downloads have been Done#################")
    print("###############Downloads have been Done#################")
    print("Error Occured at : ",error_state)
if not error_state:
    print("####################All Done######################")
    print("####################All Done######################")
    print("####################All Done######################")
