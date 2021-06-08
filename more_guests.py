# List of all the guests invited to dinner
guests = ['Steve Jobs', 'Elon Musk', 'Alan Turing', 'Steve Wozniak']
# Prints out the guests from start to finish with spaces in between
print(f"Hello {guests[0]}, I would like you to attend a dinner that I am hosting tonight.")
print(f"\nHello {guests[1]}, I would like you to attend a dinner that I am hosting tonight.")
print(f"\nHello {guests[2]}, I would like you to attend a dinner that I am hosting tonight.")
print(f"\nHello {guests[3]}, I would like you to attend a dinner that I am hosting tonight.")
print(f"\nUnfortunately {guests[3]} will not be able to attend the dinner.")
# Replaces Steve Wozniak with Stan Lee in the list
guests[3] = 'Stan Lee'

print(f"\nHello {guests[0]}, I would like you to attend a dinner that I am hosting tonight.")
print(f"\nHello {guests[1]}, I would like you to attend a dinner that I am hosting tonight.")
print(f"\nHello {guests[2]}, I would like you to attend a dinner that I am hosting tonight.")
print(f"\nHello {guests[3]}, I would like you to attend a dinner that I am hosting tonight.")
print("\nI managed to find a bigger table due to the huge amount of people attending.")
# Adds AH, DJ, MR to beginning, middle, end of list
guests.insert(0, 'Anne Hathaway')
guests.insert(2, 'Dwayne Johnson')
guests.append('Margot Robbie')

print(f"\nHello {guests[0]}, I would like you to attend a dinner that I am hosting tonight.")
print(f"\nHello {guests[1]}, I would like you to attend a dinner that I am hosting tonight.")
print(f"\nHello {guests[2]}, I would like you to attend a dinner that I am hosting tonight.")
print(f"\nHello {guests[3]}, I would like you to attend a dinner that I am hosting tonight.")
print(f"\nHello {guests[4]}, I would like you to attend a dinner that I am hosting tonight.")
print(f"\nHello {guests[5]}, I would like you to attend a dinner that I am hosting tonight.")
print(f"\nHello {guests[6]}, I would like you to attend a dinner that I am hosting tonight.")