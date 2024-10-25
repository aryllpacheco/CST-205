#Aryll Pacheco
#CST205 Lab 9
#9/30/24


#Task 1:
#   Image class in PILLOW begins on line 538

#Task 2:
#   """
#    This class represents an image object.  To create
#    :py:class:`~PIL.Image.Image` objects, use the appropriate factory
#    functions.  There's hardly ever any reason to call the Image constructor
#    directly.

#    * :py:func:`~PIL.Image.open`
#    * :py:func:`~PIL.Image.new`
#    * :py:func:`~PIL.Image.frombytes`
#    """

#Task 3:

from PIL import Image

image = Image.new('RGB', (120,120))

print(dir(image))
# Description of split: split takes the individual bands of the image and splits them into seperate ones
# it then returns a new tuple of the bands of the original image

#Task 4:

class Music:
    '''A simple class to store information about a song'''
    def Song(self, name, artist, genre, length, album):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.length = length
        self.album = album

song1 = Music('Misery Business', 'Paramore', 'Rock', 3.32, 'Riot')
song2 = Music('Dance Dance', 'Fall Out Boy', 'Rock', 3.32, 'From Under the Cork Tree')
