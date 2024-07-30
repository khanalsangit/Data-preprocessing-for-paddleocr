
import os
import random

def change_name(dir:str)->None:
    '''
    This function changes and shuffles name of images and annotation into acceptable format i.e img_1.jpg, img_2.jpg, etc
    and gt_img_1.txt. gt_img_2.txt, etc
    '''   
    i=1
    j=1

    for filename in os.listdir(dir):
        os.chdir(dir)
        if 'jpg' in filename:
            os.rename(filename,str(i)+'.jpg')
            i+=1

        if 'txt' in filename:
            os.rename(filename,str(j)+'.txt')
            j+=1

    img=[]
    for filename in os.listdir(dir):
        os.chdir(dir)
        if 'jpg' in filename:
            img.append(filename)
    print(filename)
    u=(random.sample(range(1,len(img)+1),len(img)))
    for k in range(1,len(u)+1):
        
        os.rename(str(k)+'.jpg','img_'+str(u[k-1])+'.jpg')
        os.rename(str(k)+'.txt','gt_img_'+str(u[k-1])+'.txt')
    
    
    


        
