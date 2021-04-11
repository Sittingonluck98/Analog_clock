import cv2  # computer vision
import numpy as np
from analog_values import colors, get_ticks , get_date, draw_time
from matrix import img_resized

image = np.zeros((600,600,3),dtype=np.uint8)
image[:]=img_resized

hours_init, hours_dest = get_ticks()
day, date = get_date()

for i in range(len(hours_init)):
    if i%5 == 0:
        cv2.line(image,hours_init[i], hours_dest[i], colors['black'],3)
    else:
        cv2.circle(image,hours_init[i],5, colors['gray'],-1 )

cv2.rectangle(image, (190,170), (430,265),colors['white'],-1)
cv2.putText(image, day ,(250,210),1,2,colors['magneta'],1, cv2.LINE_AA)
cv2.putText(image, date ,(210,250),1,2,colors['magneta'],1, cv2.LINE_AA)


while True:
    image_original = image.copy()

    clock_face = draw_time(image_original)

    cv2.imshow('clock',image_original)
    if cv2.waitKey(1) & 0xFF==27:
        break

cv2.destroyWindow()