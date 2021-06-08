usernames = ['pzrsa', 'rolo', 'john12', 'admin', 'frankie']

for username in usernames:
    if 'admin' in username:
        print(f"Greetings {username.title()}, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging back in.")