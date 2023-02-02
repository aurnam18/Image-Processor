import numpy as np
from PIL import Image

#this crop uses numpy arrays rather than the pixel array and is more straight forward.
def crop(img, leftCrop,rightCrop, bottomCrop,topCrop):
  imgArr = np.asarray(img)
  imgArr = imgArr[topCrop:-(bottomCrop+1),leftCrop:-(rightCrop+1),:]
  return Image.fromarray(imgArr)

#this grayscale method uses a strict average rather than a weighted average which produces a less good grayscale picture.
def grayscale(img):
  newImg = Image.new('RGB', img.size)
  pixNew = newImg.load()
  pix = img.load()
  width,height = img.size
  for y in range(height):
    for x in range(width):
      avg = (pix[x,y][0]+pix[x,y][1]+pix[x,y][2])//3
      pixNew[x,y]=(avg,avg,avg)
  return newImg