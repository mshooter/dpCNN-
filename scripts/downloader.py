import requests
import os
import sys
import time

def download_imgs(urls, path):
    if not os.path.isdir(path): 
        os.makedirs(path)
    else:
        for i in range(len(urls)):
            image_name = urls[i].split("/")[-1]
            image_path = os.path.join(path, image_name)

            if not os.path.isfile(image_path):  # ignore if already downloaded
                response=requests.get(urls[i], stream=True)

                with open(image_path,'wb') as outfile:
                    outfile.write(response.content)
