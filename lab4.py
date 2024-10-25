#with open('tarantella.txt', 'r') as my_file:
    #read_data = my_file.readlines.()
#for count, lines in enumerate(read_data):
    #line_count = count
#print(line_count)

#with open('tarantella.txt', 'r') as my_file:
    #read_data = my_file.read()


#for count, words in enumerate(read_data.split()):
    #word_count = count
#print(word_count)

with open('reminders.txt', 'w') as my_file:
    user_input = ' '
    while(user_input != 'n'):
          user_input = input("Enter a reminder: (Enter n to stop): ")
          my_file.write(user_input)
print("Heres your reminders: ")
with open('reminders.txt', 'r') as my_file:
    line_reader = my_file.read()
    print(line_reader)

#Got mostly done with the program, got stuck on printing out the data in new lines but ran out of time