color_dictionary = {
    "green" : (0,255,0),
    "blue" : (0,0,255),
    "red" : (255,0,0),
    "peach" : (255,190,152),
    "Clay Creek" : (141,125,83),
    "Seal Brown" : (35,22,19)
}
print("The red channel of peach fuzz is " + str(color_dictionary["peach"][0]))
print("The green channel of peach fuzz is " + str(color_dictionary["peach"][1]))
print("The blue channel of peach fuzz is " + str(color_dictionary["peach"][2]))

print("The blue channel of Seal Brown is " + str(color_dictionary["Seal Brown"][2]))
print("The blue channel of Clay Creek is " + str(color_dictionary["Clay Creek"][2]))

print("The red channel of Seal Brown is " + str(color_dictionary["Seal Brown"][0]))
print("The red channel of Clay Creek is " + str(color_dictionary["Clay Creek"][0]))

red = input(print("Enter red: "))
green = input(print("Enter green: "))
blue = input(print("Enter blue: "))

print(f'Thank you your RGB color is ({red}, {green}, {blue})')

print(f'The red channel intensity is: {red}')
print(f'The green channel intensity is: {green}')
print(f'The blue channel intensity is: {blue}')