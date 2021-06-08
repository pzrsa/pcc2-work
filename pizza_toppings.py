active = True

while active:
    topping = input("What topping would you like to add to your pizza?\nIf you're happy with your pizza, press 'q' to quit. ")
    if 'q' in topping:
        break
    else:
        print(f"I will add {topping} to your pizza!")
        continue