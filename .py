# Python-project-Animal-Vet
import os
import pymysql
import datetime
import platform

def selection():
    db=pymysql.connect(user='root', password='Saavi', host='localhost', database='Animal')
    cursor=db.cursor()
    print('-------------\nWELCOME TO ANIMAL VET\n----------')
    print("1. Animal Hospital")
    print("2. Animal Adoption")
    print("3. Donation")
    print("4. Volunteer")


def insert1():
    sname=input("Enter Animal specie: ")
    admno=input("Enter registration code: ")
    dob=input("Enter Date of Birth(Estimate) in (yyyy-mm-dd): ")
    cls=input("Enter department for treatment: ")
    cty=input("Enter city name: ")
    db=pymysql.connect(user='root', password='Saavi', host='localhost', database='Animal')
    cursor=db.cursor()
    sql="INSERT INTO register(sname,admno,dob,cls,cty) VALUES('%s', '%s', '%s', '%s', '%s')"%(sname,admno,dob,cls,cty)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()
#insert()
def display1():
    try:
        db=pymysql.connect(user='root', password='Saavi', host='localhost', database='Animal')
        cursor=db.cursor()
        sql="SELECT * FROM register"
        cursor.execute(sql)
        results=cursor.fetchall()
        for c in results:
            sname=c[0]
            admno=c[1]
            dob=c[2]
            cls=c[3]
            cty=c[4]
            print("(sname=%s,admno=%s,dob=%s,cls=%s,cty=%s)"%(sname,admno,dob,cls,cty))
    except:
        print("Unable to find data")
        db.close()

def display2():
    try:
        db=pymysql.connect(user='root', password='Saavi', host='localhost', database='Animal')
        cursor=db.cursor()
        sql="SELECT * FROM adoption"
        cursor.execute(sql)
        results=cursor.fetchall()
        for c in results:
            sname=c[0]
            admno=c[1]
            dob=c[2]
            cls=c[3]
            cty=c[4]
            print("(sname=%s,admno=%s,dob=%s,cls=%s,cty=%s)"%(sname,admno,dob,cls,cty))
    except:
        print("unable to find")
        db.close()

def update1():
    try:
        db=pymysql.connect(user='root', password='Saavi', host='localhost', database='Animal')
        cursor=db.cursor()
        sql="SELECT * FROM register"
        cursor.execute(sql)
        results=cursor.fetchall()
        for c in results:
            sname=c[0]
            admno=c[1]
            dob=c[2]
            cls=c[3]
            cty=c[4]
    except:
        print("Unable to find data")
    print()
    tempst=int(input("Enter registration number: "))
    temp=input("Enter new department: ")
    try:
        sql="Update register set cls=%s where admno='%s'"%(temp,tempst)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.close()
                
def delete1():
    try:
        db=pymysql.connect(user='root', password='Saavi', host='localhost', database='Animal')
        cursor=db.cursor()
        sql="SELECT *FROM register"
        cursor.execute(sql)
        results=cursor.fetchall()
        for c in results:
            sname=c[0]
            admno=c[1]
            dob=c[2]
            cls=c[3]
            cty=c[4]
    except:
        print("UnABLE to find data")
    temp=int(input("Enter registration number to be deleted: "))
    try:
              sql="delete from register where admno='%s'"%(temp)
              cursor.execute(sql)
              db.commit()
    except Exception as e:
              print(e)
              db.close()

def insert2():
    sname=input("Enter Animal species ")
    admno=input("Enter registration code: ")
    dob=input("Enter Date of Birth(Estimate) in (yyyy-mm-dd): ")
    cls=input("Enter department for- ")
    cty=input("Enter Reason to leave the animal- ")
    db=pymysql.connect(user='root', password='Saavi', host='localhost', database='Animal')
    cursor=db.cursor()
    sql="INSERT INTO adoption(sname,admno,dob,cls,cty) VALUES('%s', '%s', '%s', '%s', '%s')"%(sname,admno,dob,cls,cty)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()
              
def insert3():
    rcode=input("Enter registration number - ")
    sname=input("Enter your Name - ")
    admno=input("Enter your Contact Number - ")
    per=input("Enter your Email Id - ")
    res=input("Enter your Residential Address - ")
    db=pymysql.connect(user='root', password='Saavi', host='localhost', database='Animal')
    cursor=db.cursor()
    sql="INSERT INTO donations(rcode,sname,admno,per,res) VALUES ('%s', '%s', '%s', '%s', '%s')"%(rcode,sname,admno,per,res)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()

def update3():
    try:
        db=pymysql.connect(user='root', password='Saavi', host='localhost', database='Animal')
        cursor=db.cursor()
        sql="SELECT * from donations"
        cursor.execute(sql)
        results=cursor.fetchall()
        for c in results:
            rcode=c[0]
            sname=c[1]
            admno=c[2]
            per=c[3]
            res=c[4]
            
    except:
        print("Unable to find data")
    print()
    tempst=int(input("Enter registration number: "))
    temp=input("Enter new details: ")
    try:
        sql="Update donations set res=%s where rcode='%s'"%(temp,temst)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.close()

def delete3():
    try:
        db=pymysql.connect(user='root', password='Saavi', host='localhost', database='Animal')
        cursor=db.cursor()
        sql="SELECT * from donations"
        cursor.execute(sql)
        results=cursor.fetchall()
        for c in results:
            rcode=c[0]
            sname=c[1]
            admno=c[2]
            per=c[3]
            res=c[4]
    except:
        print("Unable to find data")
    temp=int(input("\nEnter reg no to be deleted: "))
    try:
        sql="delete from donations where rcode=='%s'"%(temp)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.close()


def insert4():
    sname=input("Enter Employee/volunteer name: ")
    admno=int(input("Enter registration number: "))
    per=float(input("Enter experience in years: "))
    res=input("Enter post: ")
    db=pymysql.connect(user='root', password='Saavi', host='localhost', database='Animal')
    cursor=db.cursor()
    sql="INSERT INTO exam(sname,admno,per,res) VALUES ('%s', '%s', '%s', '%s')"%(sname,admno,per,res)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()

def update4():
    try:
        db=pymysql.connect(user='root', password='Saavi', host='localhost', database='Animal')
        cursor=db.cursor()
        sql="SELECT * from exam"
        cursor.execute(sql)
        results=cursor.fetchall()
        for c in results:
            sname=c[0]
            admno=c[1]
            per=c[2]
            res=c[3]
    except:
        print("Unable to find data")
    print()
    tempst=int(input("Enter registration number: "))
    temp=input("Enter new details: ")
    try:
        sql="Update exam set res=%s where admno='%s'"%(temp,temst)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.close()

def delete4():
    try:
        db=pymysql.connect(user='root', password='Saavi', host='localhost', database='Animal')
        cursor=db.cursor()
        sql="SELECT * from exam"
        cursor.execute(sql)
        results=cursor.fetchall()
        for c in results:
            sname=c[0]
            admno=c[1]
            per=c[2]
            res=c[3]
    except:
        print("Unable to find data")
    temp=int(input("\nEnter reg no to be deleted: "))
    try:
        sql="delete from exam where admno=='%s'"%(temp)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.close()
selection()
ch=int(input("\nEnter your choice(1-4): "))
if ch==1:
    print("\nWelcome to Animal Hospital\n")
    print("a. New Registration for ward checkup")
    print("b. Update Pet details/department")
    print("c. Release patient")
    c=input("Enter your choice(a-c)")
    print("\nInitially the details are..\n")
    display1()
    if c=='a':
        insert1()
        print("\nModified details are..\n")
        display1()
    elif c=='b':
        update1()
        print("\nModified details are..\n")
        display1()
    elif c=='c':
        delete1()
        print("\nModified details are..\n")
        display1()
    else:
        print("Enter correct choice")

elif ch==2:
    print("\nWelcome to Adoption Centre\n")
    print("a. Register an Animal")
    print("b. Update Animal details")
    print("c. Adopt an Animal")
    c=input("Enter your choice(a-c)")
    print("\nInitially the details are..\n")
    display2()
    if c=='a':
        insert2()
        print("\nModified details are..\n")
        display2()
    elif c=='b':
        update2()
        print("\nModified details are..\n")
        display2()
    elif c=='c':
        delete2()
        print("\nModified details are..\n")
        display2()
    else:
        print("Enter correct choice")

elif ch==3:
    print("\nWelcome to Donation Window\n")
    print("a. New Donations(Money/Food/Clothes")
    print("b. Update Donator's Details")
    print("c. Withdraw Donations")
    c=input("Enter your choice(a-c)")
    if c=='a':
        insert3()
    elif c=='b':
        update3()
    elif c=='c':
        delete3()
    else:
        print("Enter correct choice")


elif ch==4:
    print("VOLUNTEER/ JOIN US")
    print("a. Volunteer/Recruit details")
    print("b. Update service/job details")
    print("c. Retirement/Transfer/Firing of an employee")
    c=input("Enter you choice(a-c)")
    if c=='a':
        insert4()
    elif c=='b':
        update4()
    elif c=='c':
        delete4()
    else:
        print("Enter correct choice")
else:
    print("Enter correct choice")

                        
                    
            
                    
        
            

