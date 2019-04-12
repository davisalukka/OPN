import MySQLdb

db = MySQLdb.connect("localhost", "root", "fIf@Ty5050!", "opnalpha")

cur = db.cursor()

print("Company manifest: \n")

cur.execute("SELECT company_name FROM decision_metrics")
counter = 1
for row in cur.fetchall():
	print "",counter," ",row[0],""
	counter = counter + 1

endpoint = raw_input("Enter Company name:")
print("\n")
print("Monthly earnings report:")
query1 = """SELECT * FROM monthly_earnings WHERE company_name = %s"""
cur.execute(query1, (endpoint, ))
record = cur.fetchall()
for i in range(len(cur.description)):
	for row in record:
		print (str(cur.description[i][0])+": "+str(row[i]))

print("\n")
print("Annual earnings report:")
total_earnings = 0
current_month = 0
confidence = 0


for j in range(1, len(cur.description)):
	for row in record:
		if(row[j] >= current_month):
			confidence += 1	
		total_earnings += row[j]
		current_month = row[j]

print("Annual earnings: "+str(total_earnings))

peratio = 20
valuation = total_earnings * peratio

print("Current valuation based on P/E and earnings: "+str(valuation))
confidence = (confidence / float(12)) * 100
print("confidence: "+str(confidence))

db.close()
