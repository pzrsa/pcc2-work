python = 'learning_python.txt'

with open(python) as file_object:
    lines = file_object.read()
    lines = lines.replace('Python', 'C')

print(lines)
