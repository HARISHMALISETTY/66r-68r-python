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
        query="""insert into students (name,age,gender,email) values (%s,%s,%s,%s)"""
        values=(name,age,gender,email)
        cursor.execute(query,values)
        print("data inserted successfully into table")
    except Exception as e:
        print("error occured while inserting data",e)
def insertManyRecords():
    try:
        cursor.execute("use 66r_68r")
        data=[('harish',26,'male','harish@gmail.com'),('nandu',25,'female','nandu@gmail.com'),('sushma',25,'female','sushma@gmail.com')]
        query="""insert into students (name,age,gender,email) values (%s,%s,%s,%s)"""
        cursor.executemany(query,data)
        print("data inserted successfully")
    except Exception as e:
        print('error occured while inserting data',e)

def updateStudentEmailById():
    try:
        cursor.execute('use 66r_68r')
        stud_id=int(input("enter student id"))
        email=input("enter email: ")
        query="""update students set email=%s where id =%s"""
        values=(email,stud_id)
        cursor.execute(query,values)
        print("record updated successfully")
    except Exception as e:
        print("error occured",e)

#updatestudentnamebyid
#updatestudentagebyid
#deleterecordbyid

def menu():
    print("choose 1 for creating new table: ")
    print("choose 2 for inserting data")
    print("choose 3 for fetching records")
    print("choose 4 for inserting multiple records")
    print("choose 5 for updating record")

    ip=int(input("enter choice"))
    if ip==1:
        createTable()
    elif ip==2:
        insertData()
    elif ip==3:
        getData()
    elif ip==4:
        insertManyRecords()
    elif ip==5:
        updateStudentEmailById()
    else:
        print("wrong option")

menu()
conn.commit()
cursor.close()
conn.close()