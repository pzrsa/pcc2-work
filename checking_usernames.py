current_users = ['parsa', 'john', 'steve', 'adam', 'frankie']

new_users = ['parsa', 'john', 'elon', 'paul', 'bill']

for user in new_users:
    if user in current_users:

        print(f"{user} has already been taken. Please enter a new username.")
    else:
        print(f"{user} is available!")