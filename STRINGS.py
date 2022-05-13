player_1 = 'Ruud Gullit'
player_2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = player_1 + " " + str(goal_0) + ", " + player_2 + " " + str(goal_1)
report = f'{player_1} scored in the {goal_0}nd minute' '\n' f'{player_2} scored in the {goal_1}th minute'
player = 'Ronald Koeman'
spatie = player.find(" ")
first_name = player[:spatie]
last = player[spatie+1:]
last_name_len = len(last)
name_short = player[:1] + '. ' + last
chant = len(first_name) * (first_name + '! ') 
chant = chant.rstrip( )
good_chant = chant[-1] != ' '
print(last_name_len)