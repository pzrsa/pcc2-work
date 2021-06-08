filename = "guest_book.txt"

while True:
    print("Press 'n' to quit.")
    guest = input("Whats your name? ")
    if guest == 'n':
        break
    else:
        print(f"Welcome, {guest.title()}!")

        with open(filename, 'a') as file:
            file.write(f"{guest.title()}\n")
