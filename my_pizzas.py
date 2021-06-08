my_pizzas = ['pepperoni pizza', 'mozzarella pizza', 'beef pizza']
friend_pizzas = my_pizzas[:]

my_pizzas.append('chicken tikka pizza')
friend_pizzas.append('tandoori hot pizza')

print("\nMy favourite pizzas are:\n")
for my_pizza in my_pizzas:
    print(my_pizza)

print("\nMy friends favourite pizzas are:\n")
for friend_pizza in friend_pizzas:
    print(friend_pizza)