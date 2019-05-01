import MySQLdb

db = MySQLdb.connect("localhost", "root", "fIf@Ty5050!", "opnalpha")

cur = db.cursor()

companyName = raw_input("Enter company name:")
EBIDTA = raw_input("Enter EBIDTA")
cashflows_monthly = raw_input("Enter cashflow monthly:")
cashflows_annual = raw_input("Enter cashflow annual:")
premoney = raw_input("Enter pre money:")
postmoney = raw_input("Enter post money:")
sharesOutstanding = raw_input("Enter shares outstanding: ")

january = raw_input("Enter january:")
february = raw_input("Enter february:")
march= raw_input("Enter march:")
april= raw_input("Enter April:")
may= raw_input("Enter May:")
june = raw_input("Enter June:")
july = raw_input("Enter July:")
august = raw_input("Enter August:")
september= raw_input("Enter September:")
october = raw_input("Enter October:")
november= raw_input("Enter November:")
december= raw_input("Enter December:")


users = raw_input("Enter users:")
page_views = raw_input("Page views:")
pages_per_session = raw_input("Enter pages per session:")
bounce_rate = raw_input("Enter bounce rate:")
average_time_on_site = raw_input("enter average time on sight:")

new_users = raw_input("Enter new users:")
total_users = raw_input("Enter total users:")
enterprise_customers = raw_input("Enter enterprise customers:")
mom_growth = raw_input("enter Mom growth:")


sql1 = """INSERT INTO decision_metrics(company_name, EBIDTA, cashflows_monthly, cashflows_annual, premoney, postmoney, shares_outstanding)
VALUES (%s, %s, %s, %s, %s, %s, %s)"""
cur.execute(sql1, (companyName, EBIDTA, cashflows_monthly, cashflows_annual, premoney, postmoney, sharesOutstanding))
db.commit()



sql2 = """INSERT INTO monthly_earnings(company_name, january, february, march, april, may, june, july, august, september, october, november, december)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""


cur.execute(sql2, (companyName, january, february, march, april, may, june, july, august, september, october, november, december))
db.commit()

sql3 = """INSERT INTO web(users, company_name, page_views, pages_per_session, bounce_rate, average_time_on_site)
VALUES (%s, %s, %s, %s, %s, %s)"""

cur.execute(sql3, (users, companyName, page_views, pages_per_session, bounce_rate, average_time_on_site))
db.commit()

sql4 = """INSERT INTO customers(company_name, new_users, total_users, enterprise_customers, mom_growth)
VALUES (%s, %s, %s, %s, %s)"""

cur.execute(sql4, (companyName, new_users, total_users, enterprise_customers, mom_growth))
db.commit()

db.close()



