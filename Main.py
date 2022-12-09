#PRogram to make SQL Database and Table

def database():             #To Create Database
    import mysql.connector as mysql
    mydb = mysql.connect(host = "localhost", user = "root", password = "mainpadega")
    mycursor = mydb.cursor()
    mycursor.execute("Create database soft")
    print("Database Created !!!!!!")

def table():                #To Create Table
    import mysql.connector as mysql
    mydb = mysql.connect(host = "localhost", user = "root", password = "mainpadega", database = "soft")
    mycursor = mydb.cursor()
    mycursor.execute("Create table theatre( First_name char(255),Last_name char(255),\
sex char(1),Phone_no bigint, userID varchar(50) Primary Key, paswd varchar(13),\
Movie_name varchar(255), ticket int(255))")
    print("Table Created!!!!!")
database() 
table()
