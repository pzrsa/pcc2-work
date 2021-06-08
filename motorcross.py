bikes = ['ktm', 'honda', 'yamaha', 'kawasaki']
print(f"I currently own a 250cc {bikes[-4].upper()} bike.")
print(f"I used to own a {bikes[-1].title()} before.")
print(f"I would love to own a {bikes[-2].title()} or {bikes[-3].title()} someday.")

print("\n")
# Adding to a list
bikes = []
bikes.append('ktm')
bikes.append('honda')
bikes.append('yamaha')
bikes.append('kawasaki')
bikes.insert(0, 'husqvarna')
print(bikes)

print("\n")
# Deleting from a list with index value
del bikes[3]
print(bikes)

print("\n")
# Temporarily taking out something from list and assigning to a new variable
last_owned = bikes.pop(0)
print(bikes)
print(last_owned)
print(f"The last dirt bike I owned was a {last_owned.title()}.")

print("\n")
# Removing something from list using the value
bikes.remove('honda')
print(bikes)