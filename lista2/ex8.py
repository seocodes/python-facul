products = {}

while True:
    try:
        code = input("Enter the product code: ")
        info = []
        name = input("Enter the product name: ")
        price = float(input("Enter the product price: "))
        qtd = int(input("Enter the product quantity: "))
        info.append(name)
        info.append(price)
        info.append(qtd)
        products[code] = info

        answer = input("Do you want to add another product? (y/n): ")
        if answer.lower() != "y":
            break
    except (ValueError, TypeError):
        break

total = 0
subtotal = None
for code, product in products.items():
    subtotal = product[1] * product[2]
    total += subtotal
    print(f"{code}: {product[0]} - ${product[1]:.2f} x {product[2]} = ${subtotal:.2f}")

print(f"Total: ${total:.2f}")

