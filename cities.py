# prompt = "\nGive a name of a city you've visited before."
# prompt += "\n(Press 'q' when you are finished) "

# while True:
#     city = input(prompt)

#     if city == 'q':
#         break
#     else:
#         print(f"\n{city.title()} is very cool!")


def describe_city(city, country='England'):
    print(f"{city.title()} is in {country.title()}.")


describe_city('london')
describe_city('manchester')
describe_city(city='tokyo', country='japan')