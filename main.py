from PIL import Image

#Purpose: Crop a photo
#parameters: 
  #img - image to crop
  #leftCrop,rightCrop,bottomCrop,topCrop - number of pixels to remove from relative side
#returns: a new image that is cropped
def crop(img, leftCrop, rightCrop, bottomCrop,topCrop):
  pix = img.load() #loads in pixel array
  width,height = img.size #get size of image
  newImg = Image.new('RGB', (width-rightCrop-leftCrop,height-bottomCrop-topCrop)) #create a new image with cropped dimensions
  pixNew = newImg.load() #loads pixel array from newImg (all black)
  for y in range(height-bottomCrop-topCrop):
    for x in range(width-rightCrop-leftCrop):
        pixNew[x,y] = pix[x+leftCrop,y+topCrop] #loops through pixels and copies img into newImg
  return newImg

#Purpose: rotates a photo clockwise by 90 degrees
#parameters: img - image to rotate
#returns: a new image that is rotated
def rotateRight(img):
  pix = img.load() #loads in pixel array
  width,height = img.size #get size of image
  newImg = Image.new('RGB', (height,width)) #create a new image with rotated dimensions
  pixNew = newImg.load() #loads pixel array from newImg (all black)
  for y in range(height):
    for x in range(width):
      pixNew[-y,x] = pix[x,y] #loop through pixels and copy into rotated locations
  return newImg

#Purpose: rotates a photo counterclockwise by 90 degrees
#parameters: img - image to rotate
#returns: a new image that is rotated
def rotateLeft(img):
  pix = img.load() #loads in pixel array
  width,height = img.size #get size of image
  newImg = Image.new('RGB', (height,width)) #create a new image with rotated dimensions
  pixNew = newImg.load() #loads pixel array from newImg (all black)
  for y in range(height):
    for x in range(width):
      pixNew[y,-x] = pix[x,y] #loop through pixels and copy into rotated locations
  return newImg

#Purpose: flip a photo horizontally
#parameters: img - image to reflect
#returns: a new image that is reflected
def horizontalFlip(img):
  pix = img.load()
  newImg = Image.new('RGB', img.size)
  pixNew = newImg.load()
  width,height = img.size
  for y in range(height):
    for x in range(width):
      pixNew[x,y] = pix[-x,y]
  return newImg

#Purpose: flip a photo vertically
#parameters: img - image to reflect
#returns: a new image that is reflected
def verticalFlip(img):
  pix = img.load()
  newImg = Image.new('RGB', img.size)
  pixNew = newImg.load()
  width,height = img.size
  for y in range(height):
    for x in range(width):
      pixNew[x,y] = pix[x,-y]
  return newImg

#Purpose: perform greenscreen editing
#parameters: 
  #img1 - image with greenscreen components to be replaced
  #img2 - image to replace the greenscreen
  #green - color of greenscreen
#returns: a new image where the green in img1 is replaced with img2
def greenScreen(img1, img2, green):
  img2 = img2.resize(img1.size)
  newImg = Image.new('RGB', img1.size)
  pix1 =img1.load()
  pix2 = img2.load()
  pixNew = newImg.load()
  width,height = img1.size
  for y in range(height):
    for x in range(width):
      if abs(pix1[x,y][1]-green[1])<100 and abs(pix1[x,y][0]-green[0])<100 and abs(pix1[x,y][2]-green[2])<100:
        pixNew[x,y]=pix2[x,y]
      else:
        pixNew[x,y]=pix1[x,y]
  return newImg

#Purpose: convert a photo to grayscale (ie black & white)
#parameters: img - image to convert to grayscale
#returns: a new image that is in black and white
def grayscale(img):
  newImg = Image.new('RGB', img.size)
  pixNew = newImg.load()
  pix = img.load()
  width,height = img.size
  for y in range(height):
    for x in range(width):
      avg = int(pix[x,y][0]*.3+pix[x,y][1]*.59+pix[x,y][2]*.11) #formula 
      pixNew[x,y]=(avg,avg,avg)
  return newImg

def main():
  #open and crop the cupcake image
  cupcakeImg = Image.open("cupcake.jpg")
  croppedImg = crop(cupcakeImg,60,50,30,50)
  croppedImg.save("cupcakeCropped.jpg")
   
  #make cupcake image grayscale 
  grayImg = grayscale(cupcakeImg)
  grayImg.save("cupcakeGrayscale.jpg")
    
  #rotate cupcake
  rotateImg = rotateRight(cupcakeImg)
  rotateImg.save("cupcakeRotated.jpg")

  #rotate cupcake
  rotateImg = rotateLeft(cupcakeImg)
  rotateImg.save("cupcakeRotatedLeft.jpg")

  # open and replace the green screen image
  greenImg = Image.open("greenscreen.jpg")
  yosemiteImg = Image.open("yosemite1.jpg")
  greenImgreplaced = greenScreen(greenImg,yosemiteImg,(0,255,0))
  greenImgreplaced.save("greenscreenreplaced.jpg") 

  #flip yosemite
  flippedImg = horizontalFlip(yosemiteImg)
  flippedImg.save("yosemiteFlipped.jpg")

  #flip yosemite
  flippedImg = verticalFlip(yosemiteImg)
  flippedImg.save("yosemiteFlippedVert.jpg")

  #stop sign flipped and change color
  stopImg = Image.open("stopsign.jpg")
  blueImg = Image.new("RGB",stopImg.size,(8,37,66))
  stopChangedImg =greenScreen(stopImg,blueImg,(255,0,0))
  stopChangedImg.save("newStopSign.jpg")
main()
