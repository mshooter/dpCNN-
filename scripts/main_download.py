import os 
import time 
import sys
from collect_urls import get_urls 
from downloader import download_imgs

# which species of animals do we want? 
# we want  maximum 5 classes.. 

bird_species = ['peacock', 
                'house sparrow', 
                'european goldfinch', 
                'emu', 
                'blue jay']

total_imgs = int(sys.argv[1]) 
rootdir = 'data'
def download():
    for bird in bird_species: 

        print('Collecting urls for', bird)
        urls = get_urls(bird, total_imgs)

        print('Downloading images for', bird)
        path = os.path.join(rootdir, bird)

        download_imgs(urls, path)

if __name__ == "__main__":
    
    s = time.time() 
    download() 
    print('Download took', round(time.time() - s, 2), 'seconds for', 5*total_imgs, "images")
