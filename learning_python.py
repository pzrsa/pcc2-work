python = 'learning_python.txt'

with open(python) as file_object:
    lines = file_object.readlines()


for _ in range(3):
    print("")
    for line in lines:
        print(line.strip())
