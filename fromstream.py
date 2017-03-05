import numpy as np
from PIL import Image
import urllib, cStringIO
import cv2
URL="http://128.104.162.15:10000/html/cam.jpg"
file= cStringIO.StringIO(urllib.urlopen(URL).read())
arr = np.asarray(bytearray(file.read()), dtype=np.uint8)
img = cv2.imdecode(arr,-1) # 'load it as it is'

cv2.imshow('lalala',img)
if cv2.waitKey() & 0xff == 27: quit()