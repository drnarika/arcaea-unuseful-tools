#TODO:随便乱复制别的2.aff

import os
import random
import shutil

path_vaild = []

def path_find(input_path='.'):
    for root, dirs, files in os.walk(input_path, topdown=False):
        for n in dirs:
            n = os.path.join(root,n)
            print(n)
            if os.path.exists(os.path.join(n,'2.aff')) or os.path.exists(os.path.join(n,'3.aff')):
                path_vaild.append(os.path.join(n))
                continue
            print('Skip ', n)
            
def array_random(arr=path_vaild):
    return arr[random.randint(0,len(arr) -1)]
    
def __main__():
    path_aff = input('给定songs文件夹（服务端）')
    path_find(path_aff)
    for r in path_vaild:
        shutil.copy(os.path.join(array_random(path_vaild),'2.aff'),os.path.join(r,'0.aff'))
        shutil.copy(os.path.join(array_random(path_vaild),'2.aff'),os.path.join(r,'1.aff'))
        
__main__()