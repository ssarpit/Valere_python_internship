# IF ELSE IN PYTHON
#NUMBER IS GREATER
# a=int(input("enter number 1: "))
# b=int(input("enter number 2: "))
# c=int(input("enter number 3: "))
# if(a>b) and (a>c):
#     print("a is greater")
# elif (b>a) and (b>c):
#     print("b is greater")
# else:
#     print("c is greater")
5 
# LOOPS IN PYTHON 
#print table of 5 using for loop 
# num=int(input("enter table of : "))
# for i in range(1,11):
#     print(f"{num} * {i}={num*i}")
#USING WHILE LOOP
# i=1
# while(i<11):
#     print(f"{num}*{i}={num*i}")
#     i=i+1

#FUNCTIONS IN PYTHON 
# num=int(input("enter number: "))
# fact=1
# def factorial(num):
#     fact=1
#     for i in range(2,num+1):
#         fact=fact*i
#     return fact
# print(f"factorial of number {num} is {factorial(num)}")

#Recursion in python 
# def factorial(num):
#     if num==0 or num==1:
#         return 1
#     else:
#         return num*factorial(num-1)
# print(factorial(5))
# LAMBDA FUNCTION 
square =lambda x:x*x
print(square(2))
# for i in range(1,11):
sum=lambda i:i+1
print(sum(5))


# #FUNCTION TO CHECK NUMBER IS PRIME 
# num=int(input("enter number"))
# prime=0
# for i in range(2,num):
#     if(num%i==0):
#         prime=1
#         break
# if(prime):
#     print("Number is not  prime")
# else:
#     print("number is  prime")
    
