# Aryll Pacheco
# CST205, 9/23/24

from PIL import Image
from glob import glob

img_list = []

def load_images(location, type):
    for image in glob(f'{location}/*.{type}'):
        img_list.append(Image.open(image))

#Task 1
def my_median(channel_vals):
    channel_vals.sort()
    length = len(channel_vals)
    median = (length + 1) // 2
    return channel_vals[median+1]


#Task 2 and 3
#load_images('task3_images', 'png')
load_images('task2_images', 'png') 



width, height = img_list[0].size
im1 = Image.new('RGB', (width,height))
#im2 = Image.new('RGB', (width,height))

for x in range(width):
    for y in range(height):
        reds = []
        greens = []
        blues = [] 
        for img in (img_list):
            curr_pixel = img.getpixel((x,y))
            reds.append(curr_pixel[0])
            greens.append(curr_pixel[1])
            blues.append(curr_pixel[2])          
        final_red = my_median(reds)
        final_green = my_median(greens)
        final_blue = my_median(blues)
        final_colors = (final_red, final_green, final_blue)
        im1.putpixel((x,y), final_colors)
    
    

im1.show()  
im1.save('median_filter_task2.png')
#im2.save('median_filter_task3.png')