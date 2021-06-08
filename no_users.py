usernames = []

if usernames:
    for username in usernames:
        if 'admin' in username:
            print(f"Greetings {username.title()}, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging back in.")
else:
    print("We need to find some users!")