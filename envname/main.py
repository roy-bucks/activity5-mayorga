import cv2 as cv
import numpy as np 


#validate the image size
def imageSize(img): 

    #not more than this bit size   
    require_size = 10000000
    size = img.size

    if size < require_size: 
        print("The image size is validated")
    else: 
        print('The size of the image is Invalid')


#show the image datatype
def getImageType(img):
    dataType = img.dtype
    print("The image data type is: ", dataType)

    imageSize(img)

#check the dimention of an image 
def dimentionValidation(img):
    size = img.shape

    #set the limit dimentions by pixel
    x = 900
    y = 900

    if size[0] > x and size[1] > y: 
        print("Image dimension is not valid")
    else: 
        print("Image dimension is cleared")

    getImageType(img)

#continue the process
#access the pixel 
def accesspx(img):
   x = int(input("Enter the x coordinate: "))
   y = int(input("Enter the y coordinate: "))
   c = int(input("Enter the attribute color 0 Blue 1 Green 2 Red: "))
   
   px = img.item(x,y,c) #access the pixel
   print("Pixel value: ", px)

   #modify the pixel ising itemset
   img.itemset((x, y, c), 100) #set the pixel
   px = img.item(x,y,c) #access the pixel
   print("After modify: ", px)
   
   dimentionValidation(img)



def loadImage():
    #accept the color image 
    img = cv.imread('./envname/sample.jpeg')

    # img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


    #validate if the image is color or grayscale 
    img_p = img.shape
    if len(img_p) != 3: 
        print("Grayscale image is not allowed")
    else : 
        accesspx(img)



loadImage()
    




