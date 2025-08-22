import pymysql as mys
import time

def connectbase():
    mycon = mys.connect(host="localhost", user="root", passwd="shuban2007", database="hospital")
    mycursor = mycon.cursor()
    return(mycon , mycursor)

def allpatient(mycursor):
    print("PRINTING ALL DATA \n")
    mycursor.execute("select * from patient;")
    mydata = mycursor.fetchall()
    for row in mydata:
        print(row)

def alldoctor(mycursor):
    print("PRINTING ALL DATA \n")
    mycursor.execute("select * from doctor;")
    mydata = mycursor.fetchall()
    for row in mydata:
        print(row)

def allappointment(mycursor):
    print("PRINTING ALL DATA \n")
    mycursor.execute("select * from appointment;")                  
    mydata = mycursor.fetchall()
    for row in mydata:
        print(row)

def addpatient(mycon, mycursor):
    PatientNo = int(input("Enter the patient number for the entry :"))
    PatientName =  input("Enter the name : ")
    PatientAge = input("Enter the age: ")
    PatientGender = input("Enter the gender: ")
    inn = ("insert into patient values(%s, %s, %s, %s)")
    values=[]
    values.append((PatientNo, PatientName, PatientAge, PatientGender))
    mycursor.executemany(inn, values)
    mycon.commit()
    time.sleep(3)
    print("PATIENT NAME ADDED TO THE DATABASE")
    print("CHANGES OCCUR AFTER YOU QUIT THE PROGRAM")

def addappointment(mycon, mycursor):
    print("ADDING APPOINTMENT, FILL THE ENTRY CORRECTLY BELOW : ")
    time.sleep(3)
    AppointmentId= int(input("Enter the appointment number : "))
    PatientId = int(input("Enter the patient id: "))
    PatientName = input("Enter patient name : ")
    DoctorId = int(input("Enter the doctor id: "))
    AppointmentDate = input("Enter the appointment date: ")
    AppointmentShift = input("Enter the shift of the appointment(morning/afternoon/evening/night) : ")
    mycursor.execute("insert into appointment values({0}, {1}, '{2}', {3}, '{4}', '{5}' );".format(AppointmentId, PatientId, PatientName, DoctorId, AppointmentDate, AppointmentShift))
    mycon.commit()
    time.sleep(3)
    print("APPOINTMENT ADDED TO DATABASE")
    print("CHANGES OCCUR AFTER YOU QUIT THE PROGRAM")

def removeappointment(mycon, mycursor):
    print("REMOVE THE APPOINTMENT ORDER: ")
    PatientNo = int(input("Enter the patient number to remove the appointment : "))
    PatientName = input("Enter the patient name : ")
    mycursor.execute("delete from appointment where patientno = {0};".format(PatientNo))
    mycon.commit()
    time.sleep(4)
    print("APPOINTMENT REMOVED FOR",PatientName)
    print("CHANGES OCCUR AFTER YOU QUIT THE PROGRAM")

def quitt(mycon):
    print("SAVING THE CACHE MEMORY INTO PERMANENT MEMORY")
    mycon.close()
    time.sleep(2)
    print("MEMORY SAVED SUCCESSFULLY")
    print("DATABASE DISCONNECTED")
    print("QUITING THE PROGRAM!!!!!!!!")
    
  
def loop():
    mycon, mycursor = connectbase()

    print("TOTAL ROWS =",mycursor.rowcount)

    print('''
0. Quit
1. All Patients
2. All Doctors
3. All Appointments
4. Add Patient
5. Add appointment
6. Remove Appointment
''')

    while True:

        run= int(input("ENTER THE OPERATION TO PROCEED THE SYSTEM :" ))
        if run==1:
            allpatient(mycursor)
        elif run==2:
            alldoctor(mycursor)
        elif run==3:
            allappointment(mycursor)
        elif run==4:
            addpatient(mycon,mycursor)
        elif run==5:
            addappointment(mycon,mycursor)
        elif run==6:
            removeappointment(mycon,mycursor)
        elif run==0:
            quitt(mycon)
            break
            
            
loop()
