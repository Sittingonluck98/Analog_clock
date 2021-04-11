import cv2
import numpy as np

BG_COLOR = 209

def blank_image(width=1024, height=1024):
    img = np.full((height, width, 1), BG_COLOR, np.uint8)
    return img

def noisy(image):
    row, col, ch = image.shape
    mean = 0
    sigma = 10
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = gauss + image
    return noisy

if __name__ == '__main__':
    img = blank_image()
    cv2.imwrite('out.jpg', noisy(img))