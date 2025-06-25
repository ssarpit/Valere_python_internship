
# WORKING ON JSON FILE
# TO READ THE JSON FILE WE USE LOAD FUNCTION
import pandas as pd
import json
d = {"name": "aj"}
with open("day_4.json", "r") as file:
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
