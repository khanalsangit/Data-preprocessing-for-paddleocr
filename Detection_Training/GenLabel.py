
import os
import json


def gen_det_label(root_path:str, input_dir:str, out_label:str)->None:
    '''
    This function creates paddle ocr accepted annotation text file
    '''
    with open(out_label, 'w') as out_file:
        for label_file in os.listdir(input_dir):
            img_path = root_path + label_file[3:-4] + ".jpg"
            label = []
            with open(
                    os.path.join(input_dir, label_file), 'r',
                    encoding='utf-8-sig') as f:
                for line in f.readlines():
                    tmp = line.strip("\n\r").replace("\xef\xbb\xbf",
                                                     "").split(',')
                    points = tmp[:8]
                    s = []
                    for i in range(0, len(points), 2):
                        b = points[i:i + 2]
                        
                        b = [int(t) for t in b]
                        s.append(b)
                    result = {"transcription": tmp[8], "points": s}
                    label.append(result)

            out_file.write(img_path + '\t' + json.dumps(
                label, ensure_ascii=False) + '\n')


# import os
# import json

# def gen_det_label(root_path: str, input_dir: str, out_label: str) -> None:
#     '''
#     This function creates paddle ocr accepted annotation text file
#     '''
#     with open(out_label, 'w') as out_file:
#         for label_file in os.listdir(input_dir):
#             img_path = root_path + label_file[3:-4] + ".jpg"
#             label = []
#             with open(os.path.join(input_dir, label_file), 'r', encoding='utf-8-sig') as f:
#                 for line in f.readlines():
#                     tmp = line.strip("\n\r").replace("\xef\xbb\xbf", "").split(',')
                    
                    
#                     # Debug log the processed line
#                     print(f"Processing line: {line.strip()}")
                    
#                     if len(tmp) < 9:
#                         print(f"Skipping line in file {label_file}: insufficient data")
#                         print(tmp)
#                         continue
                    
#                     points = tmp[:8]
#                     s = []
#                     for i in range(0, len(points), 2):
#                         b = points[i:i + 2]
#                         b = [t.strip() for t in b]  # Strip whitespace from points
#                         if all(t.lstrip('-').isdigit() for t in b):  # Handling negative numbers as well
#                             b = [int(t) for t in b]
#                             if len(b) == 2:
#                                 s.append(b)
                    
#                     # Check if s contains exactly 4 points
#                     if len(s) != 4:
#                         print(f"Skipping line in file {label_file}: invalid points data -> {s}")
#                         continue
                    
#                     # Log the valid points array
#                     print(f"Valid points: {s}")
                    
#                     result = {"transcription": tmp[8], "points": s}
#                     label.append(result)

#             out_file.write(img_path + '\t' + json.dumps(label, ensure_ascii=False) + '\n')

# # Example call
# gen_det_label("ing/Detection_Dataset/Test", "ing/Detection_Dataset/TestAnno", "ing/Detection_Dataset/Test_label.txt")
