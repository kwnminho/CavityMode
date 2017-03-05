import numpy as np
from PIL import Image
import urllib, cStringIO
import cv2
import time
URL="http://128.104.162.15:10000/html/cam.jpg"
while True:
    file= cStringIO.StringIO(urllib.urlopen(URL).read())
    arr = np.asarray(bytearray(file.read()), dtype=np.uint8)
    img = cv2.imdecode(arr,-1) # 'load it as it is'
    rows, cols, colors = img.shape
    crow, ccol = rows / 2, cols / 2
    f = np.fft.fft2(img[:,:,1])
    fshift = np.fft.fftshift(f)
    cutoff = 20
    fshift[crow - cutoff:crow + cutoff, ccol - cutoff:ccol + cutoff] = 0
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    # create a mask first, center square is 1, remaining all zeros


    cv2.imshow('lalala', img_back)
    cv2.waitKey(200)

