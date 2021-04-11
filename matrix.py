import cv2

#getting the image to the program
img = cv2.imread('grey_texture.jpg')
print(img.shape)
#cropping the image
height , width = 600 , 600
img_resized = cv2.resize(img,(height,width))
print(img_resized.shape) #checking the resized image

cv2.waitKey(0)


