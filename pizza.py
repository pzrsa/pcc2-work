#  # Store information about a pizza being ordered.
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
#     }

# # Summarize the order.
# print(f"You ordered a {pizza['crust']}-crust pizza "
#     "with the following toppings:")

# for topping in pizza['toppings']:
#     print("\t" + topping)



def make_pizza(*toppings):
    '''Print the list of toppings that have been requested.'''
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
