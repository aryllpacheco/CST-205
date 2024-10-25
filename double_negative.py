from PIL import Image
im = Image.open('bunny.png')
negative_list = [(255-p[0], 255-p[1], 255-p[2]) * 2 for p in im.getdata()]
negative_list = [(255-p[0], 255-p[1], 255-p[2]) for p in negative_list]
im.putdata(negative_list)

im.save('doublenegative_bunny.png')
im.show()

#when we negated the negative we got the positve and or the original 
#version of the image