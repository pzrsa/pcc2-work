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

print("\nSadly I can only invite two people to this dinner.")
# Removes the guest from the list and assigns to variable to print with
anne = guests.pop(0)
print(f"\nSorry {anne}, but I can't invite you to the dinner since we're full now.")

elon = guests.pop(2)
print(f"\nSorry {elon}, but I can't invite you to the dinner since we're full now.")

alan = guests.pop(2)
print(f"\nSorry {alan}, but I can't invite you to the dinner since we're full now.")

dwayne = guests.pop(1)
print(f"\nSorry {dwayne}, but I can't invite you to the dinner since we're full now.")

stan = guests.pop(1)
print(f"\nSorry {stan}, but I can't invite you to the dinner since we're full now.")

print(f"\nHello there {guests[0]}, you're still invited.")
print(f"\nHello there {guests[1]}, you're still invited.")

del guests[0]
del guests[0]

print(guests)