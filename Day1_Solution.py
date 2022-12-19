#Part1:

with open('calories.csv', mode='r+', encoding='utf-8') as f:
    calories = f.read()
    calories_array = calories.split("\n")
    
elves_calories=[]
calories_count=0
for number in calories_array:
    if number != '' :
        calories_count += int(number)
      
    else:
        elves_calories.append(calories_count)
        calories_count=0
elves_calories
max(elves_calories)

#Part2:

sorted_e_c= sorted(elves_calories, reverse=True)
sum(sorted_e_c[:3])
