import cv2
import numpy as np
import pygame
import time
import smtplib
from matplotlib import pyplot as plt
cv2.startWindowThread() 
def plt_show(image,title=""):
    if len(image.shape)==3:
        image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    plt.axis("off")
    plt.title(title)
    plt.imshow(image,cmap=plt.cm.Greys_r)
    plt.show()
def image_resize(image,width=None,height=None,inter=cv2.INTER_AREA):
    dim=None
    (h,w)=image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r=height/float(h)
        dim=(int(w*r),height)
    else:
        r=width/float(w)
        dim=(width,int(h*r))
    resized=cv2.resize(image,dim,interpolation=inter)
    return resized
r_image1=cv2.imread("./pothole.jpeg")
r_image2=image_resize(r_image1,width=275,height=180)
plt.title("Pothole Image")
im=r_image2
plt_show(im)
gray1=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
cv2.imwrite("grayimg.jpg",gray1)
imgray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imgray,127,255,0)
contours1,heirarchy1=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
contours2,heirarchy2=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img2=im.copy()
out=cv2.drawContours(img2,contours2,-1,(0,250,0),1)
output=len(contours2)
print(len(contours2))
plt.title("Image pothole drawCountours")
plt.imshow(out)
plt.show()
if output>78:
    print("poyhole")
else:
    print("No pothole")