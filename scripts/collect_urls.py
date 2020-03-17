from flickrapi import FlickrAPI
from secret import * 

# required image sizes
IMG_SIZES = ['url_o' ,'url_z', 'url_m', 'url_l', 'url_h']

# returns iterable object 
# collects the images 
# parameters is the tag
def collect_imgs(tag): 
    extras=','.join(IMG_SIZES)
    flickr = FlickrAPI(KEY, SECRET)
    imgs = flickr.walk(   text=tag, 
                            extras=extras, 
                            privacy_filter=1, 
                            per_page=500, 
                            sort='relevance')
    return imgs

# get the URL for a photo depending of sizes 
def get_imgUrl(img):
    for i in range(len(IMG_SIZES)):
        url = img.get(IMG_SIZES[i])
        if url: 
            return url

# collect all images of desired size 
def get_urls(tag, max):
    imgs = collect_imgs(tag)
    counter = 0
    urls=[]
    
    for img in imgs: 
        if counter < max: 
            url = get_imgUrl(img)
            if url: 
                urls.append(url)
                counter += 1
        else: 
            break 
    return urls
