import logging
class  AccessDenied(Exception):
    pass
try:
    age=int(input("enter age:  "))
    if age<18:
        raise AccessDenied("Your age is less than 18")
    else:
        logging.info("User age is less than 18")    
except AccessDenied as E:
    print(E)
    logging.exception("Your age is not valid")
