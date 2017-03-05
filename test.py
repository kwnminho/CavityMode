import numpy as np
from PIL import Image
import urllib, cStringIO
import cv2
from matplotlib import pyplot as plt
#URL="http://128.104.162.15:10000/html/cam.jpg"
#file = cStringIO.StringIO(urllib.urlopen(URL).read())
file='20170303_TEM00.png'
file2='20170303_HG30.png'
img=cv2.imread(file2,0)
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
rows, cols = img.shape
crow,ccol = rows/2 , cols/2

# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((rows,cols,2),np.uint8)
cutoff=10
mask[crow-cutoff:crow+cutoff, ccol-cutoff:ccol+cutoff] = 1

# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

#data=np.array(img)