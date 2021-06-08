apple_products = ['macbook', 'iphone', 'apple tv', 'apple watch']
print(apple_products)

apple_products.append('ipad')
print(apple_products)

apple_products.remove('apple tv')
print(apple_products)

macbook = apple_products.pop(0)
print(apple_products)
print(f"I currently own a {macbook.title()} made by Apple")

apple_products.insert(0, macbook)
print(apple_products)

print(sorted(apple_products))

print(sorted(apple_products, reverse=True))

apple_products.reverse()
print(apple_products)

apple_products.sort()
print(apple_products)

print(len(apple_products))