#!C:\python27\python.exe
import cgi
import MySQLdb
print "Content-Type:text/html\n\n"

data=cgi.FieldStorage()
name=data.getvalue('name')
gender=data.getvalue('gender')
state=data.getvalue('state')
city=data.getvalue('city')
phone=data.getvalue('phone')
deptt=data.getvalue('deptt')
exp=data.getvalue('exp')
con=MySQLdb.connect("127.0.0.1","root","","beekeepers",3306)
cmd=con.cursor()
query="insert into seekers(name,gender,state,city,phone,deptt,exp) values('"+name+"','"+gender+"','"+state+"','"+city+"','"+phone+"','"+deptt+"','"+exp+"')"
cmd.execute(query)
con.commit()
con.close()
print "<script>alert('Successfully Registered');window.location.href='reg.html';</script>"