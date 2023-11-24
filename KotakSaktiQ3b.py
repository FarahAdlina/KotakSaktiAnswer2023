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

sql_query2b= pd.read_sql_query('''
#Create common table expression(CTE) that save temporary table
WITH CUSTOMER_PURCHASE AS
(
	SELECT
		#check the id, name and total books bought
		c.ID,
   	c.NAME AS CUSTOMER_NAME,
   	SUM(il.QUANTITY) AS total_bought
   	
	FROM
		#Left join cutomer table with invoice table then  right join with invoice_lines table
   	CUSTOMERS c
   	LEFT JOIN INVOICES i ON c.ID = i.CUSTOMER_ID
   	RIGHT JOIN INVOICE_LINES il ON i.ID = il.INVOICE_ID 
	
	#Group the invoice_id	
	GROUP BY
   	il.INVOICE_ID
   
	#After grouping, sum the quantity and check if it is more than 5	
	HAVING
		SUM(il.QUANTITY) > 5
)

#Perform another query based on the CTE 
SELECT
	#Count the number of id bought more than 5
	COUNT(ID) AS NUMBERS_OF_CUSTOMERS_BOUGHT_MORE_THAN_5
FROM 
	CUSTOMER_PURCHASE;                             
''', connection)

df = pd.DataFrame(sql_query2b)
print(df)
