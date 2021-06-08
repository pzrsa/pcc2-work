sandwich_orders = ['chicken mayo', 'pastrami', 'bacon and chicken', 'pastrami', 'tuna and cucumber', 'pastrami']

finished_sandwiches = []

print("Unfortunately, the deli has ran out of pastrami!")

while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    for sandwich in sandwich_orders:
        print(f"\nI made your {sandwich.title()} sandwich.")
        made_sandwich = sandwich_orders.pop()
        finished_sandwiches.append(made_sandwich)

print("\nThe following sandwiches were made:")

for sandwich in finished_sandwiches:
    print(f"\n{sandwich.title()} sandwich")