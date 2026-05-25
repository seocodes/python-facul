students = int(input("Enter the number of students: "))

p1 = []
p2 = []

print("Enter the grades of the first period: ")
for i in range(students):
    grade = float(input(f"Grade of student {i+1}: "))
    p1.append(grade)

print("Enter the grades of the second period: ")
for i in range(students):
    grade = float(input(f"Grade of student {i+1}: "))
    p2.append(grade)

median_p1 = round(sum(p1) / students)
median_p2 = round(sum(p2) / students)

print(f"Median of the first period: {median_p1}")
print(f"Median of the second period: {median_p2}")

if median_p1 > median_p2:
    print("The median of the first period is higher than the median of the second period.")
elif median_p2 > median_p1:
    print("The median of the second period is higher than the median of the first period.")
else:
    print("The medians of both periods are equal.")
