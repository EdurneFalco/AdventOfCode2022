# Part 1

import csv

with open('input_day3.csv', mode='r+', encoding='utf-8') as f:
    reader = csv.reader (f)
    contents = list(reader)
 
first_half=[]
for i in contents:
    for letter in i:
        first_half.append(letter[0:len(letter)//2])

second_half=[]
for i in contents:
    for letter in i:
        second_half.append(letter[len(letter)//2:len(letter)])

misplaced=[]
for i, j in zip(first_half, second_half):
        misplaced.append(set(i).intersection(set(j)))
        
misplaced_priority=[]
for letter in misplaced:
    if str(letter)[2].islower()== True:
        misplaced_priority.append(ord(str(letter)[2])-96)
    else:
        misplaced_priority.append(ord(str(letter)[2])-38)
        
 sum(misplaced_priority)
 
# Part 2

first_elf_group=[]
for i in range(0, len(contents), 3):
    first_elf_group.append(str(contents[i]))

second_elf_group=[]
for i in range(1, len(contents), 3):
    second_elf_group.append(str(contents[i]))

third_elf_group=[]
for i in range(2, len(contents), 3):
    third_elf_group.append(str(contents[i]))

badge=[]
for i, j, k in zip(first_elf_group, second_elf_group, third_elf_group):
        badge.append(set(i).intersection(set(j).intersection(set(k))))

badge_priority=[]
for letter in badge:
    for i in letter:
        if str(i).islower()== True:
            badge_priority.append(ord(str(i))-96)
        elif str(i).isupper()== True:
            badge_priority.append(ord(str(i))-38)

sum(badge_priority)
