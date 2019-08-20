

import pyodbc
DBfile = 'd:\\Flexicon.mdb'
conn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb)};DBQ='+DBfile)
cursor = conn.cursor()
cursor.execute("SELECT PhonologicalForm FROM Entries")
	
list1 = []
dic1 = {}
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

fp = open('diphtangue.txt', 'w')  ### in file ra bareye neveshtane diphtounge ha iijad mikonim
for row in cursor.fetchall():
    heja = ''   ### motaghayyer baraye neveshtan heja negariye kalame
    div_counter = 1  ### in motaghayyer ra bareye shomaresh az entehaye kalame tarif mikonim
    #print(row[0])
    for char_num in range(len(row[0])):
        if div_counter - char_num < len(row[0]):
            #if row[0][char_num - div_counter] == 'w':  ### tafigh mikonim ta shomarende az aakhare kalame be ebtedaye aan pish beravad
                #fp.write(row[0])   ### diphtounge haye daraye w ra dar yek file minevisam
                #fp.write('\n')
                #heja = 'D' + heja
                #div_counter += 2
            if row[0][char_num - div_counter] in consonants:
                heja = 'C' + heja
                div_counter += 2
            elif row[0][char_num - div_counter] in vowels and row[0][char_num - (div_counter + 1)] in consonants:
                heja = '.CV' + heja
                div_counter += 3
            #else:
                #heja = 'NNone' ### chon badan character avval ra hazf mikonim do ta N neveshtam
            else:
                heja = ''
                fp.write(row[0])
                fp.write('\n')
                break
    #heja = heja[1:]  ### chon ebtedaye heja yek noghte ezafii dara aan ra hazf mikonim
    if len(heja) != 0:
        if heja[0] == '.':
            list1.append((row[0], heja))
            dic1[row[0]] = heja
            #print(row[0], heja)
        else: ### diphtounge haye gheire w ra be file ezafe mikonim
            fp.write(row[0])
            fp.write('\n')
fp.close()
print("size of lexicon = ", len(list1))
print("size of lexicon without repeated words = ", len(dic1))
fp1 = open('diphtangue.txt', 'r')
print("size of diphtangues = ", len(fp1.readlines()))
fp1.close()
### tedade do hejayiha ba saakhtaare CV.CV
list2 = []
for key in dic1.keys():
    if dic1[key] == '.CV.CV':
        list2.append(dic1[key])
print('size of CV.CV without repeated words = ', len(list2))

'''
tak_heja = ['CV', 'CVC']
list2 = []
for couple in range(len(list1)):
    if list1[couple][1] in tak_heja:
        list2.append(list1[couple][0])
print(len(list2))
    
i = 0
list4 = []
list5 = []
for heja in list1:
    if heja[1] == 'CVCC':
        if heja[0][:-1] not in list2:
            list4.append(heja[0])
    i += 1
       
for i in list4:
    index = list4.index(i)
    if i[:-2] not in list2:
        list5.append(i)
        list4.pop(index)
  
print(len(list4))
#print('words with CVCC formation that could drop their final consonant: ', )        
#print(list4)


print()
print()
print('words with CVCC formation that could drop both final consonants: ', )
print()
print(list5)
'''        
conn.close()
