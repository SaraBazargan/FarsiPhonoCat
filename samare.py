import pyodbc
DBfile = 'd:\\Flexicon.mdb'
conn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb)};DBQ='+DBfile)
cursor = conn.cursor()
cursor.execute("SELECT PhonologicalForm FROM Entries")


for row in cursor.fetchall():
    if 'Zo' in row[0]:
        print(row[0])

conn.close()
