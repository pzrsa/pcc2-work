from json import dump, load

username = input("whats your name?")

file = 'username.json'
with open(file, 'w') as f:
    dump(username, f)
    print(f"we'll remember you when you come back {username}.")
