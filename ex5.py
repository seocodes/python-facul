size = int(input("Size of the list: "))

list = []

for i in range(size):
    num = int(input(f"Enter the number {i+1}: "))
    list.append(num)


even = []
for i in list:
    if i % 2 == 0:
        even.append(i)

print("Original list: ", list)
print("List without odd numbers: ", even)