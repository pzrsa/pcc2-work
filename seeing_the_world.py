places = ['japan', 'united states', 'switzerland', 'australia', 'canada']
print(places)

print("\nAlphabetical order of list:")
print(sorted(places))
print("\nOriginal order of list:")
print(places)

print("\nReverse alphabetical order of list:")
print(sorted(places, reverse=True))
print("\nOriginal order of list:")
print(places)

places.reverse()
print("\nReverse non-alphabetical order of list:")
print(places)

places.reverse()
print("\nBack to original list:")
print(places)

places.sort()
print("\nPermanent alphabetical order of list:")
print(places)

places.sort(reverse=True)
print("\nReverse permanent alphabetical order of list:")
print(places)