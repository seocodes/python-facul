
numbers = []

while True:
    try:
        num = int(input(f"Enter the number: "))
        
        if num == -1:
            break
        if num < -1:
            continue
        numbers.append(num)
        
    except ValueError as e:
        print(f"Error: {e}")

if len(numbers) > 0:
    sum = sum(numbers)
    print(f"Sum: {sum}")
    median = sum / len(numbers)
    print(f"Median: {median}")
    
    lowest = min(numbers)
    print(f"Lowest: {lowest}")
    highest = max(numbers)
    print(f"Highest: {highest}")
