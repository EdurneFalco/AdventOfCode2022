#Part 1

with open('input_day6.csv', mode='r+', encoding='utf-8') as f:
    subroutine = f.read()
    
subset = []
counter=0
for i in subroutine:
    subset.append(i)
    if len(subset)== 4:
        if len(subset) == len(set(subset)):
            y= ''.join(map(str,subset))
            print(subroutine.rfind(y)+4)
        else:
            subset.pop(0)
            counter+=1
            
# Part 2

subset = []
counter=0
for i in subroutine:
    subset.append(i)
    if len(subset)== 14:
        if len(subset) == len(set(subset)):
            y= ''.join(map(str,subset))
            print(subroutine.rfind(y)+14)
        else:
            subset.pop(0)
            counter+=1
