# FUNCTION TO CHECK NUMBER IS PRIME
def check_prime(self):
    num = int(input("enter number"))
    prime = 0
    for i in range(2, num):
        if (num % i == 0):
            prime = 1
            break
    if (prime):
        return False
    else:
        return True
