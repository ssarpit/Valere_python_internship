import mysql.connector

# Connecting to the MySQL server
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"
)
c = db.cursor()

# Function to create a database


def create_database(name):
    query = f"CREATE DATABASE IF NOT EXISTS {name}"
    c.execute(query)


# Call the function
create_database('arpit')


def show_databases():
    c.execute("Show Databases")
    for i in c:
        print(i)


show_databases()
print("Now working on tables ")
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database='arpit'
)
c = db.cursor()


def create_table(name):
    query = f"""CREATE TABLE IF NOT EXISTS {name}(roll_no int primary key,name varchar(255),age int ,email_id varchar(255))"""
    c.execute(query)


create_table('student')


def show_table():
    c.execute("Show Tables")
    for i in c:
        print(i)


show_table()
# def insert_into_table():
#     query=f"""Insert into student (roll_no,name,age,email_id) values (1,'arpit',22,'arpit0275@gmail.com'),(2,'aj',23,'aj@gmail.com')"""
#     c.execute(query)
#     db.commit()
# insert_into_table()


def read_values_2():
    query = f"""select * from student"""
    c.execute(query)
    myresult = c.fetchall()
    for i in myresult:
        print(i)


read_values_2()


def read_values():
    query = f"""select * from student where name='arpit'"""
    c.execute(query)
    myresult = c.fetchall()
    for i in myresult:
        print(i)


read_values()

print("WHERE CONDITION ")


def read_values_1():
    query = f"""select * from student where age>22"""
    c.execute(query)
    myresult = c.fetchall()
    for i in myresult:
        print(i)


read_values_1()

print("Working on Update commands ")


def update_details():
    query = f"""update student set  name='Arpit Jain' where name='arpit'"""
    c.execute(query)
    result = c.fetchall()
    for i in result:
        print(i)


update_details()
read_values_2()

print("DELETING VALUES IN TABLE")


def delete_values():
    query = f"""delete from student where name='aj'"""
    c.execute(query)
    result = c.fetchall()
    for i in result:
        print(i)


delete_values()
read_values_2()
