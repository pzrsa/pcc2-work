def make_sandwich(*ingredients):
    print("\nMaking a sandwich with these items:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwich('pepperoni', 'lettuce')
make_sandwich('turkey', 'ham', 'ketchup')
make_sandwich('chicken', 'tomato', 'mustard', 'cucumber')