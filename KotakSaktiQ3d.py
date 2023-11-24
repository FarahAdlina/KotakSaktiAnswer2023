import pandas as pd
import mysql.connector as db

#Config database
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '1234',
    'database': 'bookstore'
}

#Establish a connection
connection = db.connect(**db_config)
cursor = connection.cursor()

sql_query2d= pd.read_sql_query('''
SELECT
	#Show book list with buyers name
   DESCRIPTION  as BOOK_LIST,
	NAME  as CUSTOMER_NAME

FROM
	#Left join invoice_lines with invoices and then with customers 
	INVOICE_LINES as li
	LEFT JOIN INVOICES as i on li.INVOICE_ID = i.ID
	LEFT JOIN CUSTOMERS as c on i.CUSTOMER_ID = C.ID                             
''', connection)

#Place in dataframe
df = pd.DataFrame(sql_query2d)
#Generate dataframe
print(df)