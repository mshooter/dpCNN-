import os 

path_to_imgs = "../birds/data"
path_to_save = "../birds"

def create_allImageTxt(pathf, paths):
    file = open(os.path.join(paths, "allimages.txt"), "w")
    for dirname in os.listdir(pathf): 
        path_to_dir = os.path.join(pathf, dirname)
        if os.path.isdir(path_to_dir):
            for filename in os.listdir(path_to_dir): 
                #print(os.path.abspath(path_to_dir + "/" + filename), dirname)
                line = "" 
                if dirname=="european goldfinch": 
                    line = os.path.abspath(path_to_dir + "/" + filename) + " "+  str(0)+ "\n" 
                elif dirname=="emu": 
                    line = os.path.abspath(path_to_dir + "/" + filename) + " "+  str(1)+ "\n" 
                elif dirname=="house sparrow": 
                    line = os.path.abspath(path_to_dir + "/" + filename) + " "+  str(2)+ "\n" 
                elif dirname=="peacock": 
                    line = os.path.abspath(path_to_dir + "/" + filename) + " "+  str(3)+ "\n" 
                else: 
                    line = os.path.abspath(path_to_dir + "/" + filename) + " "+  str(4)+ "\n" 
                file.write(line) 

    file.close()

if __name__ == "__main__":

    create_allImageTxt(path_to_imgs, path_to_save)
