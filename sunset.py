from PIL import Image
im = Image.open('bunny.png')
sunset_list = [(p[0], p[1]//2, p[2]) * 2 for p in im.getdata()]
sunset_list = [(p[0], p[1], p[2]//2) * 2 for p in sunset_list]
im.putdata(sunset_list)

im.save('sunset_bunny.png')
im.show()

#Tried getting the values to change by half for the green and the blue 
#values to get a gradient. Didn't like the methods I was trying to do to 
#get the value to change but I ran out of time before I was able to find 
#a working solution