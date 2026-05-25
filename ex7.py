sales =  (120, 130, 100, 110, 90, 120, 111, 80, 140, 120, 90, 120)

n = len(sales)

sum = 0
for value in sales:
    sum += value
average = sum/n

# Variance
difference_of_squares = 0
for value in sales:
    difference = value - average
    difference_of_squares += difference ** 2
variance = difference_of_squares / n
print(f"Variance: {round(variance, 2)}")

# Standard deviation
std_dev = variance ** 0.5
print(f"Standard deviation: {round(std_dev, 2)}")

max_value = sales[0]
min_value = sales[0]

for value in sales:
    if value > max_value:
        max_value = value
    if value < min_value:
        min_value = value
print(f"Max value: {max_value}")
print(f"Min value: {min_value}")


