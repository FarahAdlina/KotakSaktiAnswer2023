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

sql_query2c= pd.read_sql_query('''
SELECT
	#Show only a single time
	DISTINCT NAME AS CUSTOMER_NAME
	 
FROM
	#Left join customer table and invoice table
	CUSTOMERS as c 
	LEFT JOIN INVOICES AS i ON c.ID = i.CUSTOMER_ID

WHERE
	#Check if the customer id exist in the invoice  
	c.ID NOT IN 
	
	#Nested loop
	(
   	SELECT
			#Select customer with any invoice
			CUSTOMER_ID
			
   	FROM
   		#Left join invoice table with invoice_lines table
			INVOICES AS i2
   		LEFT JOIN INVOICE_LINES AS il2 ON i2.ID = il2.INVOICE_ID
	);                             
''', connection)

df = pd.DataFrame(sql_query2c)
print(df)