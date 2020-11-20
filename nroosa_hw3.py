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

query = 'PRAGMA table_info (EMPLOYEES)'
cursor.execute(query)
