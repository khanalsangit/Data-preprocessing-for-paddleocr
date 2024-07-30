import os
import random
from PIL import ImageFont,ImageDraw,Image
import string
from rotate_img import draw_rotated_text
import math

def create_data(img,x1,x2,y1,y2,n,rotc,intial_data):

    ij = 0
    dir=os.path.dirname(img)+'/'
    
    if 'Gen_Det_Data' in dir:  #### create a directory to save the output
        pass
    else:   
        os.mkdir('Gen_Det_Data') 

    def random_char(y:int) -> None:
        '''
        This function generates a random characters with the combination of letters numbers and symbols
        '''
        characters =  string.digits + "/-"
        return ''.join(random.choice(characters) for x in range(y))


    def get_text_dimensions(text_string, font):
        ascent, descent = font.getmetrics()

        text_width = font.getmask(text_string).getbbox()[2]
        text_height = font.getmask(text_string).getbbox()[3] + descent

        return (text_width, text_height)
   
        '''
        Function that generate data within any location of custom image
        '''
    ij = 0
    for y in range(0,n):
        image= Image.open(img)
        
        font_path = random.choice([
                                ImageFont.truetype('fonts/inkjet/DRKrapkaRound-Regular.ttf',random.randint(22,26))
                                ])  #### to choose a font randomly
        

        for k in range(0,len(intial_data.split('()'))):
            line=intial_data.split('()')[k].split(',')[0]+random_char(random.randint(int(intial_data.split('()')[k].split(',')[1]),int(intial_data.split('()')[k].split(',')[2])))
            
            if k==0:
                xcor=random.randint(x1,x2)
                ycor=random.randint(y1,y2)
            else:
                xcor = random.choice([xcor + random.randint(5,15),xcor - random.randint(5,10)])
                ycor = ycor + random.randint(28,30)
            rot=rotc.split(',')
            
            rot_ang = random.randint(int(rot[0]),int(rot[1]))

            image = draw_rotated_text(image,rot_ang,(xcor,ycor),line,(0,10,0),font = font_path)
        
            width,height = get_text_dimensions(line,font=font_path)
        
        ##### For First Rectangle Bounding box
            # calculate the corner points of the unrotated rectangle
            angle = -rot_ang
            
            top_left = (xcor, ycor-3)
            top_right = (xcor + width+15, ycor-3)
            bottom_left = (xcor, ycor + height+3)
            bottom_right = (xcor + width+15, ycor + height+3)
            # convert the rotation angle to radians
            angle_rad = math.radians(angle)

            # calculate the sin and cosine of the angle
            sin_angle = math.sin(angle_rad)
            cos_angle = math.cos(angle_rad)

            # rotate the corner points around the center point

            if angle_rad < 0:
                rotated_top_left = (
                    xcor +  cos_angle - (top_left[1] - ycor-100) * sin_angle,
                    ycor + sin_angle + (top_left[1] - ycor) * cos_angle
                )
                rotated_top_right = (
                    xcor + (top_right[0] - xcor) * cos_angle - (top_right[1] - ycor) * sin_angle,
                    ycor + (top_right[0] - xcor) * sin_angle + (top_right[1] - ycor) * cos_angle
                )
                rotated_bottom_left = (
                    xcor + cos_angle - (bottom_left[1] - ycor-100) * sin_angle,
                    ycor + sin_angle + (bottom_left[1] - ycor) * cos_angle
                )
                rotated_bottom_right = (
                    xcor + (bottom_right[0] - xcor) * cos_angle - (bottom_right[1] - ycor) * sin_angle,
                    ycor + (bottom_right[0] - xcor) * sin_angle + (bottom_right[1] - ycor) * cos_angle
                )
            else:
                rotated_top_left = (
                    xcor +  cos_angle - (top_left[1] - ycor+100) * sin_angle,
                    ycor + sin_angle + (top_left[1] - ycor) * cos_angle
                )
                rotated_top_right = (
                    xcor + (top_right[0] - xcor) * cos_angle - (top_right[1] - ycor) * sin_angle,
                    ycor + (top_right[0] - xcor) * sin_angle + (top_right[1] - ycor) * cos_angle
                )
                rotated_bottom_left = (
                    xcor + cos_angle - (bottom_left[1] - ycor+100) * sin_angle,
                    ycor + sin_angle + (bottom_left[1] - ycor) * cos_angle
                )
                rotated_bottom_right = (
                    xcor + (bottom_right[0] - xcor) * cos_angle - (bottom_right[1] - ycor) * sin_angle,
                    ycor + (bottom_right[0] - xcor) * sin_angle + (bottom_right[1] - ycor) * cos_angle
                )
            e=0
            #img1.polygon([rotated_top_left, rotated_top_right, rotated_bottom_right, rotated_bottom_left], outline='red',width=3)
            
            final_coord = []

            final_coord.append(rotated_top_left)
            final_coord.append(rotated_top_right)
            final_coord.append(rotated_bottom_right)
            final_coord.append(rotated_bottom_left)
            rect_box = []
            for i in final_coord:
                for j in i:
                    rect_box.append(int(j))

            final_result = str(rect_box).replace('[','').replace(']','') + ', ' + line
            
            with open("Gen_Det_Data/word_{}.txt".format(y),'a') as f:
                f.writelines(final_result)
                f.write('\n')
        image.save("Gen_Det_Data/word_{}.jpg".format(y))
        if ij%10==0:
            print('Count ',ij)
        ij+=1 
#create_data('gorkha_real_data.jpg',105,115,65,70,25,'-5,-2','BN:,10,11()BB:,11,13')  #### 250 == no. of image
    ###### start coord (x,y) function argument while creating data in CLI,

