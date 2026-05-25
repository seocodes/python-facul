

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

temperatures = []

sum_temp = 0
# so o primeiro trimestre fds
for i in range(3):
    try:
        temperature = float(input(f"Enter the median temperature from {months[i]}: "))
        temperatures.append(temperature)
        sum_temp += temperature
    except ValueError:
        print("Invalid input. Please enter a valid temperature.")

avg_temp = sum_temp / len(temperatures)
print(f"The average temperature is: {round(avg_temp, 2)}")

print("Temperaturas above annual average:")
for i in range(len(temperatures)):
    if temperatures[i] > avg_temp:
        print(f"{i + 1} - {months[i]}: {temperatures[i]}")


