# # #VARIABLES AND DATA TYPES 
# # a=2
# # print(type(a))
# name="arpit jain "
# print(type(name))
# b=2.3
# print(type(b))
# is_developer=True
# print(type(is_developer))

# # #INPUT AND OUTPUT IN PYTHON 
# num1=(input("enter name "))
# print(num1)


# # #OPERATORS IN PYTHON
# a=2
# b=3
# print(a+b)
# print(a*b)
# print(a-b)
# print(a/b)
# print(a%b)
# print(a>=b)
# print(a<=b)

# #SIMPLE CALCULATOR IN PYTHON 

# num1=float(input("enter number_1 "))
# op=input("enter operation: ")
# num2=float(input("enter number_2 "))
# if op=="+":
#     print(num1+num2)
# elif op=="-":
#     print(num1-num2)
# elif op=="*":
#     print(f"Result:{num1*num2}")
# elif op=="/":
#     if num2!=0:
#         print(f"Result: {num1/num2}")
#     else:
#         print(f"DIVISION OF NUMBER BY ZERO GIVES INFINITY ")
# elif op=="%":
#     if num2!=0:
#         print(f"Result of modulo operator:{num1%num2}")
#     else:
#         print(f"Modulo operator does not work for zero denominator ")
# else:
#     print("INVALID OPERATION ")

    #calculator without using if else statement 
num1=float(input("enter number_1 "))
num2=float(input("enter number_2 "))
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)