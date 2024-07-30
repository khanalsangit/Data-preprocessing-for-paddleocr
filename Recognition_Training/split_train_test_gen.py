#import opencv and numpy
import cv2  
import numpy as np
import time
import os
import random
import shutil
path1 = os.getcwd()
from pathlib import Path
dir1 = os.getcwd()
i = 0
##for filename in os.listdir(dir1):
##    if (filename.endswith(".jpg")):
##        if i % 100== 0:
##            print(i)
##        i+= 1
##        new_name = "word_"+str(filename)
##        os.rename(filename, new_name)
        
with open('labels.txt') as f:
    lines = f.readlines()
f = False
ij = 0
print(dir1)
test_lines = []
train_lines = []
for k in range(len(lines)):
    if ij % 100 == 0:
        print(ij)
    ij+= 1
    #print(lines[k])
    file_name = lines[k].split(",")

    
    randnum = random.random()
    if (randnum<0.3):
        shutil.copyfile( os.path.join(dir1,file_name[0]), os.path.join(dir1,"test",file_name[0]))
        test_lines.append(lines[k])
        
        
    else:        
        shutil.copyfile( os.path.join(dir1,file_name[0]), os.path.join(dir1,"train",file_name[0]))
        train_lines.append(lines[k])
        

os.chdir('test')        
with open('test.txt', 'a') as file1:
    for j in range(len(test_lines)):
        
        file1.write(test_lines[j])
file1.close()
os.chdir(dir1)

os.chdir('train')

with open('train.txt', 'a') as file2:
    for k2 in range(len(train_lines)):
        file2.write(train_lines[k2])
file2.close()
os.chdir(dir1)
        
        
        
        
        
    
    

##with open('demo.txt', 'a') as file:
##    for k in range(len(lines)):
##        file.write(lines[k])


