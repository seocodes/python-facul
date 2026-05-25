people = {}

def add_person(name, height, weight):
    people[name] = [height, weight]
    
for i in range(2):
    name = input(f"Enter name for person {i+1}: ")
    try:
        height = float(input(f"Enter height (cm) for person {i+1}: "))
        weight = float(input(f"Enter weight (kg) for person {i+1}: "))
        add_person(name, height, weight)
    except ValueError:
        print("Invalid input. Please enter a valid height and weight.")


shorter = None
weight_sum = 0
for person in people:
    height = people[person][0]
    weight = people[person][1]
    if shorter is None or height < shorter:
        shorter = height
        
    weight_sum += weight

print(f"The shortest person is {shorter} cm tall")
average_weight = weight_sum / len(people)
print(f"Average weight: {round(average_weight, 2)}")

# C - usar sorted nas keys/chaves do dicionario
print("Alphabetical order:")
for name in sorted(people.keys()):
    print(name)