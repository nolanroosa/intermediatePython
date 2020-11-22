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
customersDF.sort_values(by = ['STATE'], inplace = True)
print(customersDF)
customersDF.sort_values(by = ['STATE', 'LASTNAME'], inplace = True)
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

# 6
query6 = 'CREATE TABLE BOOKLIST AS\
          SELECT LNAME, FNAME, TITLE\
          FROM BOOKS, BOOKAUTHOR, AUTHOR\
          WHERE BOOKS.ISBN = BOOKAUTHOR.ISBN AND\
              BOOKAUTHOR.AUTHORID = AUTHOR.AUTHORID'
cursor.execute(query6)
bookQuery = 'SELECT *\
            FROM BOOKLIST'
cursor.execute(bookQuery)
books = cursor.fetchall()
print(books)


# 7
booklistDF = pd.DataFrame(books, columns = [name[0] for name in cursor.description])
print(booklistDF)
booklistDF.sort_values(by = ['LNAME', 'FNAME'], inplace = True)
print(booklistDF)

queryGroup = 'SELECT LNAME, COUNT(*)\
              FROM BOOKLIST\
              GROUP BY LNAME'

cursor.execute(queryGroup)
grouped = cursor.fetchall()
print(grouped)

#there are two people with the last name 'WHITE' that are being counted together
#to get the correct counts for individual authors, we need to group by LNAME and FNAME


# 8
queryX = 'SELECT name\
          FROM sqlite_master\
          WHERE type="table"'
cursor.execute(queryX)
row = cursor.fetchall()

for name in row:
    print('\nTable: {}'.format(name[0]))
    queryY = 'PRAGMA table_info('+name[0]+')'
    cursor.execute(queryY)
    colNames = cursor.fetchall()
    print('Columns: ', end = '')
    for i in colNames:
        print(i[1], '| ', end = '')
    queryZ = 'SELECT COUNT(*)\
              FROM ('+name[0]+')'
    cursor.execute(queryZ)
    count = cursor.fetchall()
    print('\n # Rows = ', count[0][0])
    print('')
