import random 

    
def blur_aug_values(n,blvalue_list):
    b_values=[]
    for i in range(int(blvalue_list[0]),int(blvalue_list[1])+3,3):
        b_values.append(i)
    random_b_values=[]
    for i in range(0,n):
        random_b_values.append(random.choice(b_values))
    return random_b_values

def contrast_aug_values(n,cvalue_list):
    c_values=[]
    for i in range(int(cvalue_list[0]),int(cvalue_list[1])+10,10):
        c_values.append(i)
    random_c_values=[]
    for i in range(0,n):
        random_c_values.append(random.choice(c_values))
    return random_c_values

def elastic_transform(n,evalue_list):
    e_values=[]
    for i in range(int(evalue_list[0]),int(evalue_list[1])+20,20):
        e_values.append(i)
    random_e_values=[]
    for i in range(0,n):
        random_e_values.append(random.choice(e_values))
    return random_e_values




