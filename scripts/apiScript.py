import MySQLdb

db = MySQLdb.connect("localhost", "root", "fIf@Ty5050!", "opnalpha")

cur = db.cursor()

print("1. Company name\n2. EBITDA\n3. Cashflows (Monthly)\n4. Cashflows (Annual)\n5. Pre money valuation\n6. Post money valuation\n7. Shares outstanding\n0.Exit")

while(True):
	endpoint = input("Requested data point:")

	if(endpoint == 0): 
		break

	cur.execute("SELECT * FROM decisionMetrics")
	for row in cur.fetchall():
		print row[endpoint-1]

db.close()
