class Music:
    '''A simple class to store information about a song'''
    def __init__(self, name, artist, genre, length, album):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.length = length
        self.album = album

    def __eq__(self, other):
        if(self.name == other.name):
            print("The songs have the same name")
            return True
        elif(self.genre == other.genre):
            print("The songs have the same genre")
            return True
        elif(self.artist == other.artist):
            print("The songs are by the same artist")
            return True
        elif(self.length == other.length):
            print("The songs have the same length")
            return True
        elif(self.album == other.album):
            print("The songs are on the same album")
            return True
        return False


    def __str__(self):
        return f"Song: {self.name}, Artist: {self.artist}, Genre: {self.genre}, Length: {self.length} minutes, Album: {self.album}"


song1 = Music('Misery Business', 'Paramore', 'Rock', 3.32, 'Riot')
song2 = Music('Dance Dance', 'Fall Out Boy', 'Rock', 3.32, 'From Under the Cork Tree')

if song1 == song2:
    print("At least one condition matches")
else:
    print("Not identical")
print(song1)
print(song2)

#MyWidget inherits from QtWidgets.QWidget in the main class file

