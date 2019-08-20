

import pyodbc
DBfile = 'd:\\Flexicon.mdb'
conn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb)};DBQ='+DBfile)
cursor = conn.cursor()
cursor.execute("SELECT PhonologicalForm FROM Entries")

do_hejayiha = ['CV.CV', 'CV.CVC', 'CV.CVCC', 'CVC.CV', 'CVCC.CV', 'CVC.CVC', 'CVC.CVCC', 'CVCC.CVC', 'CVCC.CVCC']	

consonants = ["'", 'b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z', 'C', 'S', 'Z', 'y']
vowels = ['A', 'i', 'u', 'a', 'e', 'o']

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
lexicon_size = 0
list1 = [[] for i in range(len(do_hejayiha))]
fp = open('diphtangue_and_errors.txt', 'w')  ### in file ra bareye neveshtane diphtounge ha iijad mikonim
for row in cursor.fetchall():
    heja = ''
    div_counter = 1
    #print(row[0])
    for char_num in range(len(row[0])):
        if div_counter - char_num < len(row[0]):
            #if row[0][char_num - div_counter] == 'w':
                #fp.write(row[0])   ### diphtounge haye daraye w ra dar yek file minevisam
                #fp.write('\n')
                #heja = 'W' + heja
                #div_counter += 2
            if row[0][char_num - div_counter] in consonants:
                heja = 'C' + heja
                #word = row[0][char_num - div_counter] + word
                div_counter += 2
            elif row[0][char_num - div_counter] in vowels and row[0][char_num - (div_counter + 1)] in consonants:
                heja = '.CV' + heja 
                div_counter += 3
            else:
                heja = ''
                fp.write(row[0])
                fp.write('\n')
                break
        
    #print(row[0], heja)
    if len(heja) != 0:
        if heja[0] == '.':
            #print(heja)
            lexicon_size += 1
        else:
            fp.write(row[0])
            fp.write('\n')

            
        if heja == '.CV.CV':
            list1[0].append(row[0])
        elif heja == '.CV.CVC':
            list1[1].append(row[0])
        elif heja == '.CV.CVCC':
            list1[2].append(row[0])
        elif heja == '.CVC.CV':
            list1[3].append(row[0])
        elif heja == '.CVCC.CV':
            list1[4].append(row[0])
        elif heja == '.CVC.CVC':
            list1[5].append(row[0])
        elif heja == '.CVC.CVCC':
            list1[6].append(row[0])
        elif heja == '.CVCC.CVC':
            list1[7].append(row[0])
        elif heja == '.CVCC.CVCC':
            list1[8].append(row[0])
        
    #else:
        #print(row[0])
#for i in list1:
    #print(len(i))
fp.close()
print("size of lexicon = ", lexicon_size)        


def catrgories_in_heja(lst):   
    list8 = []
    for word in lst:
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
        list8.append(category_word)
    

    for word in lst:
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
        list8.append(category_word)
    return(list8)


def list_to_dict(slb, heja_kind):
    ''' convert the list of category_taged_heja to dict in order to find the frequencyies
    '''
    dict1 = {}
    if "." in heja_kind: ### for tarkibe hejaii
        length = (len(heja_kind)- 1) * 2
    else:   ### for tak heja
        length = len(heja_kind) * 2
    for heja in slb:
        if len(heja) == length:
            try:
                dict1[heja] += 1
            except:
                dict1[heja] = 1
    return(dict1)


def separate(lst8, heja_kind):
    ''' separates the syllables of category_taged_heja
    '''
    separation_point = heja_kind.index('.')
    #print('separation_point: ', separation_point)
    first_sylb = []
    second_sylb = []
    list_of_above_lists = []
    for cat in lst8:
        #print(cat)
        #print(cat[:int(separation_point) * 2])
        if len(cat) == (len(heja_kind) - 1) * 2:
            first_sylb.append(str(cat[:int(separation_point) * 2]))
            second_sylb.append(str(cat[int(separation_point) * 2:]))
            #print(str(cat[:int(separation_point) * 2]))
            #print(str(cat[int(separation_point) * 2:]))
    #print(len(lst8))
    #print(len(first_sylb))
    #print(len(first_sylb))
    list_of_above_lists.append(first_sylb)
    list_of_above_lists.append(second_sylb)
    return(list_of_above_lists)
            

'''
for i in l_to_d1.items():
    print('In first syllable : ' + '\t', i)
print()
for i in l_to_d2.items():
    print('In second syllable : ' + '\t', i)
print()
'''        


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


def segment_gaps(dictionary, heja_kind):
    list_of_gaps = []
    n = 0
    if heja_kind == 'CV':
        #print('list of gaps in first sylable of CV.CV: ')
        for C in ['C1', 'C2', 'C3', 'C4']:
            for V in ['V1', 'V2', 'V3', 'V4', 'V5']:
                n += 1
                if C+V not in dictionary.keys():
                    list_of_gaps.append(C+V)
    elif heja_kind == 'CVC':
        for C1 in ['C1', 'C2', 'C3', 'C4']:
            for V in ['V1', 'V2', 'V3', 'V4', 'V5']:
                for C2 in ['C1', 'C2', 'C3', 'C4']:
                    n += 1
                    if C1+V+C2 not in dictionary.keys():
                        list_of_gaps.append(C1+V+C2)
    elif heja_kind == 'CVCC':
        for C1 in ['C1', 'C2', 'C3', 'C4']:
            for V in ['V1', 'V2', 'V3', 'V4', 'V5']:
                for C2 in ['C1', 'C2', 'C3', 'C4']:
                    for C3 in ['C1', 'C2', 'C3', 'C4']:
                        n += 1
                        if C1+V+C2+C3 not in dictionary.keys():
                            list_of_gaps.append(C1+V+C2+C3)
    print("number of all possible segments: ", n)
    return(list_of_gaps)

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
'''

def tarkib_gaps(list_2_dict1, list_2_dict2, dictionary):
    list_of_gaps = []
    for first in list_2_dict1.keys():
        for second in list_2_dict2.keys():
            if first + second not in dictionary.keys():
                list_of_gaps.append(first + second)
    return(list_of_gaps)



def existed_categories_Cs(heja, C1VC_C, C2VC_C, C3VC_C, C4VC_C):
    #if len(heja) == 6:
    if heja[1] == '1':
        if heja[2:] not in C1VC_C:
            C1VC_C.append(heja[2:])
        #if heja[4:] not in C1VC_C[1]:
            #C1VC_C[1].append(heja[4:])
    elif heja[1] == '2':
        if heja[2:] not in C2VC_C:
            C2VC_C.append(heja[2:])
        #if heja[4:] not in C2VC_C[1]:
            #C2VC_C[1].append(heja[4:])
    elif heja[1] == '3':
        if heja[2:] not in C3VC_C:
            C3VC_C.append(heja[2:])
        #if heja[4:] not in C3VC_C[1]:
            #C3VC_C[1].append(heja[4:])
    else:
        if heja[2:] not in C4VC_C:
            C4VC_C.append(heja[2:])
        #if heja[4:] not in C4VC_C[1]:
            #C4VC_C[1].append(heja[4:])

def existed_categories_Vs(semi_heja, V1C_C, V2C_C, V3C_C, V4C_C, V5C_C):
    if semi_heja[1] == '1':
        if semi_heja[2:] not in V1C_C:
            V1C_C.append(semi_heja[2:])
    elif semi_heja[1] == '2':
        if semi_heja[2:] not in V2C_C:
            V2C_C.append(semi_heja[2:])
    elif semi_heja[1] == '3':
        if semi_heja[2:] not in V3C_C:
            V3C_C.append(semi_heja[2:])
    elif semi_heja[1] == '4':
        if semi_heja[2:] not in V4C_C:
            V4C_C.append(semi_heja[2:])
    elif semi_heja[1] == '5':
        if semi_heja[2:] not in V5C_C:
            V5C_C.append(semi_heja[2:])
'''
    elif len(heja) == 8:
        if heja[1] == '1':
            if heja[2:] not in C1VC_C:
                C1VC_C.append(heja[2:])
            #if heja[4:6] not in C1VC_C[1]:
                #C1VC_C[1].append(heja[4:6])
            #if heja[6:] not in C1VC_C[2]:
                #C1VC_C[2].append(heja[6:])
        elif heja[1] == '2':
            if heja[2:] not in C2VC_C:
                C2VC_C.append(heja[2:])
            #if heja[4:6] not in C2VC_C[1]:
                #C2VC_C[1].append(heja[4:6])
            #if heja[6:] not in C2VC_C[2]:
                #C2VC_C[2].append(heja[6:])
        elif heja[1] == '3':
            if heja[2:] not in C3VC_C:
                C3VC_C.append(heja[2:])
            #if heja[4:6] not in C3VC_C[1]:
                #C3VC_C[1].append(heja[4:6])
            #if heja[6:] not in C3VC_C[2]:
                #C3VC_C[2].append(heja[6:])
        else:
            if heja[2:] not in C4VC_C:
                C4VC_C.append(heja[2:])
            #if heja[4:6] not in C4VC_C[1]:
                #C4VC_C[1].append(heja[4:6])
            #if heja[6:] not in C4VC_C[2]:
                #C4VC_C[2].append(heja[6:])
    
'''        




for i in range(len(do_hejayiha)):
    words = list1[i]
    print("size of " + do_hejayiha[i] + " form in lexicon = ", len(list1[i]))
    print()
    category_taged_heja = catrgories_in_heja(words)
    #print(category_taged_heja)
    #print(len(category_taged_heja))
    list_of_lists = separate(category_taged_heja, do_hejayiha[i])
    #print('list_of_lists: ', len(list_of_lists))
    #for i in list_of_lists:
        #print(i)
    ##### the following three lines: convert the list of category_taged_heja and each syllabeles to dict in order to find the frequencies
    dict1 = list_to_dict(category_taged_heja, do_hejayiha[i])
    l_to_d1 = list_to_dict(list_of_lists[0], do_hejayiha[i].split('.')[0])
    l_to_d2 = list_to_dict(list_of_lists[1], do_hejayiha[i].split('.')[1])
    #gaps in first heja:
    list_of_sylabs = do_hejayiha[i].split('.')
    
    print("list of exists in first syllable: ")
    if len(list_of_sylabs[0]) >= 2:
        C1VC_C = [] 
        C2VC_C = [] 
        C3VC_C = [] 
        C4VC_C = [] 
        for x in l_to_d1.keys():
            existed_categories_Cs(x, C1VC_C, C2VC_C, C3VC_C, C4VC_C)
        if len(C1VC_C[1]) >= 4:
            V1C_C = []
            V2C_C = []
            V3C_C = []
            V4C_C = []
            V5C_C = []
            for j in C1VC_C:
                existed_categories_Vs(j, V1C_C, V2C_C, V3C_C, V4C_C, V5C_C)
            #print(len(V4C_C))
            for k in C2VC_C:
                existed_categories_Vs(k, V1C_C, V2C_C, V3C_C, V4C_C, V5C_C)
            #print(len(V4C_C))
            for m in C3VC_C:
                existed_categories_Vs(m, V1C_C, V2C_C, V3C_C, V4C_C, V5C_C)
            #print(len(V4C_C))
            for n in C4VC_C:
                existed_categories_Vs(n, V1C_C, V2C_C, V3C_C, V4C_C, V5C_C)
            #print(len(V4C_C))
            
            if len(V1C_C[1]) == 4:
                C1_C = []
                C2_C = []
                C3_C = []
                C4_C = []
                for p in V1C_C:
                    existed_categories_Cs(p, C1_C, C2_C, C3_C, C4_C)
                for q in V2C_C:
                    existed_categories_Cs(q, C1_C, C2_C, C3_C, C4_C)
                for r in V3C_C:
                    existed_categories_Cs(r, C1_C, C2_C, C3_C, C4_C)
                for s in V4C_C:
                    existed_categories_Cs(s, C1_C, C2_C, C3_C, C4_C)
                for t in V5C_C:
                    existed_categories_Cs(t, C1_C, C2_C, C3_C, C4_C)

                
        print('C1 ', C1VC_C)
        print()
        print('C2 ', C2VC_C)
        print()
        print('C3 ', C3VC_C)
        print()
        print('C4 ', C4VC_C)
        print()
        if len(C1VC_C[1]) >= 4:
            print('V1 ', V1C_C)
            print()
            print('V2 ', V2C_C)
            print()
            print('V3 ', V3C_C)
            print()
            print('V4 ', V4C_C)
            print()
            print('V5 ', V5C_C)
            print()
            if len(V1C_C[1]) == 4:
                print('C1 ', C1_C)
                print()
                print('C2 ', C2_C)
                print()
                print('C3 ', C3_C)
                print()
                print('C4 ', C4_C)
                print()
        
    print("list of exists in second syllable: ")
    if len(list_of_sylabs[1]) >= 2:
        C1VC_C = [] 
        C2VC_C = [] 
        C3VC_C = [] 
        C4VC_C = [] 
        for z in l_to_d2.keys():
            existed_categories_Cs(z, C1VC_C, C2VC_C, C3VC_C, C4VC_C)
        if len(C1VC_C[1]) >= 4:
            V1C_C = []
            V2C_C = []
            V3C_C = []
            V4C_C = []
            V5C_C = []
            for u in C1VC_C:
                existed_categories_Vs(u, V1C_C, V2C_C, V3C_C, V4C_C, V5C_C)
            #print(len(V4C_C))
            for v in C2VC_C:
                existed_categories_Vs(v, V1C_C, V2C_C, V3C_C, V4C_C, V5C_C)
            #print(len(V4C_C))
            for w in C3VC_C:
                existed_categories_Vs(w, V1C_C, V2C_C, V3C_C, V4C_C, V5C_C)
            #print(len(V4C_C))
            for y in C4VC_C:
                existed_categories_Vs(y, V1C_C, V2C_C, V3C_C, V4C_C, V5C_C)
            #print(len(V4C_C))
            
            if len(V1C_C[1]) == 4:
                C1_C = []
                C2_C = []
                C3_C = []
                C4_C = []
                for a in V1C_C:
                    existed_categories_Cs(a, C1_C, C2_C, C3_C, C4_C)
                for b in V2C_C:
                    existed_categories_Cs(b, C1_C, C2_C, C3_C, C4_C)
                for c in V3C_C:
                    existed_categories_Cs(c, C1_C, C2_C, C3_C, C4_C)
                for d in V4C_C:
                    existed_categories_Cs(d, C1_C, C2_C, C3_C, C4_C)
                for e in V5C_C:
                    existed_categories_Cs(e, C1_C, C2_C, C3_C, C4_C)

                
        print('C1 ', C1VC_C)
        print()
        print('C2 ', C2VC_C)
        print()
        print('C3 ', C3VC_C)
        print()
        print('C4 ', C4VC_C)
        print()
        if len(C1VC_C[1]) >= 4:
            print('V1 ', V1C_C)
            print()
            print('V2 ', V2C_C)
            print()
            print('V3 ', V3C_C)
            print()
            print('V4 ', V4C_C)
            print()
            print('V5 ', V5C_C)
            print()
            if len(V1C_C[1]) == 4:
                print('C1 ', C1_C)
                print()
                print('C2 ', C2_C)
                print()
                print('C3 ', C3_C)
                print()
                print('C4 ', C4_C)
                print()



    ### gaps in first heja:    
    list_of_gaps1_1 = segment_gaps(l_to_d1, list_of_sylabs[0])
    #print("list of gaps in first syllable: ")
    #for i in list_of_gaps1_1:
        #print(i)
    print("first segment's gap: ", len(list_of_gaps1_1))
    for b in list_of_gaps1_1:
        print(b)
    print()
    
    ### gaps in second heja:
    list_of_gaps1_2 = segment_gaps(l_to_d2, list_of_sylabs[1])
    #print("list of gaps in second syllable: ")
    #for i in list_of_gaps1_2:
        #print(i)
    print("second segment's gap: ", len(list_of_gaps1_2))
    for b in list_of_gaps1_2:
        print(b)
    print()
    
    ### gaps in tarkib:
    list_of_gaps1 = tarkib_gaps(l_to_d1, l_to_d2, dict1)
    #for i in list_of_gaps1:
        #print('gap: ', i)

    print('number of all possible 2-syllables under the ' + do_hejayiha[i] + 'pattern: multiply the "number of all possible segments" in the above two syllables!')
    print('number of all possible 2-syllables over the existed combination of categories in each of syllables: ', (len(l_to_d1) * len(l_to_d2)))
    print()
    print('gaps: ', len(list_of_gaps1))
    print('exists: ', (len(l_to_d1) * len(l_to_d2)) - len(list_of_gaps1))
    #print(list_of_gaps1)
    #print('exists: ', len(dict1))
    print()
    #for i in list_of_gaps1:
        #print('gap: ', i)
    print()
    print()
    print()
        
conn.close()
