import pymysql
try:
    #entire connection object will stored in conn variable
    conn=pymysql.connect(
        host="localhost",
        user="root",
        password="Harish258@@"
    )
    print("database connected successfully")
except Exception as e:
    print("error occured in connection",e)
cursor=conn.cursor()

try:
    cursor.execute("create database if not exists 66r_68r")
    print("database created successfully")
except Exception as e:
    print("error while creating database")

def createTable():
    try:
        cursor.execute("use 66r_68r")
        cursor.execute("""
                        create table if not exists students (id int primary key auto_increment,
                        name varchar(100),age int,
                        gender varchar(50),
                        email varchar(100))
                    """)
        print("table created successfully")

    except Exception as e:
        print("error while creating table",e)
def insertData():
    try:
        name=input("enter student name: ")
        age=int(input("enter age : "))
        gender=input("enter gender : ")
        email=input("enter email : ")
        cursor.execute("use 66r_68r")
        cursor.execute(f""" 
                    insert into students values({name},{age},{gender},{email});
        """)
        print("data inserted successfully into table")
    except Exception as e:
        print("error occured while inserting data",e)
def menu():
    print("choose 1 for creating new table: ")
    ip=int(input("enter choice"))
    if ip==1:
        createTable()
    elif ip==2:
        insertData()
    else:
        print("wrong option")

menu()
conn.commit()
cursor.close()
conn.close()