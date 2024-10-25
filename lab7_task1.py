from PIL import Image
im = Image.open('bunny.png')

width, height = im.size

for x in range(width):
    for y in range(height):
        red = int([im.getpixel((x,y))[0]])
        green = int([im.getpixel((x,y))[1]])
        blue = int([im.getpixel((x,y))[2]])
        average_color = (red + green + blue) // 3
        im.putpixel((x,y), average_color)

im.show()

# tried to get the pixels to load from the the image, wasn't liking the 
# values for what I was trying to do. Ended up running out of time at the 
# end of class to try to get it to properly function