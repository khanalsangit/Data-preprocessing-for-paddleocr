import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageOps,ImageDraw
import random
import shutil
from scipy.ndimage.interpolation import map_coordinates
from scipy.ndimage.filters import gaussian_filter
from random import randint,choice

def original(dir,outdir,n,l,g):
    img=dir
    img2=Image.open(img)
    img2.save(outdir+img.replace('.jpg','_'+str(n)+'.jpg'))
    f=open('labels.txt') 
    out_annot=img.replace('.jpg','_'+str(n)+'.jpg')+(',')+f.readlines()[l].split(',')[1].replace('\n','')
    f.close()
    g.writelines(out_annot)
    g.writelines('\n')

def blur(dir,value,outdir,n,l,g):

    img=dir
    img2=Image.open(img)
        
    img2=img2.filter(ImageFilter.GaussianBlur(value / 4))
    img2.save(outdir+img.replace('.jpg','_b_'+str(value)+str(n)+'.jpg'))
    f=open('labels.txt') 
    out_annot=img.replace('.jpg','_b_'+str(value)+str(n)+'.jpg')+(',')+f.readlines()[l].split(',')[1].replace('\n','')
    f.close()
    g.writelines(out_annot)
    g.writelines('\n')
    

def contrast(dir,value,outdir,n,l,g):
    
    img=dir
    img2=Image.open(img)
    
    img2=ImageEnhance.Brightness(img2).enhance(1.0 + value / 100)
    img2.save(outdir+img.replace('.jpg','_c_'+str(value)+str(n)+'.jpg'))
    f=open('labels.txt') 
    out_annot=img.replace('.jpg','_c_'+str(value)+str(n)+'.jpg')+(',')+f.readlines()[l].split(',')[1].replace('\n','')
    f.close()
    g.writelines(out_annot)
    g.writelines('\n')
    

def elastic_transform(dir, value,outdir,n,l,g):
    
    img=dir
    img3=Image.open(img)
    img2 = cv2.cvtColor(np.array(img3), cv2.COLOR_RGB2BGR)
    
    
    sigma=8
    
    random_state=None
    if random_state is None:
        random_state = np.random.RandomState(None)

    shape = img2.shape
    dx = gaussian_filter((random_state.rand(*shape) * 2 - 1), sigma, mode="constant", cval=0) * value
    dy = gaussian_filter((random_state.rand(*shape) * 2 - 1), sigma, mode="constant", cval=0) * value
    dz = np.zeros_like(dx)

    x, y, z = np.meshgrid(np.arange(shape[1]), np.arange(shape[0]), np.arange(shape[2]))
    
    indices = np.reshape(y+dy, (-1, 1)), np.reshape(x+dx, (-1, 1)), np.reshape(z, (-1, 1))

    img2 = map_coordinates(img2, indices, order=1, mode='reflect').reshape(img2.shape)
    img4 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
    img4.save(outdir+img.replace('.jpg','_e_'+str(value)+str(n)+'.jpg'))
    f=open('labels.txt') 
    out_annot=img.replace('.jpg','_e_'+str(value)+str(n)+'.jpg')+(',')+f.readlines()[l].split(',')[1].replace('\n','')
    f.close()
    g.writelines(out_annot)
    g.writelines('\n')
