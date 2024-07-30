import os 
import yaml
import subprocess
import shutil
def auto_train(master_dir:str,augmented_dir:str,gui_dir_path:str)->None:
    '''
    This function takes the augmented data from the augmentation and set the path of data
    in config file and start training the data for text detection.
     '''
    ################## reading config file (yml) ##############
    config_dir = os.path.join(master_dir,'config.yml')   
    with open(os.path.join(config_dir),'r') as file:
        config_data = yaml.safe_load(file)
    augmented_data = os.listdir(augmented_dir) ##### output of augmentation

    ################# For Trained Model ######################
    trained_model_path = os.path.join(master_dir,'trained_model')
    config_data['Global']['save_model_dir'] = trained_model_path

    ################# For Pretrained Model ###################
    pretrained_model_path = os.path.join(master_dir,'pretrained_model')
    config_data['Global']['pretrained_model'] = pretrained_model_path

    ################# For Output ###########################
    output_path = os.path.join(master_dir,'output')
    output_dir = os.listdir(output_path)
    output_final_path = os.path.join(output_path,output_dir[0])
    config_data['Global']['save_res_path'] = output_final_path
    ################# For Train data ######################
    train_data = augmented_dir + '/' + augmented_data[3]
    train_label = [augmented_dir + '/' + augmented_data[5]]
    config_data['Train']['dataset']['data_dir'] = train_data
    config_data['Train']['dataset']['label_file_list'] = train_label
    ################# For test data #######################
    test_data = augmented_dir + '/' + augmented_data[0] + '/'
    test_label = augmented_dir + '/' + augmented_data[2]
    config_data['Eval']['dataset']['data_dir'] = test_data
    config_data['Eval']['dataset']['label_file_list'] = test_label
    ################# For Infer_Image #####################
    test_img = os.listdir(test_data)
    infer_img = os.path.join(test_data,test_img[0])
    shutil.copy(infer_img,os.path.join(master_dir,'infer_img'))
    config_data['Global']['infer_img'] = infer_img
   
    ################# update the config file ###############
    with open(config_dir,'w') as file:
        yaml.dump(config_data,file)

    ################# Train the data #######################
    train_file_path = os.path.join(gui_dir_path,'tools'+'/'+'train.py')
    config_path = os.path.join(master_dir,'config.yml')
    pretrained_model_path = os.path.join(master_dir,('pretrained_model'+'/'+'best_accuracy'))
    train_command = [
        'python',
        train_file_path,
        '-c',
        config_path,
        '-o',
        'Global.pretrained_model={}'.format(pretrained_model_path)
    ]
    subprocess.run(train_command)
    print("Data Training Completed")
    print("Model Export Started")

    ################# Export the model after training ####################
    export_file_path = os.path.join(gui_dir_path,'tools'+'/'+'export_model.py')
    trained_model_path = os.path.join(master_dir,('trained_model'+'/'+'best_accuracy'))
    inference_model_path = os.path.join(master_dir,('inference_model'))
    eval_command = [
        'python',
        export_file_path,
        '-c',
        config_path,
        '-o',
        'Global.pretrained_model={}'.format(trained_model_path),
        'Global.save_inference_dir={}'.format(inference_model_path)
    ]
    subprocess.run(eval_command)
    print("Model Export completed")
   
   ############### Copying the trained and exported model in the product respective brands ################
    infer_dest_path = os.path.join(gui_dir_path,'Brands')
    infer_dest_data = os.listdir(infer_dest_path)
    final_infer_path = os.path.join(infer_dest_path,(infer_dest_data[0]+'/'+'Detection'))
    print("Final Infer Path",final_infer_path)
    source_dir = os.path.join(master_dir, 'inference_model')
    source_data = os.listdir(source_dir)
    for file in source_data:
        initial_dir = os.path.join(source_dir,file)
        shutil.copy(initial_dir,final_infer_path)
    print("Inference Model copied successfully in brand directory")

# auto_train('C:/Users/User/Desktop/Batch_Code_Updated/One_click_training/Detection/master_directory/','C:/Users/User/Desktop/Batch_Code_Updated/One_click_training/Detection/working_directory/samples/Detection_Dataset','C:/Users/User/Desktop/Batch_Code_Updated/One_click_training/GUI')