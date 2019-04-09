import MySQLdb

db = MySQLdb.connect("localhost", "root", "fIf@Ty5050!", "opnalpha")

cur = db.cursor()

"""print("1. Company name\n2. EBITDA\n3. Cashflows (Monthly)\n4. Cashflows (Annual)\n5. Pre money valuation\n6. Post money valuation\n7. Shares outstanding\n0.Exit")

while(True):
	endpoint = input("Requested data point:")

	if(endpoint == 0): 
		break

	cur.execute("SELECT * FROM decisionMetrics")
	for row in cur.fetchall():
		print row[endpoint-1]
"""
print("Company manifest: \n")

cur.execute("SELECT company_name FROM decision_metrics")
counter = 1
for row in cur.fetchall():
	print "",counter," ",row[0],""
	counter = counter + 1

endpoint = raw_input("Enter Company name:")
print("\n")
print("Finances")
query1 = """SELECT * FROM decision_metrics WHERE company_name = %s"""
cur.execute(query1, (endpoint, ))
record = cur.fetchall()
for i in range(len(cur.description)):
	for row in record:
		print (str(cur.description[i][0])+": "+str(row[i]))

print("\n")
print("Customers")
query2 = """SELECT * FROM customers WHERE company_name = %s"""
cur.execute(query2, (endpoint, ))
record = cur.fetchall()
for i in range(len(cur.description)):
	for row in record:
		print(str(cur.description[i][0])+": "+str(row[i]))


print("\n")
print("Web stats")
query3 = """SELECT * FROM web WHERE company_name = %s"""
cur.execute(query3, (endpoint, ))
record = cur.fetchall()
for i in range(len(cur.description)):
	for row in record:
		print(str(cur.description[i][0]+": "+str(row[i])))


		
	
	


	

db.close()
