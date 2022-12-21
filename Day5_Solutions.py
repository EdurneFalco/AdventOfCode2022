# Part 1

import csv
with open('input_day5.csv', mode='r+', encoding='utf-8') as f:
    reader = csv.reader (f)
    contents = list(reader)
    
import re
content_str=[]

for order in contents:
    string = ' '.join([str(item) for item in order])
    content_str.append(string)   
  
num_order= []
for i in content_str:
    translation = i.maketrans('','','move ''from' 'to ')
    num_order.append(i.translate(translation))
    
to_do = []
for i in num_order:
    if len(i)==3 and i[0]==1:
        to_do.append(i[1:])
    elif len(i)==3 and i[0]!=1:
        for item in range(0, int(i[0])):
            to_do.append(i[1:])
    else:
        for item in range(0, (int(i[0])*10)+int(i[1])):
            to_do.append(i[2:])
            
pos_1 = ['V','N','F','S','M','P','H','J']
pos_2 = ['Q','D','J','M','L','R','S']
pos_3 = ['B','W','S','C','H','D','Q','N']
pos_4 = ['L','C','S','R']
pos_5 = ['B','F','P','T','V','M']
pos_6 = ['C','N','Q','R','T']
pos_7 = ['R','V','G']
pos_8 = ['R','L','D','P','S','Z','C']
pos_9 = ['F','B','P','G','V','J','S','D']
total_pos = {'pos_1': pos_1, 
             'pos_2': pos_2, 
             'pos_3': pos_3, 
             'pos_4': pos_4, 
             'pos_5': pos_5,
             'pos_6': pos_6, 
             'pos_7': pos_7, 
             'pos_8': pos_8,
             'pos_9': pos_9
             }

def from_to(i, j):
    pos_i = list(total_pos.values())[int(i)-1]
    pos_j = list(total_pos.values())[int(j)-1]
    if len(pos_i)!=0:
        pos_j.insert(0, pos_i[0])
        pos_i.pop(0)
    else:
        pass
      
for element in to_do:
    from_to(element[0],element[1])
total_pos

pos_1[0], pos_2[0], pos_3[0], pos_4[0], pos_5[0], pos_6[0], pos_7[0], pos_8[0], pos_9[0]


# Part 2 (requires recharge initial situation total_pos)

def from_to_2(n, i, j):
    pos_i = list(total_pos.values())[int(i)-1]
    pos_j = list(total_pos.values())[int(j)-1]
    sublist = pos_i[0:n]
    if len(pos_i)!=0:
        for num in reversed(sublist):
            pos_j.insert(0, num)
        del pos_i[0:n]
    else:
        pass
      
for element in num_order:
    if len(element)==3:
        from_to_2(int(element[0]), int(element[1]), int(element[2]))
    else:
        from_to_2((((int(element[0]))*10)+int(element[1])), int(element[2]), int(element[3]))
total_pos

pos_1[0], pos_2[0], pos_3[0], pos_4[0], pos_5[0], pos_6[0], pos_7[0], pos_8[0], pos_9[0]
