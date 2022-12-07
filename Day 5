# Part 1

import pandas as pd
sections= pd.read_csv('input_day4.csv', header=None, names=['Elf1', 'Elf2'] )

sections['Elf1_1']=sections['Elf1'].apply((lambda x: x[0:2]))
sections['Elf1_1'] = sections['Elf1_1'].str.replace('-','')
sections['Elf1_2']=sections['Elf1'].apply(lambda x: x[-2:])
sections['Elf1_2'] = sections['Elf1_2'].str.replace('-','')
sections['Elf2_1']=sections['Elf2'].apply(lambda x: x[0:2])
sections['Elf2_1'] = sections['Elf2_1'].str.replace('-','')
sections['Elf2_2']=sections['Elf2'].apply(lambda x: x[-2:])
sections['Elf2_2'] = sections['Elf2_2'].str.replace('-','')

sections['Elf1_1']=sections['Elf1_1'].astype(int)
sections['Elf1_2']=sections['Elf1_2'].astype(int)
sections['Elf2_1']=sections['Elf2_1'].astype(int)
sections['Elf2_2']=sections['Elf2_2'].astype(int)

sections['elf1_in_elf2']= (sections['Elf1_1']>=sections['Elf2_1']) & (sections['Elf1_2']<=sections['Elf2_2'])
sections['elf2_in_elf1']= (sections['Elf1_1']<=sections['Elf2_1']) & (sections['Elf1_2']>=sections['Elf2_2'])

(sections['elf1_in_elf2']==True).sum()+(sections['elf2_in_elf1']==True).sum()-(sections['elf1_is_equal_elf2']==True).sum()

#Part 2

sections['overlap']= ((sections['Elf1_1']<=sections['Elf2_1']) & (sections['Elf1_2']>=sections['Elf2_1']) |
                    (sections['Elf2_1']<=sections['Elf1_1']) & (sections['Elf2_2']>=sections['Elf1_1']))
                    
(sections['overlap']==True).sum()
