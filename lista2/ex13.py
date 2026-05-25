products = {}

for i in range(3):
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    products[name] = price

most_expensive_name = ""
most_expensive_price = 0

for name in products:
    if products[name] > most_expensive_price:
       most_expensive_name = name
       most_expensive_price = products[name]
       
print(f"The most expensive product is {most_expensive_name} with a price of {most_expensive_price}.")
