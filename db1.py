import MySQLdb
#Create the connection object
myconn = MySQLdb.connect("localhost","root","root")
#creating the cursor object
cur = myconn.cursor()
#executing the query
dbs = cur.execute("show databases")
#display the result
for x in cur:
	print(x)
#close the connection
myconn.close()
