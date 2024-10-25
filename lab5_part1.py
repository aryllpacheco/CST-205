from PIL import Image

im = Image.new('RGB', (2,3))
c1 = (54,54,54)
c2 = (204,82,122)
c3 = (71,71,71)
c4 = (232,22,93)
c5 = (54,54,54)
c6 = (168,167,167)

im.putpixel((0,0), (c1))
im.putpixel((0,1), (c2))
im.putpixel((0,2), (c3))
im.putpixel((1,0), (c4))
im.putpixel((1,1), (c5))
im.putpixel((1,2), (c6))

im.save('task1.jpg')
im.show()