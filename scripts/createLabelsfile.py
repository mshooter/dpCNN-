import os

path_to_dir = "../birds/data"
path_to_save = "../birds"

def create_labelsTxt(pathf, paths):
    file = open(os.path.join(paths, "labels.txt"), "w") 
    for dirname in os.listdir(pathf): 
        pathDir = os.path.join(pathf, dirname)
        if os.path.isdir(pathDir):
            line = dirname + "\n"
            file.write(line) 
    file.close()

if __name__ == "__main__":

    create_labelsTxt(path_to_dir, path_to_save)

