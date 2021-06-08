# Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
# The blank slice copies the entire list and assigns to friend_foods
friend_foods = my_foods[:]

my_foods.append('lasagne')
friend_foods.append('burger')

# This proves that they are two different lists now
print("My favourite foods are:")
print(my_foods)
print("\nMy friends favourite foods are:")
print(friend_foods)