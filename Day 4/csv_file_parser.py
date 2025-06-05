import csv
with open("parser_file.csv", "r") as file:
    content = csv.reader(file)
    students = list(content)
print(students)

# APPLYING PARSING METHOD IN CSV FILE:
for student in students:
    print(student)
