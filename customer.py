#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb
cgitb.enable()

# Create instance of FieldStorage
form = cgi.FieldStorage()

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Online Registration Form</title>")
print ("</head>")
print ("<body>")

print ("Registration Form")

print ("<form action=\"/cgi-bin/customerins.py\" method=GET>")
print ("  First Name : <input type=text name=FIRST_NAME value=\"\" size=23>")
print ("  <br>")
print ("  Last Name : <input type=text name=LAST_NAME value=\"\" size=23>")
print ("  <br>")
print ("  Address : <input type=text name=ADDRESS value=\"\" size=23>")
print ("  <br>")
print ("  Contact No : <input type=text name=CONTACT_NO value=\"\" size=23>")
print ("  <br>")
print ("  Email: <input type=text name=EMAIL value=\"\" size=23>")
print ("  <br>")
print ("  Password: <input type=password name=PASSWORD value=\"\" size=23>")
print ("  <br>")
print ("    <input type=submit value=Submit name=B1>")
print ("    <input type=reset value=Reset name=B2>")
print ("  </form>")
print ("</body>")
print ("</html>")
