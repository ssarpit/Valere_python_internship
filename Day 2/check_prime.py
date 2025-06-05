

# FUNCTION TO CHECK NUMBER IS PRIME
num = int(input("enter number"))
prime = 0
for i in range(2, num):
    if (num % i == 0):
        prime = 1
        break
if (prime):
    print("Number is not  prime")
else:
    print("number is  prime")
