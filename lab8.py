from PIL import Image 
# im = Image.new('RGB', (640,480), 'lavender')
#im.show()

# def copy_image(your_image):
#    my_src = Image.open(your_image)
#    w,h = my_src.width, my_src.height
#    my_trgt = Image.new('RGB', (w,h))

#    target_x = 0
#    for source_x in range(w):
#        target_y = 0
#        for source_y in range(h):
#            p = my_src.getpixel((source_x, source_y))
#            my_trgt.putpixel((target_x, target_y), p)
#            target_y += 1
#        target_x += 1

#    my_trgt.show()
my_src = Image.open('BassClarinet.png')

new_w, new_h = my_src.width + 200, my_src.height + 200
my_trgt = Image.new('RGB', (new_w, new_h), 'lavender')

target_x = 100
for source_x in range(my_src.width):
   target_y = 100
   for source_y in range(my_src.height):
       pixel = my_src.getpixel((source_x, source_y))
       my_trgt.putpixel((target_x, target_y), pixel)
       target_y += 1
   target_x += 1

my_trgt.show()


# copy_image('/cst205/BassClarinet.png')

# Was working on get one image to be copied on to the background before attempting to 
# add all three to the background. Couldn't get the one image to add to the background 
# so I tried troublshooting that before I ended up running out of time at the end of class.
