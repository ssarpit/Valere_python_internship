import csv
import pandas as pd
import json

#APPLYING READ OPERATION IN CSV FILE
with open("myfile.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#APPLYING WRITE OPERATION IN CSV FILE

data = [
    ['Name', 'Branch', 'Year', 'CGPA'],
    ['Nikhil', 'COE', 2, 9.0],
    ['Sanchit', 'COE', 2, 9.1],
    ['Aditya', 'IT', 2, 9.3],
    ['Sagar', 'SE', 1, 9.5],
    ['Prateek', 'MCE', 3, 7.8],
    ['Sahil', 'EP', 2, 9.1]
]
d=[{"name":"aj","age":22}]
f=["name","branch","year","cgpa"]
# with open("myfile.csv","w") as file:
#     content=csv.DictWriter(file,fieldnames=f)
#     content.writerows(d)

with open("myfile.csv","a") as file:
    content=csv.writer(file)
    content.writerow(data)