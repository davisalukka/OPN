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


for j in range(1, len(cur.description)):
	for row in record:
		total_earnings += row[j]

print("Total earnigns for 2018-2019: "+str(total_earnings))

print("\n")
print("6 month history:")
half_yearly_earnings = 0


for j in range(6, len(cur.description)):
	for row in record:
		half_yearly_earnings += row[j]

print("Total earnigns for last 6 month period: "+str(half_yearly_earnings))









db.close()
