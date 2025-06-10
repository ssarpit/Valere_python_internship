from psycopg2 import connect

# # declare the connection string specifying
# # the host name database name
# # use name and password
# try:
#     conn_string = "host='localhost' \
#     dbname='postgres' user='postgres'\
#     password='root'"
#     print("connection established")
# except:
#     print("connection error")

try:
    conn_string = "host='localhost' \
    user='postgres'\
    password='root'"
    print("connection established")
except BaseException:
    print("connection error")

# # use connect function to establish the connection
conn = connect(conn_string)
conn.autocommit = True
c = conn.cursor()
# def show_databases():
#     c.execute(f"""Show Databases""")
#     for i in c:
#         print(i)
# show_databases()
# def create_database():
#     c.execute('''Create database Employee''')

# # Call the function
# create_database()


def show_databases():
    c.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
    for i in c:
        print(i)


show_databases()
try:
    conn_string = "host='localhost' \
    dbname='employee' user='postgres'\
    password='root'"
    print("connection established")
except BaseException:
    print("connection error")


def create_table():
    c.execute(
        "create table employee_records (id int primary key,name varchar(255),salary int not null)")
    print("SUCCESSFULLY CREATED TABLE")
# create_table()


def show_tables():
    c.execute("""
        SELECT 'employee_records'
        FROM information_schema.tables
        WHERE table_schema = 'public' AND table_type='BASE TABLE';
    """)
    for table in c.fetchall():
        print(table[0])


show_tables()

# INSERTING INTO TABLES VALUES
# def insert_into_values():
#     c.execute("Insert into employee_records (id,name,salary) values (101,'arpit',50000), (102,'aj',52000)")
# insert_into_values()


def read_values():
    c.execute("Select * from employee_records order by id")
    result = c.fetchall()
    for i in result:
        print(i)


read_values()
print("Applying Read_values")


def read_values_1():
    c.execute("Select * from employee_records where name='arpit'")
    result = c.fetchall()
    for i in result:
        print(i)


read_values_1()
print("applying update ")


def update_details():
    c.execute("Update employee_records set salary=48000 where salary =50000 ")


update_details()
read_values()

print("deleting values from table")


def delete_values():
    c.execute("Delete from employee_records where name='aj'")


delete_values()

read_values()
