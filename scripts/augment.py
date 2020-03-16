import os 
import time 
import sys 
from PIL import Image
from tqdm import tqdm

path_to_data = "../birds/data"
folder = sys.argv[2]

def create_imgList(path, degree): 
        time.sleep(1)
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
                            r_img.save("../birds/"+folder+"/"+dirname+"/"+filename)
                            print("image: ", i)

if __name__ == "__main__": 
    
    print("augmenting the data")
    create_imgList(path_to_data,int(sys.argv[1]))
    print("modifying the data is done")
