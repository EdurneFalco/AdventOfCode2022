#Part 1:

import csv

with open('input_day2.csv', mode='r+', encoding='utf-8') as f:
    reader = csv.reader (f)
    game = list(reader)
print(game)

winning_points=0
win= (['A Y'], ['B Z'], ['C X'])
tie= (['A X'], ['B Y'], ['C Z'])
for i in game:
    if i in win:
        winning_points += 6  
    elif i in tie:
        winning_points += 3
    else:
        winning_points += 0
winning_points

playing_points=0
rock=(['A X'], ['B X'], ['C X'])
paper=(['A Y'], ['B Y'], ['C Y'])
for i in game:
    if i in rock:
        playing_points += 1
    elif i in paper:
        playing_points += 2
    else:
        playing_points +=3
playing_points

game_result= winning_points + playing_points
game_result

#Part 2:

winning_points_2 = 0
winning = (['A Z'], ['B Z'], ['C Z'])
tiying=(['A Y'], ['B Y'], ['C Y'])
for i in game:
    if i in winning:
        winning_points_2 += 6
    elif i in tiying:
        winning_points_2 += 3
    else:
        winning_points_2 += 0 
winning_points_2

playing_points_2=0
rock = (['A Y'], ['C Z'], ['B X'])
paper = (['B Y'], ['A Z'], ['C X'])
for i in game:
    if i in rock:
        playing_points_2 += 1
    elif i in paper:
        playing_points_2 += 2
    else:
        playing_points_2 += 3 
playing_points_2

game_result_2 = winning_points_2 + playing_points_2
game_result_2
