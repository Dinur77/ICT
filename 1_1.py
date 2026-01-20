def calculate_average(grades):
    return sum(grades) / len(grades)

grades = [] 

for i in range(5):
    grade = float(input())
    grades.append(grade)

print(calculate_average(grades))