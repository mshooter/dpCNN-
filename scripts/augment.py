import os 
import time 
import sys 
from PIL import Image
from tqdm import tqdm

# TODO: change the argument to the real path and not file/dir names 

path_to_data = "../birds/data"
folder = sys.argv[2]

def create_augmentedimg(path, degree): 
    """ 
    This function will augment the image and save it into another folder
    /Arguments 
    path: the path where to find the original data 
    degree: the angle how much the data needs to rotate 

    How to run the script? 
    python3 augment.py -how many degrees to rotate -which folder -newname  
    example: 
    python3 augment.py 30 fdata min
    """
        for dirname in os.listdir(path): 
            path_to_dir = os.path.join(path, dirname)
            print("folder", dirname)
            if os.path.isdir(path_to_dir):
                for i, filename in enumerate(os.listdir(path_to_dir)): 
                    path_to_file = os.path.join(path_to_dir, filename)
                    if os.path.exists(path_to_file):
                        c_img = Image.open(path_to_file) 
                        c_img = c_img.convert("RGB")
                        r_img = c_img.rotate(degree) 
                        if not os.path.exists("../birds/"+folder+"/"+dirname):
                            os.mkdir("../birds/"+folder+"/"+dirname)
                        else:
                            r_img.save("../birds/"+folder+"/"+dirname+"/"+sys.argv[3]+filename)
                            print("image: ", i)

if __name__ == "__main__": 
    
    print("augmenting the data")
    create_augmentedimg(path_to_data,int(sys.argv[1]))
    print("modifying the data is done")
