filename = 'guest.txt'

guest = input("What's your name? ")

with open(filename, 'w') as file:
    file.write(f"{guest.title()}")
