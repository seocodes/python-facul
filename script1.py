# n1 = int(input("Digite o número 1: "))
# n2 = int(input("Digite o número 2: "))
# n3 = int(input("Digite o número 3: "))

# sum = n1+n2+n3

# print(f"Sum = {sum}")


###########################################

# base = float(input("Input base size in cm: "))
# height = float(input("Input height in cm: "))

# rect_area = base*height

# print(f"Rectangle area is: {rect_area}")

###########################################

# n1 = float(input("Type num 1: "))
# n2 = float(input("Type num 2: "))

# try:
#     div = n1/n2
#     print(f"Division = {div}")
# except ZeroDivisionError:
#     print("Can't dive by zero")

###########################################

def getGrades():
    n1 = float(input("Type grade 1: "))
    n2 = float(input("Type grade 2: "))
    grades = [n1,n2]
    return grades

def calculateAvg(grades):
    sum_grades = sum(grades)
    avg = sum_grades / len(grades)
    return avg

def approvedOrNot(avg):
    if avg >= 7:
        return "Approved"
    else:
        return "Not Approved"

try:
    grades = getGrades()
    avg = calculateAvg(grades) 
    print(approvedOrNot(avg))

except IndexError:
    print("Insert a grade pls motherfucker")    
except ZeroDivisionError:
    print("Can't divide by zero")
except Exception as e:
    print(f"An error occurred: {e}")    


