#   # TRY AND EXCEPT BLOCKS
# # Printing the multiplication table of number
n = int(input("enter number: "))
try:
    for i in range(1, 11):
        print(f"{n}*{i}={n*i}")
except Exception as E:
    print(E)

    # NOW APPLYING TRY AND EXCEPT IN SIMPLE CALCULATOR PROGRAM


def calculator():
    num1 = float(input("enter number_1 "))
    op = input("enter operation: ")
    num2 = float(input("enter number_2 "))
    if op == "+":
        print(num1+num2)
    elif op == "-":
        print(num1-num2)
    elif op == "*":
        print(f"Result:{num1*num2}")
    elif op == "/":
        try:
            result = num1/num2
            print(f"Result: {result}")
        except Exception as e:
            print("float division", e)
    elif op == "%":
        try:
            result = num1 % num2
            print("Modulo of number is: ", result)
        except ZeroDivisionError:
            print("Not possible for zero denominator")
        else:
            print("Reaminder  is obtained")
        finally:
            print("All are printed")
    else:
        print("INVALID OPERATION ")


calculator()
