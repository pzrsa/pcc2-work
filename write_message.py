filename = 'programming.txt'

# with open(filename, 'w') as file_object:
#     file_object.write('I love programming.\n')
#     file_object.write('I love creating with it.\n')

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love building stuff with Python.\n")
