import os
from skimage import data,io,transform
from skimage.color import rgba2rgb
import shutil

def path_find(input_path='.'):
    pv = []
    for root, dirs, files in os.walk(input_path, topdown=False):
        for n in dirs:
            n = os.path.join(root,n)
            print(n)
            if os.path.exists(os.path.join(n,'base.jpg')):
                pv.append(os.path.join(n))
                continue
            if os.path.exists(os.path.join(n,'base.png')):
                os.rename(os.path.join(n,'base.png'),os.path.join(n,'base.jpg'))
                pv.append(os.path.join(n))
                continue
            print('Skip ', n)
    return pv
            
def cut_image_1to1(img):
    center = [img.shape[0]//2,img.shape[1]//2]
    min_size = min(img.shape[0],img.shape[1])
    img = img[center[0]-(min_size//2):center[0]+(min_size//2),center[1]-(min_size//2):center[1]+(min_size//2)]
    return img

def resize_512(img):
    return transform.resize(img,(512,512))

def resize_256(img):
    return transform.resize(img,(256,256))

def deal_img(img,size:int):
    if img.shape[0] != img.shape[1]:
            img = cut_image_1to1(img)
            print('Cut image 1:1.')
    if img.shape[0] != size:
        if size == 512:
            img = resize_512(img)
            print('Resize base.jpg to 512.')
        else:
            img = resize_256(img)
            print('Resize base_256.jpg to 256.')
    return img if img.shape[2] == 3 else rgba2rgb(img)

def __main__():
    p = input('输入客户端songs文件夹路径')
    pv = path_find(p)
    piv = []
    for path in pv:
        base_path = os.path.join(path,'base.jpg')
        base_256_path = os.path.join(path,'base_256.jpg')
        img = io.imread(base_path)
        print(path)
        img = deal_img(img,512)
        io.imsave(base_path,img)
        
        if not os.path.exists(base_256_path):
            shutil.copy(base_path,base_256_path)
        img_256 = io.imread(base_256_path)
        img_256 = deal_img(img_256,256)
        io.imsave(base_256_path,img_256)
        print('\n')
    print('Done.')
    
__main__()