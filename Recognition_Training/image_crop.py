import cv2
import numpy as np
import os
import time
import random
import shutil

########## Cropped or ROI of an image
def img_crop(input_dir,out_dir,ty,cr):
    
    if ty=='no' and cr=='no':
        in_list=os.listdir(input_dir)
        dir_list=in_list

    elif cr=='no' and ty!='no':
        for filename in os.listdir(ty):
            filepath = os.path.join(ty, filename)
            if os.path.isfile(filepath):
                shutil.move(filepath, input_dir)
                # os.makedirs(input_dir+'/CroppedFile')
                # shutil.copy(input_dir,input_dir+'/CroppedFile')
    elif cr!='no' and ty=='no':
        
        f=open(cr+'/labels.txt')
        l=len(f.readlines())
        f.close()
        for i in range(0,l):
            
            g=open(cr+'/labels.txt')
            txt_name=g.readlines()[i].replace('\n','').split(',')[0].replace('.jpg','.txt').replace('.jpg','.txt')
            g.close()
            
            g=open(cr+'/labels.txt')
            h=open(cr+'/'+txt_name,'a')
            h.writelines('0,0,0,0,0,0,0,0,'+g.readlines()[i].replace('\n','').split(',')[1].replace('"',''))
            h.writelines('\n')
            h.close()
            g.close()
        os.remove(cr+'/labels.txt')
        for filename in os.listdir(cr):
            filepath = os.path.join(cr, filename)
            if os.path.isfile(filepath):
                shutil.move(filepath, input_dir)
                # os.makedirs(input_dir+'/CroppedFile')
                # shutil.copy(input_dir,input_dir+'/CroppedFile')
    elif cr!='no' and ty!='no':
        for filename in os.listdir(ty):
            filepath = os.path.join(ty, filename)
            if os.path.isfile(filepath):
                shutil.move(filepath, input_dir)
        
        f=open(cr+'/labels.txt')
        l=len(f.readlines())
        f.close()
        for i in range(0,l):
            
            g=open(cr+'/labels.txt')
            txt_name=g.readlines()[i].replace('\n','').split(',')[0].replace('.jpg','.txt').replace('.jpg','.txt')
            g.close()
            
            g=open(cr+'/labels.txt')
            h=open(cr+'/'+txt_name,'a')
            h.writelines('0,0,0,0,0,0,0,0,'+g.readlines()[i].replace('\n','').split(',')[1].replace('"',''))
            h.writelines('\n')
            h.close()
            g.close()
        os.remove(cr+'/labels.txt')
        for filename in os.listdir(cr):
            filepath = os.path.join(cr, filename)
            if os.path.isfile(filepath):
                shutil.copy(filepath, input_dir)
    else:
        pass
    a=0

    dir_list=os.listdir(input_dir)
    
    dir_list_shuf = random.sample(dir_list, len(dir_list))

    
    for filename in dir_list_shuf:
        img_path = os.path.join(input_dir, filename)
        
        global res
        u=0
        if os.path.isfile(img_path): 
            
            if '.jpg' in img_path:
                txt=img_path.replace('.jpg','.txt')
        
                g=open(txt,'r')
                le=len(g.readlines())
                g.close()
                img_name = []
                for i in range(0,le):
                    img=cv2.imread(img_path) 
                    mask = np.zeros(img.shape[0:2], dtype=np.uint8)
                    
                    f = open(txt,'r')
                    a=int(f.readlines()[i].split(',')[0])
                    f.close()
                    f=open(txt,'r')
                    b=int(f.readlines()[i].split(',')[1])
                    f.close()
                    f=open(txt,'r')
                    c=int(f.readlines()[i].split(',')[2])
                    f.close()
                    f=open(txt,'r')
                    d=int(f.readlines()[i].split(',')[3])
                    f.close()
                    f=open(txt,'r')
                    e=int(f.readlines()[i].split(',')[4])
                    f.close()
                    f=open(txt,'r')
                    g=int(f.readlines()[i].split(',')[5])
                    f.close()
                    f=open(txt,'r')
                    h=int(f.readlines()[i].split(',')[6])
                    f.close()
                    f=open(txt,'r')
                    j=int(f.readlines()[i].split(',')[7])
                    f.close()
                    points = np.array([[np.abs(a),np.abs(b)],[np.abs(c),np.abs(d)],[np.abs(e),np.abs(g)],[np.abs(h),np.abs(j)]])
                    if a==0 and b==0 and c==0 and d==0 and e==0 and g==0 and h==0 and j==0:
                        file_name = str(time.time())+'.jpg'
                        time.sleep(0.1)
                        img_name.append(file_name)
                        cv2.imwrite(out_dir+'/' + file_name,img)
                    else:
                        cv2.drawContours(mask, [points], -1, (255, 255, 255), -1, cv2.LINE_AA)
                        res = cv2.bitwise_and(img,img,mask = mask)
                        rect = cv2.boundingRect(points)
                        cropped = res[rect[1]: rect[1] + rect[3], rect[0]: rect[0] + rect[2]]
                    
                        file_name = str(time.time())+'.jpg'
                        time.sleep(0.1)
                        img_name.append(file_name)
                        cv2.imwrite(out_dir+'/' + file_name,cropped)
    
                    h=open(txt,'r')
                    
                    outtxt=(file_name+','+'"'+h.readlines()[i].split(',')[-1].replace('\n','')+'"')
                    outtxt=outtxt.replace('" ','"')
                
                    h.close()
                    with open(out_dir+'/labels.txt','a') as file:
                        file.writelines(outtxt)
                        file.writelines('\n')
        
                    file.close()
            u+=1
            if u%100==0:
                print('Number of cropped image Created: ',u)
            else:
                pass
             
                

                 

                
                