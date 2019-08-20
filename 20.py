

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
V2 = ['A', 'o', 'u', 'ow']
V3 = ['a', 'A']
V4 = ['e', 'o', 'ow']
V5 = ['i', 'u']
ensedadi = ["'", 'b', 'd', 'g', 'k', 'p', 'q', 't']
sayeshi = ['f', 'h', 's', 'v', 'x', 'z', 'S', 'Z']
ensayeshi = ['j', 'C']
kenari = ['l']
kheyshumi = ['m', 'n']
larzeshi = ['r']
ravan = ['y']

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

'''
for i in list1:
    if i[1] not in heja_kinds and 'D' not in i[1]:
        print(i)


list2 = []
list3 = []

list5 = []
#list6 = []
'''
list4 = []
list7 = []
count = 0
for cpl_num in range(len(list1)):
    '''
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
    '''

    
    if list1[cpl_num][1] == 'CV.CV':
        count += 1
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
'''

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

'''        
#print("size of 'CVCC.CVCC' paterns = ", len(list2))
#print("size of 'CVC.CVC' paterns = ", len(list3))
print("size of 'CV.CV' paterns with diphtounges = ", len(list7))
print("size of 'CV.CV' paterns without diphtounges of 'w'= ", count)
#print("size of 'CV.CVC' paterns = ", len(list5))

list8 = []
for word in list7:
    category_word = ''
    for char in word:
        if char in ensedadi:
            category_word = category_word + 'C1'
        elif char in sayeshi:
            category_word = category_word + 'C2'
        elif char in ensayeshi:
            category_word = category_word + 'C3'
        elif char in kenari:
            category_word = category_word + 'C4'
        elif char in kheyshumi:
            category_word = category_word + 'C5'
        elif char in larzeshi:
            category_word = category_word + 'C6'
        elif char in ravan:
            category_word = category_word + 'C7'
        elif char in V1:
            category_word = category_word + 'V1'
        elif char in V2:
            category_word = category_word + 'V2'
        #elif char in V3:
            #category_word = category_word + 'V3'
    list8.append(category_word)
    
dict1={}
for cat in list8:
    try:
        dict1[cat] += 1
    except:
        dict1[cat] = 1
        
#for k, v in dict1.items():
   # print(k, v)

    
'''
second_vowel_1 = {}
for couple in list2:
    
    if couple[0] == 'a':
        try:
            second_vowel_1[(couple[0], couple[1])] += 1
        except:
            second_vowel_1[(couple[0], couple[1])] = 1
            
    elif couple[0] == 'e':
        try:
            second_vowel_1[(couple[0], couple[1])] += 1
        except:
            second_vowel_1[(couple[0], couple[1])] = 1
            
    elif couple[0] == 'o' or couple[0] == 'ow':
        try:
            second_vowel_1[(couple[0], couple[1])] += 1
        except:
            second_vowel_1[(couple[0], couple[1])] = 1
    
    elif couple[0] == 'A':
        try:
            second_vowel_1[(couple[0], couple[1])] += 1
        except:
            second_vowel_1[(couple[0], couple[1])] = 1
    
    elif couple[0] == 'i':
        try:
            second_vowel_1[(couple[0], couple[1])] += 1
        except:
            second_vowel_1[(couple[0], couple[1])] = 1
    
    elif couple[0] == 'u':
        try:
            second_vowel_1[(couple[0], couple[1])] += 1
        except:
            second_vowel_1[(couple[0], couple[1])] = 1
    

for i in second_vowel_1.items():
    print(i)

n = 0            
for i in second_vowel.values():
    n = n + i
print(n)
       



second_vowel_2 = {}
for couple in list3:
    if couple[0] == 'a':
        try:
            second_vowel_2[(couple[0], couple[1])] += 1
        except:
            second_vowel_2[(couple[0], couple[1])] = 1
           
    elif couple[0] == 'e':
        try:
            second_vowel_2[(couple[0], couple[1])] += 1
        except:
            second_vowel_2[(couple[0], couple[1])]= 1
            
    elif couple[0] == 'o' or couple[0] == 'ow':
        try:
            second_vowel_2[(couple[0], couple[1])] += 1
        except:
            second_vowel_2[(couple[0], couple[1])] = 1
    
    elif couple[0] == 'A':
        try:
            second_vowel_2[(couple[0], couple[1])] += 1
        except:
            second_vowel_2[(couple[0], couple[1])] = 1
    
    elif couple[0] == 'i':
        try:
            second_vowel_2[(couple[0], couple[1])] += 1
        except:
            second_vowel_2[(couple[0], couple[1])] = 1
    
    elif couple[0] == 'u':
        try:
            second_vowel_2[(couple[0], couple[1])] += 1
        except:
            second_vowel_2[(couple[0], couple[1])] = 1


print()
for i in second_vowel_2.items():
    print(i)

   
n = 0            
for i in second_vowel_2.values():
    n = n + i
print("size of 'CVC.CVC' paterns = ", n)    
'''



second_vowel_3 = {}
for couple in list4:
    if couple[0] == 'a':
        try:
            second_vowel_3[(couple[0], couple[1])] += 1
        except:
            second_vowel_3[(couple[0], couple[1])] = 1
           
    elif couple[0] == 'e':
        try:
            second_vowel_3[(couple[0], couple[1])] += 1
        except:
            second_vowel_3[(couple[0], couple[1])]= 1
            
    elif couple[0] == 'o' or couple[0] == 'ow':
        try:
            second_vowel_3[(couple[0], couple[1])] += 1
        except:
            second_vowel_3[(couple[0], couple[1])] = 1
    
    elif couple[0] == 'A':
        try:
            second_vowel_3[(couple[0], couple[1])] += 1
        except:
            second_vowel_3[(couple[0], couple[1])] = 1
    
    elif couple[0] == 'i':
        try:
            second_vowel_3[(couple[0], couple[1])] += 1
        except:
            second_vowel_3[(couple[0], couple[1])] = 1
    
    elif couple[0] == 'u':
        try:
            second_vowel_3[(couple[0], couple[1])] += 1
        except:
            second_vowel_3[(couple[0], couple[1])] = 1

#for k,v in second_vowel_3.items():
    #print(k,v)
'''

print()
for i in second_vowel_3.items():
    print(i)   



second_vowel_4 = {}
for couple in list5:
    if couple[0] == 'a':
        try:
            second_vowel_4[(couple[0], couple[1])] += 1
        except:
            second_vowel_4[(couple[0], couple[1])] = 1
           
    elif couple[0] == 'e':
        try:
            second_vowel_4[(couple[0], couple[1])] += 1
        except:
            second_vowel_4[(couple[0], couple[1])]= 1
            
    elif couple[0] == 'o' or couple[0] == 'ow':
        try:
            second_vowel_4[(couple[0], couple[1])] += 1
        except:
            second_vowel_4[(couple[0], couple[1])] = 1
    
    elif couple[0] == 'A':
        try:
            second_vowel_4[(couple[0], couple[1])] += 1
        except:
            second_vowel_4[(couple[0], couple[1])] = 1
    
    elif couple[0] == 'i':
        try:
            second_vowel_4[(couple[0], couple[1])] += 1
        except:
            second_vowel_4[(couple[0], couple[1])] = 1
    
    elif couple[0] == 'u':
        try:
            second_vowel_4[(couple[0], couple[1])] += 1
        except:
            second_vowel_4[(couple[0], couple[1])] = 1


print()
for i in second_vowel_4.items():
    print(i)   

'''

conn.close()
