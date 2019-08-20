
import collections
import pyodbc
DBfile = 'd:\\Flexicon.mdb'
conn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb)};DBQ='+DBfile)
cursor = conn.cursor()
cursor.execute("SELECT PhonologicalForm FROM Entries")
	
list1 = []
consonants = ["'", 'b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z', 'C', 'S', 'Z', 'y']
vowels = ['A', 'a', 'e', 'o', 'i', 'u']
'''
heja_kinds = ['CV', 'CVC', 'CVCC', 'CV.CV', 'CV.CVCC', 'CVC.CV', 'CVC.CVCC', 'CVCC.CVCC', 'CVCC.CVC', 'CVCC.CV', 'CV.CVC', 'CVC.CVC',
              'CVC.CV.CV', 'CV.CV.CV', 'CV.CV.CVC', 'CVC.CV.CVC', 'CV.CVC.CVC', 'CVC.CVC.CVC', 'CV.CVC.CV', 'CVC.CVC.CV', 'CVCC.CV.CV',
              'CV.CV.CVCC', 'CVC.CV.CVCC', 'CV.CVC.CVCC', 'CVCC.CV.CVC', 'CV.CVCC.CV', 'CV.CVCC.CVCC', 'CVCC.CV.CVCC', 'CVCC.CVCC.CV', 'CVCC.CVC.CV',
              'CVCC.CVCC.CVCC', 'CVCC.CVC.CVCC', 'CVC.CVCC.CVCC', 'CVCC.CVCC.CVC', 'CV.CVCC.CVC', 'CVC.CVCC.CV',
              'CV.CV.CV.CV', 'CVC.CV.CV.CV', 'CV.CVC.CV.CV', 'CV.CV.CV.CVC', 'CVC.CVC.CV.CV', 'CVC.CV.CV.CVC', 'CV.CV.CVC.CVC', 'CV.CVC.CV.CVC',
              'CVC.CVC.CV.CVC', 'CV.CV.CVC.CV', 'CVC.CV.CVC.CVC', 'CVC.CV.CVC.CV', 'CV.CVC.CVC.CV', 'CVCC.CV.CV.CV', 'CV.CV.CV.CVCC', 'CV.CVC.CVC.CVC',
              'CVC.CVC.CVC.CV', 'CV.CV.CV.CV.CV', 'CVC.CV.CV.CV.CV', 'CV.CVC.CV.CV.CV', 'CV.CV.CVC.CV.CV', 'CV.CV.CV.CV.CVC', 'CVC.CVC.CV.CV.CV',
              'CVC.CV.CVC.CV.CV', 'CVC.CV.CV.CV.CVC', 'CV.CVC.CVC.CV.CV', 'CVC.CVC.CV.CVC.CV', 'CV.CVC.CV.CVC.CV', 'CV.CV.CVC.CV.CVC', 'CV.CV.CV.CVC.CV',
              'CV.CVC.CV.CV.CVC', 'CVC.CV.CV.CVC.CV', 'CV.CV.CV.CVC.CVC', 'CVC.CV.CVC.CV.CVC', 'CVC.CVC.CVC.CV.CV', 'CVC.CV.CV.CVC.CVC', 'CVC.CVC.CV.CV.CVC',
              'CV.CV.CVC.CVC.CVC', 'CV.CV.CVC.CVC.CV', 'CV.CV.CV.CV.CVCC', 'CVC.CV.CV.CV.CVCC', 'CV.CV.CV.CV.CV.CV', 'CVCC.CV.CV.CVC', 'CVCC.CV.CVC.CV',
              'CVC.CV.CV.CVCC', 'CV.CVC.CVC.CV.CV.CV.CV', 'CVC.CVC.CVC.CV.CV.CV', 'CVC.CVC.CVC.CVC.CV',  'CVC.CVC.CVC.CVC', 'CV.CVC.CVC.CV.CV.CV.CV',
              'CVC.CV.CV.CV.CV.CV', 'CVC.CVC.CV.CVC.CV.CVC.CVC',  'CVC.CVC.CV.CVC.CV.CV.CVC', 'CVC.CVC.CVC.CVC', 'CVC.CVCC.CVC.CVC', 'CVC.CVCC.CVC',
              'CVCC.CVC.CV.CV', 'CV.CVCC.CV.CV', 'CVC.CV.CVC.CV.CVC.CV', 'CV.CV.CV.CV.CVC.CV', 'CV.CV.CVC.CVCC', 'CVC.CV.CVC.CVC.CV.CV',
              'CVC.CV.CVC.CV.CV.CV', 'CVCC.CVC.CVC', 'CV.CV.CV.CVCC.CV.CV', 'CVC.CV.CV.CV.CV.CV.CVC', 'CVC.CV.CV.CV.CV.CV.CVC.CV.CVC', 'CV.CVC.CV.CVCC',
              'CV.CVC.CVC.CV.CV.CV', 'CV.CV.CVC.CVC.CV.CV', 'CV.CV.CV.CVC.CV.CV', 'CV.CV.CV.CVC.CV.CV', 'CVC.CV.CV.CV.CVC.CVC', 'CV.CVC.CV.CVC.CVC',
              'CV.CV.CVC.CV.CV.CV', 'CVC.CV.CV.CV.CV.CVCC', 'CV.CVC.CVC.CV.CVC', 'CV.CV.CVC.CV.CVC.CVC', 'CVC.CVC.CVCC', 'CV.CV.CVC.CV.CV.CV.CV.CVC',
              'CV.CV.CV.CV.CV.CV.CV', 'CV.CVC.CVC.CV.CVC', 'CVC.CVC.CVCC', 'CVC.CVC.CV.CVCC', 'CVC.CVC.CV.CV.CV.CV.CVCC', 'CVCC.CV.CVC.CV.CV', 'CVCC.CV.CV.CV.CV',
              'CVC.CVC.CV.CV.CV.CV', 'CV.CV.CVC.CVC.CV.CVC', 'CVC.CV.CVC.CVC.CV.CVC.CV', 'CV.CVC.CVC.CV.CV.CVC', 'CVC.CVC.CVC.CVC.CV.CV', 'CV.CV.CV.CV.CV.CVC',
              'CVC.CVC.CVC.CV.CVC.CV.CV.CV.CVCC', 'CV.CV.CVC.CV.CV.CV.CV.CV', 'CVC.CV.CVC.CV.CVCC', 'CV.CVC.CV.CVC.CV.CVC', 'CV.CV.CVC.CV.CV.CVC.CV.CV',
              'CVC.CVC.CV.CV.CVCC', 'CVC.CV.CV.CV.CV.CVC', 'CV.CV.CV.CVC.CVC.CVC', 'CV.CV.CV.CV.CV.CVC', 'CVC.CVCC.CV.CV', 'CV.CVC.CV.CV.CV.CV', 'CV.CV.CV.CV.CV.CVC',
              'CVC.CVC.CV.CVC.CVC', 'CV.CVCC.CV.CVC', 'CV.CVCC.CVC.CV', 'CVCC.CV.CVC.CV.CV.CV', 'CV.CVC.CV.CVC.CV.CV.CV', 'CV.CVC.CVC.CVC.CV', 'CV.CVC.CVC.CVC.CVC',
              'CV.CV.CV.CV.CV.CVC.CV', 'CV.CV.CVC.CV.CVC.CV', 'CV.CVC.CV.CVC.CV.CVC.CVC', 'CV.CV.CV.CVC.CV.CVC', 'CV.CV.CV.CVC.CV.CVC', 'CVC.CV.CV.CV.CVC.CV',
              'CV.CV.CV.CVC.CVCC', 'CVCC.CVC.CVC.CV', 'CV.CVC.CVC.CVC.CV.CVC', 'CV.CV.CV.CV.CV.CV.CV.CV', 'CVC.CVCC.CV.CV.CV', 'CVC.CV.CVC.CVC.CV',
              'CVC.CV.CVC.CVC.CV.CV.CV', 'CVC.CV.CVC.CV.CV.CVC', 'CVC.CVCC.CV.CV.CV', 'CV.CV.CVC.CV.CV.CVC', 'CVC.CVCC.CVC.CV.CV', 'CV.CV.CVC.CV.CV.CVC.CVC',
              'CV.CV.CV.CV.CV.CV.CVC', 'CV.CV.CVC.CV.CV.CV.CV', 'CV.CV.CVCC.CV.CV', 'CV.CVC.CV.CV.CV.CVC', 'CV.CV.CVC.CVC.CV.CV.CV', 'CVC.CVC.CVC.CV.CVC.CV',
              'CV.CVCC.CVC.CVCC', 'CVC.CV.CVC.CV.CVC.CVC', 'CVC.CV.CVC.CV.CVC.CVC', 'CVC.CV.CVC.CVCC', 'CVC.CV.CVC.CVCC', 'CVC.CVCC.CVC.CV', 'CV.CVC.CV.CVC.CV.CV',
              'CVC.CV.CV.CVCC.CVC.CV', 'CVC.CV.CV.CV.CV.CV.CV', 'CVC.CV.CV.CV.CVC.CV.CV', 'CV.CV.CV.CVC.CV.CVC.CV', 'CV.CV.CV.CVC.CV.CV.CV']
'''
V1 = ['a', 'e', 'i']
V2 = ['A', 'o', 'u']
V3 = ['a', 'A']
V4 = ['e', 'o']
V5 = ['i', 'u']
ensedadi = ["'", 'b', 'd', 'g', 'k', 'p', 'q', 't']
sayeshi = ['f', 'h', 's', 'v', 'x', 'z', 'S', 'Z']
ensayeshi = ['j', 'C']
resa = ['l', 'r', 'y', 'm', 'n']
#kenari = ['l']
#kheyshumi = ['m', 'n']
#larzeshi = ['r']
#ravan = ['y']

for row in cursor.fetchall():
    if len(row[0]) == 4:
        heja = ''
        div_counter = 1
        #print(row[0])
        for char_num in range(len(row[0])):
            if div_counter - char_num < len(row[0]):
                if row[0][char_num - div_counter] == 'w':
                    heja = 'W' + heja
                    div_counter += 2
                #elif row[0][char_num - div_counter] in consonants:
                    #heja = 'C' + heja
                    #word = row[0][char_num - div_counter] + word
                    #div_counter += 2
                elif row[0][char_num - div_counter] in vowels and row[0][char_num - (div_counter + 1)] in consonants:
                    heja = '.CV' + heja 
                    div_counter += 3
            else:
                break
        heja = heja[1:]
        if heja == 'CV.CV':
            list1.append(row[0])
print("size of CV.CV form in lexicon = ", len(list1))
#for i in list1:
    #print(i)
'''

list2 = []
list3 = []

list5 = []
#list6 = []

list4 = []
list7 = []

for cpl_num in range(len(list1)):
    
    if list1[cpl_num][1] == 'CVCC.CVCC':
        list2.append((list1[cpl_num][0][1], list1[cpl_num][0][5]))
    elif list1[cpl_num][1] == 'CVDCC.CVDCC':
        list2.append((list1[cpl_num][0][1:3], list1[cpl_num][0][6:8]))
    elif list1[cpl_num][1] == 'CVDCC.CVCC':
        list2.append((list1[cpl_num][0][1:3], list1[cpl_num][0][6]))
    elif list1[cpl_num][1] == 'CVCC.CVDCC':
        list2.append((list1[cpl_num][0][1], list1[cpl_num][0][5:7]))


        
    elif list1[cpl_num][1] == 'CVC.CVC':
        #print(list1[cpl_num])
        list3.append((list1[cpl_num][0][1], list1[cpl_num][0][4]))
    elif list1[cpl_num][1] == 'CVDC.CVDC':
        list3.append((list1[cpl_num][0][1:3], list1[cpl_num][0][5:7]))
    elif list1[cpl_num][1] == 'CVDC.CVC':
        list3.append((list1[cpl_num][0][1:3], list1[cpl_num][0][5]))
        #print(list1[cpl_num][0][1:3], list1[cpl_num][0][5])
    elif list1[cpl_num][1] == 'CVC.CVDC':
        list3.append((list1[cpl_num][0][1], list1[cpl_num][0][4:6]))



    if list1[cpl_num][1] == 'CV.CV':
        list4.append((list1[cpl_num][0][1], list1[cpl_num][0][3]))
        list7.append((list1[cpl_num][0]))
        #if list1[cpl_num][0][3] == ' ':  #sud#
            #print(list1[cpl_num][0])
    elif list1[cpl_num][1] == 'CVD.CVD':
        list4.append((list1[cpl_num][0][1:3], list1[cpl_num][0][4:]))
        list7.append((list1[cpl_num][0]))
    elif list1[cpl_num][1] == 'CVD.CV':
        list4.append((list1[cpl_num][0][1:3], list1[cpl_num][0][4]))
        list7.append((list1[cpl_num][0]))
    elif list1[cpl_num][1] == 'CV.CVD':
        list4.append((list1[cpl_num][0][1], list1[cpl_num][0][3:]))
        list7.append((list1[cpl_num][0]))


    elif list1[cpl_num][1] == 'CV.CVC':
        list5.append((list1[cpl_num][0][1], list1[cpl_num][0][3]))
        if list1[cpl_num][0][3] in consonants:
            print(list1[cpl_num][0])
    elif list1[cpl_num][1] == 'CVD.CVDC':
        list5.append((list1[cpl_num][0][1:3], list1[cpl_num][0][4:6]))
    elif list1[cpl_num][1] == 'CVD.CVC':
        list5.append((list1[cpl_num][0][1:3], list1[cpl_num][0][4]))
    elif list1[cpl_num][1] == 'CV.CVDC':
        list5.append((list1[cpl_num][0][1], list1[cpl_num][0][3:5]))


    elif list1[cpl_num][1] == 'CV.CVCC':
        list5.append((list1[cpl_num][0][1], list1[cpl_num][0][3]))
        if list1[cpl_num][0][3] in consonants:
            print(list1[cpl_num][0])
    elif list1[cpl_num][1] == 'CVD.CVDC':
        list5.append((list1[cpl_num][0][1:3], list1[cpl_num][0][4:6]))
    elif list1[cpl_num][1] == 'CVD.CVC':
        list5.append((list1[cpl_num][0][1:3], list1[cpl_num][0][4]))
    elif list1[cpl_num][1] == 'CV.CVDC':
        list5.append((list1[cpl_num][0][1], list1[cpl_num][0][3:5]))

       
#print("size of 'CVCC.CVCC' paterns = ", len(list2))
#print("size of 'CVC.CVC' paterns = ", len(list3))
print("size of 'CV.CV' paterns = ", len(list4))
#print("size of 'CV.CVC' paterns = ", len(list5))
'''

list8 = []
for word in list1:
    category_word = ''
    for char in word:
        if char in ensedadi:
            category_word = category_word + 'C1'
        elif char in sayeshi:
            category_word = category_word + 'C2'
        elif char in ensayeshi:
            category_word = category_word + 'C3'
        elif char in resa:
            category_word = category_word + 'C4'
        
        elif char in V3:
            category_word = category_word + 'V3'
        elif char in V4:
            category_word = category_word + 'V4'
        elif char in V5:
            category_word = category_word + 'V5'
        else:
            #print(word)
            continue
    list8.append(category_word)
#for i in list8:
    #print(i)
#print(len(list8))
    
for word in list1:  ### ba in kar har kalame 2 bar dar list8 neveshte mishavad
    category_word = ''
    for char in word:
        if char in ensedadi:
            category_word = category_word + 'C1'
        elif char in sayeshi:
            category_word = category_word + 'C2'
        elif char in ensayeshi:
            category_word = category_word + 'C3'
        elif char in resa:
            category_word = category_word + 'C4'
        
        elif char in V1:
            category_word = category_word + 'V1'
        elif char in V2:
            category_word = category_word + 'V2'
        else:
            #print(word)   ### word = 'Ace
            continue
       
    list8.append(category_word)

dict1={}
for cat in list8:
    try:
        dict1[cat] += 1
    except:
        dict1[cat] = 1
#print(len(list8))
#print(len(dict1))
        
#print('size of tarkib types: ', len(list8) / 2) ### mafhoome ghalat

first_sylb = []
second_sylb = []
list_of_consonants = []
list_of_vowels = []
dict3 = {}
for cat in list8:
    if len(cat) == 8:
        first_sylb.append(str(cat[:4]))
        second_sylb.append(str(cat[4:]))
        list_of_consonants.append(str(cat[:2])+str(cat[4:6]))
        list_of_vowels.append(str(cat[2:4])+str(cat[6:]))
        try:
            dict3[cat] += 1
        except:
            dict3[cat] = 1
#print(len(dict3))
dict3 = collections.Counter(dict3)
print('most common tarkib CV.CV: ', dict3.most_common(1))


dict1 = {}
dict2 = {}
dict4 = {}
dict5 = {}
'''
list_of_2_heja = []
for h1 in range(len(first_sylb)): 
    if  (first_sylb[h1], second_sylb[h1]) not in list_of_2_heja:
        list_of_2_heja.append((first_sylb[h1], second_sylb[h1]))
#print(len(list_of_2_heja))
'''        
for heja in first_sylb:
    #print(i)
    try:
        dict1[heja] += 1
    except:
        dict1[heja] = 1

for heja in second_sylb:
    try:
        dict2[heja] += 1
    except:
        dict2[heja] = 1

for Cs in list_of_consonants:
    #print(i)
    try:
        dict4[Cs] += 1
    except:
        dict4[Cs] = 1

for Vs in list_of_vowels:
    #print(i)
    try:
        dict5[Vs] += 1
    except:
        dict5[Vs] = 1
        

for i in dict1.items():
    print('In first syllable : ' + '\t', i)
dict1 = collections.Counter(dict1)
print('most common tarkib in first sylable: ', dict1.most_common(1))

print()
for i in dict2.items():
    print('In second syllable : ' + '\t', i)
dict2 = collections.Counter(dict2)
print('most common tarkib in second sylable: ', dict2.most_common(1))

dict4 = collections.Counter(dict4)
print('most common Cs in CV.CV: ', dict4.most_common(1), '*** Divide numer by 2')

dict5 = collections.Counter(dict5)
print('most common Vs in CV.CV: ', dict5.most_common(1))
print()
'''
print(len(dict3), "different syllable formation.")
#print(len(dict1))
#print(len(dict2))
#j = 0
for i in dict3.keys():
    print(i[:4], '.', i[4:], ': ', dict3[i])
    #j = j + dict3[i]
    #print()
#print(j)
#print(len(dict1))
'''

#gaps in first heja, second heja, consonants, vowels:
list_of_gaps1 = []
list_of_gaps2 = []
for C in ['C1', 'C2', 'C3', 'C4']:
    for V in ['V1', 'V2', 'V3', 'V4', 'V5']:
        if C+V not in dict1.keys():
            list_of_gaps1.append(C+V)
        if C+V not in dict2.keys():
            list_of_gaps2.append(C+V)
print('list of gaps in first sylable of CV.CV: ', len(list_of_gaps1))
print('list of gaps in second sylable of CV.CV: ', len(list_of_gaps2))

list_of_gaps_cons = []
for C1 in ['C1', 'C2', 'C3', 'C4']:
    for C2 in ['C1', 'C2', 'C3', 'C4']:
        if C1+C2 not in list_of_consonants:
            list_of_gaps_cons.append(C1+','+C2)
print('list of gaps in consonants CV.CV: ', len(list_of_gaps_cons))

list_of_gaps_vows = []
for V1 in ['V1', 'V2']:
    for V2 in ['V1', 'V2']:
        if V1+V2 not in list_of_vowels:
            list_of_gaps_vows.append(V1+','+V2)
            
for V1 in ['V3', 'V4', 'V5']:
    for V2 in ['V3', 'V4', 'V5']:
        if V1+V2 not in list_of_vowels:
            list_of_gaps_vows.append(V1+','+V2)
print('list of gaps in vowels CV.CV: ', len(list_of_gaps_vows))
for i in list_of_gaps_vows:
    print(i)
print()
'''
if list_of_gaps1 == []:
    print('There is no gap in the first sylable of CV.CV: ')
else:
    for i in list_of_gaps1:
        print(i)
print()        


if list_of_gaps2 == []:
    print('There is no gap in the second sylable of CV.CV: ')
else:
    for i in list_of_gaps2:
        print(i)

print()

list_of_gaps = []
for first in dict1.keys():
    for second in dict2.keys():
        if first + second not in dict3.keys():
            list_of_gaps.append(first + second)

if list_of_gaps == []:
    print('There is no gap in CV.CV: ')
else:
    for i in list_of_gaps:
        print(i)

print('all: ', len(dict1) * len(dict2))
print('gaps: ', len(list_of_gaps))
print('exists: ', len(dict3))
'''
conn.close()
