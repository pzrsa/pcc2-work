my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

my_foods.append('burger')
friends_foods.append('jacket potato')

print("\nMy favourite foods are:\n")
for my_food in my_foods:
    print(my_food)

print("\nMy friends favourite foods are:\n")
for friends_food in friends_foods:
    print(friends_food)