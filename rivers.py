rivers = {
    'thames': 'england',
    'nile': 'egypt',
    'new york': 'america',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")