with open("day_4.txt", "a") as file:
    file.write('hello')
with open("day_4.txt", "r") as file:
    content = file.read()
print(content)
