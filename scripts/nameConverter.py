import os
#import progressbar 

path_to_data = "../birds/data"

def convert_nameOfImages(path): 
 path_to_dir   for dirname in os.listdir(path):
        path_to_dir = os.path.join(path,dirname)
        if os.path.isdir(path_to_dir):
            for i, filename in enumerate(os.listdir(path_to_dir)):
                os.rename(path_to_dir+"/"+filename, path_to_dir + "/" + str(i).zfill(5) + ".jpg")

if __name__ == "__main__":
    
    print("Converting the names")
    convert_nameOfImages(path_to_data)
