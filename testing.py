num1=float(input("enter number_1 "))
op=input("enter operation: ")
num2=float(input("enter number_2 "))
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(f"Result:{num1*num2}")
elif op=="/":
    try:
        result=num1/num2
        print(f"Result: {result}")
    except Exception as e:
        print("float division",e)
elif op=="%":
    if num2!=0:
        print(f"Result of modulo operator:{num1%num2}")
    else:
        print(f"Modulo operator does not work for zero denominator ")
else:
    print("INVALID OPERATION ")
