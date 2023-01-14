import os
import shutil
TARGET ="all"

os.chdir(TARGET)

filename = os.listdir(".")

for file_ in filename:
    dirname = file_.split(".")[-1]
    os.makedirs(dirname,exist_ok= True)
    src =file_ 
    dst = os.path.join(dirname,file_)
    shutil.move(src,dst) 
