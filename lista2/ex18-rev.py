n = int(input("Type a number: "))

count = 1

for i in range(1, n+1):  # for each row
    row = ""
    for j in range(i):
        row += str(count) + " "
        count += 1 # make each number +1 
    print(row.strip())