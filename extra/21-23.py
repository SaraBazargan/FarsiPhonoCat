
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
                #if row[0][char_num - div_counter] == 'w':
                    #heja = 'W' + heja
                    #div_counter += 2
                #elif row[0][char_num - div_counter] in consonants:
                    #heja = 'C' + heja
                    #word = row[0][char_num - div_counter] + word
                    #div_counter += 2
                if row[0][char_num - div_counter] in vowels and row[0][char_num - (div_counter + 1)] in consonants:
                    heja = '.CV' + heja 
                    div_counter += 3
                else:
                    break
        #heja = heja[1:]
        if heja == '.CV.CV':
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
    list8.append((word,category_word))
#for i in list8:
    #print(i)
#print(len(list8))

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
        
        elif char in V1:
            category_word = category_word + 'V1'
        elif char in V2:
            category_word = category_word + 'V2'
        else:
            #print(word)
            continue
       
    list8.append((word, category_word))
print('size of tarkib types: ', len(list8) / 2)

first_sylb = []
second_sylb = []
list_of_consonants = []
list_of_vowels = []
dict3 = {}
for cat in list8:
    #print(cat)
    if len(cat[0]) == 4:
        first_sylb.append((str(cat[0][:2]), str(cat[1][:4])))
        #print((str(cat[0][:2]), str(cat[1][:4])))
        second_sylb.append((str(cat[0][2:]), str(cat[1][4:])))
        list_of_consonants.append((str(cat[0][0])+str(cat[0][2]), str(cat[1][:2])+str(cat[1][4:6])))
        list_of_vowels.append((str(cat[0][1])+str(cat[0][3]), str(cat[1][2:4])+str(cat[1][6:])))
        try:
            dict3[cat[1]] += 1
        except:
            dict3[cat[1]] = 1
        
#print(len(dict3))
#for i in list8:
   # print(i)
dict3 = collections.Counter(dict3)
print('most common tarkib CV.CV: ', dict3.most_common(1))

after_a_vowel = {}
after_e_vowel = {}
after_o_vowel = {}
after_A_vowel = {}
after_i_vowel = {}
after_u_vowel = {}
for i in range(len(list1)):
    if list1[i][1] == 'a':
        try:
            after_a_vowel[list1[i][3]] += 1
        except:
            after_a_vowel[list1[i][3]] = 1
    elif list1[i][1] == 'e':
        try:
            after_e_vowel[list1[i][3]] += 1
        except:
            after_e_vowel[list1[i][3]] = 1
    elif list1[i][1] == 'o':
        try:
            after_o_vowel[list1[i][3]] += 1
        except:
            after_o_vowel[list1[i][3]] = 1
    elif list1[i][1] == 'A':
        try:
            after_A_vowel[list1[i][3]] += 1
        except:
            after_A_vowel[list1[i][3]] = 1
    elif list1[i][1] == 'i':
        try:
            after_i_vowel[list1[i][3]] += 1
        except:
            after_i_vowel[list1[i][3]] = 1
    elif list1[i][1] == 'u':
        try:
            after_u_vowel[list1[i][3]] += 1
        except:
            after_u_vowel[list1[i][3]] = 1
print('after a, ', after_a_vowel.items())
print('after e, ', after_e_vowel.items())
print('after o, ', after_o_vowel.items())
print('after A, ', after_A_vowel.items())
print('after i, ', after_i_vowel.items())
print('after u, ', after_u_vowel.items())
print()

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
    #print(heja)
    try:
        dict1[heja[1]] += 1
    except:
        dict1[heja[1]] = 1

for heja in second_sylb:
    try:
        dict2[heja[1]] += 1
    except:
        dict2[heja[1]] = 1

for Cs in list_of_consonants:
    #print(Cs)
    try:
        dict4[Cs[1]] += 1
    except:
        dict4[Cs[1]] = 1

for Vs in list_of_vowels:
    #print(Vs)
    try:
        dict5[Vs[1]] += 1
    except:
        dict5[Vs[1]] = 1


after_a = {}
after_e = {}
after_o = {}
after_A = {}
after_i = {}
after_u = {}
for i in range(len(list_of_vowels)):
    #print(list_of_vowels[i])
    if list_of_vowels[i][0][0] == 'a':
        try:
            after_a[list_of_vowels[i][1][2:]] += 1
        except:
            after_a[list_of_vowels[i][1][2:]] = 1
    elif list_of_vowels[i][0][0] == 'e':
        try:
            after_e[list_of_vowels[i][1][2:]] += 1
        except:
            after_e[list_of_vowels[i][1][2:]] = 1
    elif list_of_vowels[i][0][0] == 'o':
        try:
            after_o[list_of_vowels[i][1][2:]] += 1
        except:
            after_o[list_of_vowels[i][1][2:]] = 1
    elif list_of_vowels[i][0][0] == 'A':
        try:
            after_A[list_of_vowels[i][1][2:]] += 1
        except:
            after_A[list_of_vowels[i][1][2:]] = 1
    elif list_of_vowels[i][0][0] == 'i':
        try:
            after_i[list_of_vowels[i][1][2:]] += 1
        except:
            after_i[list_of_vowels[i][1][2:]] = 1
    elif list_of_vowels[i][0][0] == 'u':
        try:
            after_u[list_of_vowels[i][1][2:]] += 1
        except:
            after_u[list_of_vowels[i][1][2:]] = 1
t1 = 0
t2 = 0
t3 = 0
t4 = 0
t5 = 0
t6 = 0
for v in after_a.values():
    t1 += v
for v in after_e.values():
    t2 += v
for v in after_o.values():
    t3 += v
for v in after_A.values():
    t4 += v
for v in after_i.values():
    t5 += v
for v in after_u.values():
    t6 += v
print('after a, ', after_a.items(), ' / ', t1/2)
print('after e, ', after_e.items(), ' / ', t2/2)
print('after o, ', after_o.items(), ' / ', t3/2)
print('after A, ', after_A.items(), ' / ', t4/2)
print('after i, ', after_i.items(), ' / ', t5/2)
print('after u, ', after_u.items(), ' / ', t6/2)

       

#for i in dict1.items():
    #print('In first syllable : ' + '\t', i)
dict1 = collections.Counter(dict1)
print('most common tarkib in first sylable: ', dict1.most_common(1))

print()
#for i in dict2.items():
    #print('In second syllable : ' + '\t', i)
dict2 = collections.Counter(dict2)
print('most common tarkib in second sylable: ', dict2.most_common(1))

dict4 = collections.Counter(dict4)
print('most common Cs in CV.CV: ', dict4.most_common(1), ' divide by 2')

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
        if C1+C2 not in dict4.keys():
            list_of_gaps_cons.append(C1+','+C2)
print('list of gaps in consonants CV.CV: ', len(list_of_gaps_cons))


list_of_gaps_vows = []
for V1 in ['V1', 'V2']:
    for V2 in ['V1', 'V2']:
        if V1+V2 not in dict5.keys():
            list_of_gaps_vows.append(V1+','+V2)
            
for V1 in ['V3', 'V4', 'V5']:
    for V2 in ['V3', 'V4', 'V5']:
        if V1+V2 not in dict5.keys():
            list_of_gaps_vows.append(V1+','+V2)
print('list of gaps in vowels CV.CV: ', len(list_of_gaps_vows))
#print('gaps:')
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
