#!/usr/bin/python

import cgi, cgitb
import smtplib
import MySQLdb

cgitb.enable()

#Create instance of FieldStorage
form = cgi.FieldStorage()
names = form.getvalue('confirm')
fname = form.getvalue('FIRST_NAME')
lname = form.getvalue('LAST_NAME')
address = form.getvalue('ADDRESS')
contactno = form.getvalue('CONTACT_NO')
email = form.getvalue('EMAIL')
password  = form.getvalue('PASSWORD')

print("Content-type:text/html\r\n\r\n")
print("<HTML>")

print("Registration Form")

print ("  <br>")
print ("  <br>")

if(names!='no'):
    #open database connection
    db = MySQLdb.connect(host='localhost',user='root',passwd='Sap123$')
    #Preapare a cursor object using cursor()method
    cursor = db.cursor()
    cursor.execute('use A2Z')
    # Execute the SQL command
    cursor.execute('SELECT * from CUSTOMER WHERE EMAIL = ("%s")' % (email))

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    flag = 0
    for row in results:
       flag = 1
       print("E-mail : ", email, "Already exists ************")
    if flag == 0:
       cursor.execute('insert into CUSTOMER(FIRST_NAME,LAST_NAME,ADDRESS,CONTACT_NO,EMAIL,PASSWORD) values("%s","%s","%s","%s","%s","%s")' % (fname, lname, address, contactno, email,password ))
       print("INSERTED")    
    db.commit()

    #disconnect from server
    db.close()

print("</form>")
print("</HTML>")

