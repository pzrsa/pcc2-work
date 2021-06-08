# name = input("Please enter your name: ")
# print(f"Hello, {name.title()}")

# prompt = "If you tell us your name, we can personalize messages for you."
# prompt += "\nWhat is your name? "

# name = input(prompt)

# print(f"Hello, {name.title()}!")


# def greet_user(name):
#     """Displays a simple greeting"""
#     print(f"Hello, {name.title()}!")

# greet_user('parsa')


def get_formatted_name(first_name, last_name):
    '''Returns the full name formatted'''
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# Infinite Loop
while True:
    print("\nWhat is your name?")
    print("\n(If you want to quit, simply press 'q'.)\n")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    if f_name == 'q' or l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello there, {formatted_name}")