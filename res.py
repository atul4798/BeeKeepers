#!C:\Python27\python.exe
import MySQLdb
print "Content-Type:text/html\n\n"
import cgi
data=cgi.FieldStorage()
state=data.getvalue('state')
city=data.getvalue('city')
deptt=data.getvalue('deptt')
exp=data.getvalue('exp')
con=MySQLdb.connect("127.0.0.1","root","","beekeepers",3306)
cmd=con.cursor()
query="select name,gender,phone,exp from seekers where city='"+city+"' and state='"+state+"' and deptt='"+deptt+"' and exp='"+exp+"'"
cmd.execute(query)
res = cmd.fetchall()
print"""
<!DOCTYPE html>
<html lang="en">
<head>
  <link rel="stylesheet" type="text/css" href="res.css">
  <title>Result</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
</head>
<body>

<div class="jumbotron text-center" style="margin-bottom:0;background: red;">
  <h1>Result</h1>
  <p>Description</p> 
</div>


<nav class="navbar navbar-expand-sm bg-dark navbar-dark">
  <a class="navbar-brand" href="#">BeeKeepers</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="collapsibleNavbar">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#">check</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">check</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">check</a>
      </li>    
    </ul>
  </div>  
</nav>
"""
for row in res:
	print"""<div class="row"><div class="column"><div class="card">"""
	print"<h3>",row[0],"</h3>","<p>",row[1],"</p>","<p>",row[2],"</p>","<p>",row[3],"</p>","</div>","</div>"
	print"</div>"
print"""
<div class="jumbotron text-center" style="margin-bottom:0">
<p>Footer</p>
</div>

</body>
</html>
"""
