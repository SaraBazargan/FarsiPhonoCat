import pyodbc
DBfile = 'd:\\Flexicon.mdb'
conn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb)};DBQ='+DBfile)
cursor = conn.cursor()
cursor.execute("SELECT PhonologicalForm FROM Entries")
consonants = ["'", 'b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z', 'C', 'S', 'Z', 'y']
vowels = ['A', 'a', 'e', 'o', 'i', 'i', 'u']

list1 = []
for row in cursor.fetchall():
    heja = ''
    div_counter = 1
    #print(row[0])
    for char_num in range(len(row[0])):
        if div_counter - char_num < len(row[0]):
            if row[0][char_num - div_counter] == 'w':
                heja = 'D' + heja
                div_counter += 2
            elif row[0][char_num - div_counter] in consonants:
                heja = 'C' + heja
                div_counter += 2
            else:
                heja = '.CV' + heja
                div_counter += 3
        else:
            break
    heja = heja[1:]
    list1.append((row[0], heja))
print("size of lexicon = ", len(list1))

for i in list1:
    if "y\" in i[0] and i[1] == 'CVCC':
        print(i)

'''
list2 = []
for row in list1:
    if 'eg' in row[0] or 'og' in row[0]:
        list2.append(row[0]) 

list3 = []
for i in list2:
    if 'egi' not in i:
        if 'egA' not in i:
            if 'egu' not in i:
                if 'ega' not in i:
                    if 'ege' not in i:
                        if 'ego' not in i:
                            list3.append(i)
list4 = []
for i in list3:
    if 'ogi' not in i:
        if 'ogA' not in i:
            if 'ogu' not in i:
                if 'oga' not in i:
                    if 'oge' not in i:
                        if 'ogo' not in i:
                            list4.append(i)           

for i in list4:
    print(i)

'''
conn.close()
