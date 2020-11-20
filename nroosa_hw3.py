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
