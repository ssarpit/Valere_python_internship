import mysql.connector
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root"
    )
    print("connection established")
except BaseException:
    print("connection error")
c = db.cursor()


def create_database(name):
    query = f"CREATE DATABASE IF NOT EXISTS {name}"
    c.execute(query)


# Call the function
create_database('Employee_Management_records')


def show_databases():
    c.execute("Show Databases")
    for i in c:
        print(i)


show_databases()


def use_databases():
    c.execute(" Use  Employee_Management_records")


use_databases()


def create_table():
    c.execute("Create table employee_table (id int  primary key,name varchar(255),salary int not null ,age int not null)")


# create_table()
# def drop_table():
#     c.execute("Drop table employee_table")
# drop_table()
print("done")


def insert_into_table():
    c.execute(
        "Insert into employee_table (id,name,salary,age) values (101,'arpit',50000,22),(102,'aj',52000,21)")


insert_into_table()


def read_values_2():
    query = f"""select * from employee_table"""
    c.execute(query)
    myresult = c.fetchall()
    for i in myresult:
        print(i)


read_values_2()


def update_details():
    query = f"""update employee_table set  name='Arpit Jain' where name='arpit'"""
    c.execute(query)
    result = c.fetchall()
    for i in result:
        print(i)


update_details()
read_values_2()


def delete_details():
    query = f"""delete from employee_table where name='aj'"""
    c.execute(query)
    result = c.fetchall()
    for i in result:
        print(i)


delete_details()
read_values_2()
