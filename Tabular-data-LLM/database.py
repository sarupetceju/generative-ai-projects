import sqlite3
connection=sqlite3.connect("customer.db")
cursor=connection.cursor()
table_definition = """
Create table CUSTOMER(CUSTOMER_NAME VARCHAR(25),AGE INT, LANDING_SCREEN INT,
PRODUCT_DETAILS INT,PAYMENT_SCREEN INT, FUlFILLMENT_SCREEN INT);
"""
cursor.execute(table_definition)
cursor.execute('''Insert Into CUSTOMER values('Michael', 35,1,1,0,0)''')
cursor.execute('''Insert Into CUSTOMER values('Akarsh', 30,1,1,1,1)''')
cursor.execute('''Insert Into CUSTOMER values('Sydney', 23,1,1,1,1)''')
cursor.execute('''Insert Into CUSTOMER values('Brian', 45,1,1,0,0)''')
cursor.execute('''Insert Into CUSTOMER values('Runi', 39,1,1,1,0)''')
cursor.execute('''Insert Into CUSTOMER values('David', 22,1,1,1,1)''')
cursor.execute('''Insert Into CUSTOMER values('David', 21,1,1,1,1)''')
cursor.execute('''Insert Into CUSTOMER values('David', 60,1,1,1,0)''')
cursor.execute('''Insert Into CUSTOMER values('David', 55,1,1,1,0)''')
cursor.execute('''Insert Into CUSTOMER values('David', 42,1,1,1,0)''')
cursor.execute('''Insert Into CUSTOMER values('David', 23,1,1,1,1)''')
cursor.execute('''Insert Into CUSTOMER values('David', 18,1,1,1,1)''')


print("The records added successfully are ")
data=cursor.execute('''Select * from CUSTOMER''')
for row in data:
    print(row)
connection.commit()
connection.close()