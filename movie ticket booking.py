#movie ticket software0
def menu():                 #Menu
    c = 'y'
    while (c=='y'):
        print("1: Book Ticket")
        print("2: Update Ticket Booked")
        print("3: Cancel Booking")
        print("4: View Booking")
        print("5: Exit")
        choice=input("Enter your choice:")
        if choice == "1":
            adddata()
        elif choice == "2":
            updatedata()
        elif choice == "3":
            deldata()
        elif choice == "4":
            fetchdata()
        elif choice == "5":
            print("Exiting")
            print("*****Thank you for visiting*****")
            break
        else:
            print("Wrong Input")

def fetchdata():            #To view booking(Choice = 4)
    v_userID = input ("Enter your userID :")
    v_passwd = input ("Enter your password :")
    print("Wait... Fetching data...")
    import mysql.connector
    try:
        db = mysql.connector.connect(host = "localhost", user = "root", password = 'mainpadega', database = 'soft')
        cursor = db.cursor()
        cursor.execute("SELECT First_name, Last_name,sex,phone_no, Movie_name, ticket from theatre where userID = '%s' and paswd = '%s'" %(v_userID, v_passwd))
        results = cursor.fetchall()
        for x in results:
            print(x, end = "\n----------------------------\n")
    except:
        print("Error: unable to fetch data")

def adddata():              #To Book Ticket(Choice = 1)
        print("Please Wait...")
        import mysql.connector
        db = mysql.connector.connect(host = "localhost", user = "root", password = 'mainpadega', database = 'soft')
        cursor = db.cursor()
        v_fname = input ("Enter your first name :")
        v_lname = input ("Enter your last name :")
        v_sex = input ("Enter your sex(M/F/O) :" )
        v_phno = input("Enter your phone number :")
        v_userID = input ("Create UserID :")
        v_passwd = input ("Create Password :")
        v_mname = input("Enter the movie name :")
        v_tic = input("Enter total tickets :" )
        v_ins= "insert into theatre values( '{}','{}','{}','{}','{}','{}','{}','{}')".format(v_fname,v_lname,v_sex,v_phno,v_userID,v_passwd,v_mname,v_tic)
        cursor.execute(v_ins)
        db.commit()
        bk = " Ticket Booked. Congrats!!!"
        print(bk.center(50))

def updatedata():           #To Update ticket booked(Choice = 2)
    print("Please Wait...")
    import mysql.connector
    try:
        db = mysql.connector.connect(host = "localhost", user = "root", password = 'mainpadega', database = 'soft')
        cursor = db.cursor()
        v_userID = input ("Enter your userID :")
        v_passwd = input ("Enter your password :")
        v_tic = input("Update total tickets:")
        sql = ("Update theatre set ticket=%s where userID = '%s' and paswd = '%s'" % (v_tic, v_userID, v_passwd))
        cursor.execute(sql)
        up = "Ticket Updated!!!"
        print(up.center(50))
        db.commit()
    except Exception as e:
            print(e)

def deldata():              #To Cancel Booking(Choice = 3)
    import mysql.connector
    db = mysql.connector.connect(host = "localhost", user = "root", password = 'mainpadega', database = 'soft')
    cursor = db.cursor()
    v_userID = input ("Enter your userID :")
    v_passwd = input ("Enter your password :")    
    sql  = ("delete from theatre where userID = '%s' and paswd = '%s'" % (v_userID, v_passwd))
    a = cursor.execute(sql)
    if a==None:
        can = "Booking Cancelled"
        print(can.center(50))
    else:
        er = "Error"
        print(er.center(50))
        tr = "Try Again"
        print(tr.center(50))
    db.commit()

wlcm= "*****Welcome to BookMyTicket*****"
print(wlcm.center(50))

i=1  
while i>0:
    c=input("Do you want to continue(y) or not(n):")
    if c=='y' or c=='Y':
        menu()
        i=-1
    elif c=='n' or c=='N':
        print("*****Thank you for visiting*****")
        input("Press Enter to Exit")
        i=-1
    else:
        print("Wrong Input")
        
