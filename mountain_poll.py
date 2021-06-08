responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for users name and response
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb someday? ")

    # Store the responses in dictionary
    responses[name] = response

    # Find out if anyone else will take the poll
    repeat = input("Would you like to let another person take the poll? ('y'/'n') ")
    if repeat == 'n':
        polling_active = False

# Polling completed, showing results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb the {response.title()} mountain.")