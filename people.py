people = { 
    'parsa': {
        'first_name': 'parsa',
        'last_name': 'mesgarha',
        'age': 17,
        'city': 'london',
    },

    'elon': {
        'first_name': 'elon',
        'last_name': 'musk',
        'age': 40,
        'city': 'los angeles',
    },

    'steve': {
        'first_name': 'steve',
        'last_name': 'jobs',
        'age': 50,
        'city': 'cupertino',
    }
}

for person, info in people.items():
    print(f"\nPerson:\t{person.title()}\n")
    print(f"\tFirst Name:\t{info['first_name'].title()}")
    print(f"\tLast Name:\t{info['last_name'].title()}")
    print(f"\tAge:\t{info['age']}")
    print(f"\tCity:\t{info['city'].title()}")
