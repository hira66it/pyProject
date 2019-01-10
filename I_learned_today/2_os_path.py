import os

path = r'/Users/Hinyong_Mac/Downloads/L12.pdf'

#1. Join the path
print(os.path.join(r'/Users/Hinyong_Mac/Downloads/','L12.pdf'))

#2. Split the file name from path of folder
print(os.path.split(path))
# 확장자만 따로 떨어트린다.
print(os.path.splitext(path))

#3. Change the working directory
os.chdir(r'/Users/Hinyong_Mac/Downloads/')
print(os.getcwd())

#4-1. show the directory of folder
os.path.dirname(path)
#4-2. show the file name with extension
os.path.basename(path)

#5. show the size of folder
os.path.getsize(path)

#6-1. 존재 하는지
os.path.exists(r'c:\python36\python.exe')
#6-2. dir가 존재하는지
os.path.isdir(r'c:\awfewef')
#6-3. file 존재하는지
os.path.isfile(r'c:\python36\python.exe')

#7. 리눅스와 윈도우 디렉토리 포맷이 섞이거나, 잘못 써졌을때.. 
mixed = r'C;\\\\temp\\\\public/files/index.html'
print(os.path.normpath(mixed))

#8. 절대경로
os.path.abspath(r'temp')
os.path.abspath(r'temp\hello.txt')
os.path.abspath(r'..\temp\hello.txt')