# names = ['parsa', 'john', 'steve', 'alfred']
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])

from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
	first = input("\nPlease give me a first name: ")
	if first == 'q':
		break
	last = input("Please give me a last name: ")
	if last == 'q':
		break

	formatted_name = get_formatted_name(first, last)
	print(f"\nNeatly formatted name: {formatted_name}.")