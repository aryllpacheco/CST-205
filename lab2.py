color = (100, 231, 231)

if(color[0] > color[1] and color[0] > color[2]):
    print("The color is reddish")
elif(color[1] > color[0] and color[1] > color[2]):
    print("The color is greenish")
elif(color[0] == color[1]):
    print("The color is a shade of yellow")
elif(color[1] == color[2]):
    print("The color is a shade of cyan")
elif(color[0] == color[2]):
    print("The color is a shade of magenta")
else:
    print("The color is blueish")

# Finished all of the tests for the lab, was able to check between each of the 
# numbers for the colors individually, I might try and use inputs later but it was
# easier for me in the moment to check them the way that I did 