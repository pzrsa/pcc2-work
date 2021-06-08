sandwich_orders = ['chicken mayo', 'bacon and chicken', 'tuna and cucumber']

finished_sandwiches = []

while sandwich_orders:
    for sandwich in sandwich_orders:
        print(f"\nI made your {sandwich.title()} sandwich.")
        made_sandwich = sandwich_orders.pop()
        finished_sandwiches.append(made_sandwich)

print("\nThe following sandwiches were made:")

for sandwich in finished_sandwiches:
    print(f"\n{sandwich.title()} sandwich")