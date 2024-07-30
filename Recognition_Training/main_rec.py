'''consider
1. img_i.jpg and img_i.txt
2. for json to txt conversion file name should be i.json and so on
'''
import os
import argparse
import gen_data
import image_crop
import aug 
import ast
import AugmentValues
import DetSplit
import Gen_label

parser=argparse.ArgumentParser() #CLI documentation for commandline input
parser.add_argument('--crop_dir=',type=str)
parser.add_argument('--img_dir=',type=str)
parser.add_argument('--count=',type=int)
parser.add_argument('--rot=',type=str )
parser.add_argument('--annot=',type=str)
parser.add_argument('--n=',type=str)
parser.add_argument('--blur=',type=str)
parser.add_argument('--contrast=',type=str)
parser.add_argument('--elastic=',type=str)
parser.add_argument('--percent=',type=int)
args=parser.parse_args()

cr_dir=vars(args)['crop_dir=']
img_dir=vars(args)['img_dir=']
n=vars(args)['n=']
no=vars(args)['count=']
rot=vars(args)['rot=']
annot=vars(args)['annot=']
blvalue=vars(args)['blur=']
cvalue=vars(args)['contrast=']
percent=vars(args)['percent=']
evalue=vars(args)['elastic=']
cr = 'no'
ty = 'no'
dir=img_dir
cropdir = dir+'/Recognition_Cropped'
print(dir)
if not os.path.isdir(cropdir):
    
    os.mkdir(cropdir)
    print('Recognition_Cropped Folder Created')

count=0
n=int(n.replace('x',''))

print("Image cropped Started")
image_crop.img_crop(dir,cropdir,cr,ty)
print("Image cropped Completed")

dir_name = cropdir+'/Recognition_Dataset'
if not os.path.isdir(dir_name):
    os.mkdir(dir_name)
    print('Recognition_Dataset Folder Created')
outdir=dir_name+'/'

blvalue_list=AugmentValues.blur_aug_values(n,blvalue.split('to'))
cvalue_list=AugmentValues.contrast_aug_values(n,cvalue.split('to'))
evalue_list=AugmentValues.elastic_transform(n,evalue.split('to'))

print("Augmentation Started")

k=0
l=0
for filename in os.listdir(cropdir): #Applying Augmentaion
    crop_data = filename
    if '.jpg' in filename:
        os.chdir(cropdir)
        g=open(outdir+'/labels.txt','a')
        
        j=0
        for i in range(0,n):

            if j<n:
                aug.original(filename,outdir,i,l,g) #original
                count+=1
                j+=1
                if count%100==0:
                    print("Number of data created: ",count)
            
            if j<n:
                
                aug.blur(filename,blvalue_list[i],outdir,i,l,g)#bluring
                
                count+=1
                j+=1
                if count%100==0:
                    print("Number of data created: ",count)
              
            if j<n:
                 
                aug.contrast(filename,cvalue_list[i],outdir,i,l,g) #contrasting
                
                j+=1
                count+=1
                if count%100==0:
                    print("Number of data created: ",count)
                
            if j<n:
                
                aug.elastic_transform(filename,evalue_list[i],outdir,i,l,g) #elastic
                
                j+=1
                count+=1
                if count%100==0:
                    print("Number of data created: ",count)
    if '.jpg' in crop_data:
        os.remove(crop_data)
    if '.txt' in crop_data:
        os.remove(crop_data)
    l=l+1  
        
print("Total number of data created: ",count)
print("Augmentation Completed")

print("Train Test Split Started")
DetSplit.split(outdir,percent)#split into train and test
print("Train Test Split Completed")



print('Gen Label Started')
Gen_label.gen_rec_label(outdir+'train_label.txt',outdir+'train_gt.txt') #apply genlabel
Gen_label.gen_rec_label(outdir+'test_label.txt',outdir+'test_gt.txt')
# # os.remove('cropped/train/train.txt')
# # os.remove('cropped/test/test.txt')
# # os.remove(outdir+'labels.txt')
print('Gen label completed')



exit()



print("Train Test Split Started")
DetSplit.split(r"D:/computervision/PaddleOCR/paddleocr_end/Recognition_Training/data/Recognition_Cropped/Recognition_Dataset/",percent)#split into train and test
print("Train Test Split Completed")



print('Gen Label Started')
Gen_label.gen_rec_label('data/Recognition_Cropped/Recognition_Dataset/train_label.txt','data/Recognition_Cropped/Recognition_Dataset/train_gt.txt') #apply genlabel
Gen_label.gen_rec_label('data/Recognition_Cropped/Recognition_Dataset/test_label.txt','data/Recognition_Cropped/Recognition_Dataset/test_gt.txt')
# # os.remove('cropped/train/train.txt')
# # os.remove('cropped/test/test.txt')
# # os.remove(outdir+'labels.txt')
print('Gen label completed')


# print('Gen Label Started')
# Gen_label.gen_rec_label(outdir+'train_label.txt',outdir+'train_gt.txt') #apply genlabel
# Gen_label.gen_rec_label(outdir+'test_label.txt',outdir+'test_gt.txt')
# os.remove(outdir+'train_label.txt')
# os.remove(outdir+'test_label.txt')
# # os.remove(outdir+'labels.txt')
# print('Gen label completed')




