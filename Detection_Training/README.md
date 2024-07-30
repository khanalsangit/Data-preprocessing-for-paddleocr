This repository is about the augmentation of images that can used in object detection and recognition.

python main.py --dir=D:/computervision/PaddleOCR/paddleocr_end/Detection_Training/converted_img/ --n=100x --rotate=-20to20 --blur=2to10 --contrast=-25to25 --elastic=300to400 --rigid=15to35 --recursion_rate=0.3 --percent=70 --master_dir= C:/Users/User/Desktop/Batch_Code_Updated/One_click_training/Detection/master_directory --gui_dir_path=C:/Users/User/Desktop/Batch_Code_Updated/One_click_training/GUI

dir: Input directory of images and after augmetation is completed, a folder named "Detection_Dataset" is created and all the augmented images are stored there.
x is times
rotate should be multiple of 5
blur should be multiple of 3
contrast should be mutiple of 10
/
Note: You can visualize the augmented images and it's bounding box by using https://github.com/crimsontech-io/augumentation-app/blob/master/AugOCR/MainSoftware.py file but before doing that you have to stop the process after augmentation by using the "exit()".


