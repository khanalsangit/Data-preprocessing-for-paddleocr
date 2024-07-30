import random
import os
import shutil

def split(dir,percent):

    f=open(dir+'labels.txt','r')
    l=len(f.readlines())
    f.close()

    if 'Train' not in os.listdir(dir):
        os.makedirs(dir+'Train')

    if 'Test' not in os.listdir(dir):
        os.makedirs(dir+'Test')
    split=int(l*(percent/100))
    train=random.sample(range(l), split)
    test=[]
    for j in range(0,l):
        if j in train:
            pass
        else:
            test.append(j)

    h=open(dir+'/Train/train_label.txt','a')
    for i in range(0,len(train)):
        g=open(dir+'labels.txt','r')
        lines=g.readlines()[train[i]]
        h.writelines(lines.replace('\n',''))
        shutil.copy(dir+lines.split(',')[0],dir+'/Train')
        h.write('\n')
        g.close()
    h.close()

    m=open(dir+'/Test/test_label.txt','a')
    for k in range(0,len(test)):
        g=open(dir+'labels.txt','r')
        liness=g.readlines()[test[k]]
        m.writelines(liness.replace('\n',''))
        shutil.copy(dir+liness.split(',')[0],dir+'/Test')
        m.write('\n')
        g.close()
    for files in os.listdir(dir):
        if '.jpg' in files:
            os.remove(os.path.join(dir,files))
    m.close()
################# To move the train annotation files ###################
    rec_train_path = os.path.join(dir,'Train')
    train_data = os.listdir(rec_train_path)
    for train_file in train_data:
        if '.txt' in train_file:
            src = os.path.join(rec_train_path,train_file)
            shutil.move(src,dir)
################ To move the test annotation files #####################
    rec_test_path = os.path.join(dir,'Test')
    test_data = os.listdir(rec_test_path)
    for test_file in test_data:
        if '.txt' in test_file:
            srcs = os.path.join(rec_test_path,test_file)
            shutil.move(srcs,dir)

# split('C:/Users/User/Desktop/Batch_Code_Updated/One_click_training/Recognition/recognition_working_directory/samples/Recognition_Cropped/Recognition_Dataset/',70)



