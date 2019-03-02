#!/usr/bin/python

import cgi, cgitb
import smtplib
import MySQLdb

cgitb.enable()

#Create instance of FieldStorage
form = cgi.FieldStorage()
names = form.getvalue('confirm')
email = form.getvalue('EMAIL')
product_id = form.getvalue('PRODUCT_ID')
qty  = form.getvalue('QTY')

print("Content-type:text/html\r\n\r\n")
print("<HTML>")

print ("  <br>")
print ("  <br>")

if(names!='no'):
    #open database connection
    db = MySQLdb.connect(host='localhost',user='root',passwd='Sap123$')
    #Preapare a cursor object using cursor()method
    cursor = db.cursor()
    cursor.execute('use A2Z')
    # Execute the SQL command
    cursor.execute('insert into CART(EMAIL,PRODUCT_ID, QTY) values("%s","%s","%d")' % (email, product_id, qty))
    print("INSERTED")    
    db.commit()
    #disconnect from server
    db.close()
print("</form>")
print("</HTML>")

