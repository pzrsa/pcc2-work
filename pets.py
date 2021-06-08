# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)


def describe_pet(pet_name, animal_type='dog'):
    """Displays info about the pet"""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

describe_pet('coco', 'hamster')
describe_pet('harry')