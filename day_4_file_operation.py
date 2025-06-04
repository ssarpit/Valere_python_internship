import csv
import pandas as pd
import json

with open("myfile.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

df = pd.read_csv("myfile.csv")
print(df.head())
print(df.describe())
print(df["Product"])
print(df["Price"].mean())

df = pd.read_csv("order_details.csv")
df1 = df[0:1]
print(df1)
print(df.describe())

with open("Day4.txt", "a") as file:
    file.write('hello')

# WORKING ON JSON FILE
# TO READ THE JSON FILE WE USE LOAD FUNCTION

d = {"name": "aj"}
with open("Day_4.json", "a") as file:
    content = json.load(file)
print(content)

# WRITING IN JSON FILE

# Dump is used for writing in the json file

with open("Day_4.json", "a") as file:
    content = json.dump(d, file)
    print(content)

d1 = pd.read_csv("myfile.csv")
df = pd.DataFrame(d1)
print(df)
