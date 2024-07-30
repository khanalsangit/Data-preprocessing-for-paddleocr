import os
import shutil
dir = os.path.join(os.getcwd(),"Recognition_Cropped")
outdir = os.path.join(dir,'Renamed')
if not os.path.isdir(outdir):
    os.mkdir(outdir)

for filename in os.listdir(dir):
    if '.jpg' and '.txt' in filename:
        shutil.copy((os.path.join(dir,filename)),outdir)
        for data in os.listdir(outdir):
            i = 0
            os.rename(os.path.join(outdir,data),outdir + '/' + str(i)+'.jpg')
            i += 1
