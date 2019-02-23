from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2, error
import os

#정상 작동하는 파일
P = os.listdir(os.getcwd())
for files in P:
    if files.endswith('.jpg'):
        imagedata = open(files, 'rb').read()
        id3 = ID3(os.path.splitext(files)[0]+'.mp3')
        id3.add(APIC(3, 'image/jpeg', 3, 'Front cover', imagedata))
        id3.add(TIT2(encoding=3, text=os.path.splitext(files)[0]))
        id3.save(v2_version=3)
        os.remove(files)