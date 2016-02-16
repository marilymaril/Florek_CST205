#Marilyn Florek
#Project One: Images

pics = []
redPixelList = []
bluePixelList = []
greenPixelList = []

for counter in range(1,10):  #for loop to grab the images in the designated folder
  imagePath = "/Users/MFlorek/CST205Proj1/bit_photos/" + str(counter) + '.jpg'   #gets the first file path and calls it imagePath
  pics.append(makePicture(imagePath))  #stores the photo from that file path into an array called pics
  show(makePicture(imagePath)) #this was to show it grab the images as it goes

width = getWidth(pics[0]) #these two stores the height and width of the first pic in order to create the dimensions for the final pic
height = getHeight(pics[0])

newPic = makeEmptyPicture(width,height) #makes a new empty picture that is the same size as the first pic in the array

for x in range(0,width): #these loops will sort it and get the color 
  for y in range(0,height): 
    for image in pics: #this for loop gets the pixel data and stores it into an array
      pixel = getPixel(image,x,y)
      r = getRed(pixel)
      g = getGreen(pixel)
      b = getBlue(pixel)
      redPixelList.append(r) #stores the red values in this array
      greenPixelList.append(g) #stores the green values in this array
      bluePixelList.append(b) #stores the blue values in this array
    r = sorted(redPixelList) #these sort the pixels. THIS IS THE MEDIAN FILTER PART.
    g = sorted(greenPixelList)
    b = sorted(bluePixelList)
    color = makeColor(r[4],g[4],b[4]) #gets the median and will be used to set the pixel at that color
    setColor(getPixel(newPic,x,y),color)
    redPixelList = [] #these reset the arrays so that it can keep looping through without using the data from previous pixels
    bluePixelList = [] 
    greenPixelList = []

file =  r"/Users/MFlorek/CST205Proj1/final2.jpg" #designates a name for the final product
writePictureTo(newPic,file)
show(newPic)
