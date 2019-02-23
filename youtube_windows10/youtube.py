# This program uses youtube-dl, ffmpeg.
# Import
import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2, error
from subprocess import call
from time import sleep


# youtube-dl -U  #업데이트하는법
# http://manpages.ubuntu.com/manpages/trusty/man1/youtube-dl.1.html
#conda install -c conda-forge youtube-dl #update
# 정상 작동하는 파일

def slugify(files):
    import string
    valid_chars = "-_.()%s%s" % (string.ascii_letters, string.digits)
    files = ''.join(c for c in files if c in valid_chars)
    files = files.replace('-', '_')
    return files


def Replace(files):
    files = files.replace('(', '\(')
    files = files.replace(')', '\)')
    print('++' + files)
    return files


# Find Music List
Q = os.listdir(os.getcwd())
'''
for files in Q:
	if files.endswith('.txt'):
		print ("Is it music link list file? \n %s" % files)
		a = 'y'#input('y/n? ')
		if a == 'y':
			templist = open(files,'r')
			break
		elif a =='n':
			continue
'''
templist = open(os.getcwd() + '\\musiclist.txt', 'r')

musiclinklist = [line.strip() for line in templist]

print('Start downloding...')
sleep(0.5)
i = 0
# Download youtube
for link in musiclinklist:
    try:
        i += 1
        print("####################Downloading######################")
        print(i, ' / ', len(musiclinklist))
        print("#####################################################")
        call("youtube-dl --embed-thumbnail --format mp4 " + link, shell=True)
        # call('youtube-dl '+link+' -x --audio-format mp3 --audio-quality 0')
        print('Checking downloded files..')
        # n = len(musiclinklist)
        sleep(5)

        # t = input("Press return to continue")

        # Slugify
        P = os.listdir(os.getcwd())

        for files in P:
            if files.endswith('.mp4'):
                os.rename(files, slugify(files))
                real_name = '.'.join(files.split('.')[:-1]) + '.mp3'
            # elif files.endswith('.jpg'):
            #    os.rename(files, slugify(files))

        print("Wait Slugifying..")
        sleep(1)

        # Convert mp4 to mp3
        P = os.listdir(os.getcwd())

        for files in P:
            if files.endswith('.mp4'):
                print(files)
                # f=Replace(files)
                f = files
                call("ffmpeg -i " + f + " -b:a 320K -vn " + "C:\\Users\\horim\\Documents\\Python" + ".".join(
                    os.path.splitext(f)[:-1]) + '.mp3', shell=True)
                os.remove(files)
                os.rename("C:\\Users\\horim\\Documents\\Python" + '.'.join(os.path.splitext(f)[:-1]) + '.mp3',real_name)
    except:
        print("Error")
        continue
templist.close()

a = input('Done y/n? ')
if a == 'y':
    with open(os.getcwd() + '\\musiclist.txt', 'w') as f:
        f.write('')
    # 정상 작동하는 파일
    P = os.listdir(os.getcwd())
    for files in P:
        if files.endswith('.jpg'):
            imagedata = open(files, 'rb').read()
            id3 = ID3(os.path.splitext(files)[0] + '.mp3')
            id3.add(APIC(3, 'image/jpeg', 3, 'Front cover', imagedata))
            id3.add(TIT2(encoding=3, text=os.path.splitext(files)[0]))
            id3.save(v2_version=3)
            os.remove(files)
print("####################All Done######################")
