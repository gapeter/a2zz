#!/usr/bin/python

import cgi, cgitb
import smtplib
import MySQLdb

cgitb.enable()

#Create instance of FieldStorage
form = cgi.FieldStorage()
names = form.getvalue('confirm')
email = form.getvalue('email')

print("Content-type:text/html\r\n\r\n")
print("<HTML>")

#print("<form method=GET action=/cgi-bin/products.py>")

print ("  <br>")
print ("  <br>")

if(names!='no'):
    #open database connection
    db = MySQLdb.connect(host='localhost',user='root',passwd='Sap123$')
    #Preapare a cursor object using cursor()method
    cursor = db.cursor()
    cursor.execute('use A2Z')

    # Execute the SQL command
    cursor.execute("SELECT CART.*, PRODUCT_MASTER.*  FROM CART INNER JOIN PRODUCT_MASTER ON CART.PRODUCT_ID = PRODUCT_MASTER.PRODUCT_ID WHERE EMAIL = email")
    try:

       # Fetch all the rows in a list of lists.
       results = cursor.fetchall()
       for row in results:
  
          print(row)
          print ("  <br>")
          # Now print fetched result
    except:
       print ("Error: unable to fetch data")

    #disconnect from server
    db.close()

print("</form>")
print("</HTML>")

