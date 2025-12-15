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

def showContacts():
    try:
        cursor.execute("use contact_book")
        query="select * from contacts"
        cursor.execute(query)
        rows=cursor.fetchall()
        if len(rows) == 0:
            print("no records found...!")
        else:
            for row in rows:
                print(f"col1_name:{row[0]}")
                print(f"col2_name:{row[1]}")
                print(f"col3_name:{row[2]}")
                print("----------------------------")
    except Exception as e:
        print("Error while searching the data",e)


def create_contact():
    try:
        cursor.execute("use contact_book")
        name=input("enter name : ")
        ph_num=int(input("enter phone number : "))
        query="""insert into contacts (name,phn_num) values (%s,%s)"""        
        values=(name,ph_num)
        cursor.execute(query,values)
        print("created contact successfully")
    except Exception as e:
        print("error while creating contact",e)

def update_contact():
    try:
        name = input("enter contact name: ")
        cursor.execute("use contact_book")
        print("select 1 to update name")
        print("select 2 to update phone_number")
        select = int(input("Enter choice: "))
        if select == 1:
            new_name = input("enter new name: ")
            query = """
                    update contacts set name = %s where name = %s
                    
                    """
            cursor.execute(query,(new_name,name))
            print("updated successfully")
        elif select == 2:
            new_ph_number = int(input("Enter new phone number: "))
            query = """
                    update contacts set phn_num = %s where name = %s
                    
                    """
            cursor.execute(query,(new_ph_number,name))
            print("updated successfully")
        else:
            print("invalid choice!")
    except Exception as e:
        print("unable to update",e)

def search_contact():
    try:
        cursor.execute("use contact_book")
        name=input('enter the name to search ')
        query="""select * from contacts where name = %s  """
        cursor.execute(query,name)
        rows=cursor.fetchall()
        if len(rows)>0:
            for i in rows:
                print(i)
        else:
            print("no contact found")
    except ValueError as e:
        print('error occured',e)

def delete_contact():
    try:
        cursor.execute("use contact_book")
        c_id=int(input("Enter id:"))
        query="delete from contacts where id=%s"
        cursor.execute(query,c_id)
        print("contact deleted successfully")
    except Exception as e:
        print("error while deleting data",e)

def menu():

    print("1. enter 1 for creating contact : ")
    print("2. enter 2 for show contacts : ")
    print("3. enter 3 for update contact : ")
    print("4. enter 4 for search contact : ")
    print("5.enter 5 for delete contact :")
    choice=int(input("enter ur choice: "))
    if choice==1:
        create_contact()
    elif choice==2:
        showContacts()
    elif choice==3:
        update_contact()
    elif choice==4:
        search_contact()
    elif choice==5:
        delete_contact()
    else:
        print("invalid choice")
menu()

conn.commit()
cursor.close()
conn.close()