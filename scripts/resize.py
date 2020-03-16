import cv2 
import imutils

pathimg = "../birds/data/emu/00001.jpg"
img = cv2.imread(pathimg, cv2.IMREAD_UNCHANGED)

print('O. Dimensions: ', img.shape)

w = 256

resized_img = imutils.resize(img,width=w, height=w)
print('O. Dimensions: ', resized_img.shape)

cv2.imshow("Resized image", resized_img) 
cv2.waitKey(0)
cv2.destroyAllWindows()
