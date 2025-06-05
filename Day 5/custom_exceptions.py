class invalidageerror(Exception):
    "age is smaller than 18 "
    pass


def eligibility():

    try:
        age = int(input("enter age "))
        if (age >= 18):
            print("You are eligible to vote")
        else:
            raise invalidageerror("age is less than 18")
    except invalidageerror as e:
        print("Age is invalid", e)


eligibility()
