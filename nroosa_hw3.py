with open('/Users/nolanroosa/Downloads/JustLeeBooks (1).txt', 'r') as jl:
    commands = []
    for line in jl:
        clean = line.strip('\n')
        if len(clean) > 0:
            commands.append(clean)
print(commands)
            
# 2
import sqlite3
connection = sqlite3.connect('LeeBooks.db')
cursor = connection.cursor()
for i in commands:
    cursor.execute(i)
connection.commit()

# 3
query = 'SELECT name FROM sqlite_master WHERE type="table"'
cursor.execute(query)
row = cursor.fetchall()

for name in row:
    print('\nTable: {}'.format(name[0]))
    queryY = 'PRAGMA table_info('+name[0]+')'
    cursor.execute(queryY)
    colNames = cursor.fetchall()
    print('Columns: ', end = '')
    for i in colNames:
        print(i[1], '| ', end = '')
    print('')

    # 4
import pandas as pd
query4 = 'SELECT LASTNAME, FIRSTNAME, STATE\
          FROM CUSTOMERS'
cursor.execute(query4)
customers = cursor.fetchall()
customersDF = pd.DataFrame(customers, columns = [name[0] for name in cursor.description])
print(customersDF)

# 5
query5 = 'SELECT ORDERNUM, QUANTITY, PAIDEACH\
          FROM ORDERITEMS'
cursor.execute(query5)
orders = cursor.fetchall()
orderItemsDF = pd.DataFrame(orders, columns = [name[0] for name in cursor.description])
print(orderItemsDF)

query5 = 'SELECT ORDERNUM, QUANTITY, PAIDEACH,\
          (QUANTITY*PAIDEACH) AS TOTAL\
          FROM ORDERITEMS'
cursor.execute(query5)
orders = cursor.fetchall()
orderItemsDF = pd.DataFrame(orders, columns = [name[0] for name in cursor.description])
print(orderItemsDF)
print('\n\tTotal Revenue = ${}'.format(orderItemsDF["TOTAL"].sum()))
