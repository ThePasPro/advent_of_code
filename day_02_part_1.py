# https://adventofcode.com/2023/day/2

import re

ids_of_succesful_games = []
for game in open('day_02_input.txt', 'r'):
    cleaned_games = game.split(':')
    cleaned_games = [string.strip() for string in cleaned_games]
    game_id = cleaned_games[0].split()[1] # Index 0 for "Game ID", Index 1 for "ID". 

    game_details = cleaned_games[1].split(';')
    cleaned_game_details = [string.strip() for string in game_details]

    succesful_turns = 0

    for turn in cleaned_game_details:     
        game_turns = turn.split(',')
        cleaned_game_turns = [string.strip() for string in game_turns]     

        red_cubes = 12
        green_cubes = 13
        blue_cubes = 14
        sum_of_red_cubes = 0
        sum_of_green_cubes = 0
        sum_of_blue_cubes = 0

        for cube in cleaned_game_turns:
            game_cubes = cube.split(',')
            for element in game_cubes:
                elements = element.split()
                count = int(elements[0])
                color = elements[1]

                if color == 'red':
                    sum_of_red_cubes += count
                elif color == 'green':
                    sum_of_green_cubes += count
                elif color == 'blue':
                    sum_of_blue_cubes += count

        if sum_of_red_cubes <= red_cubes and sum_of_green_cubes <= green_cubes and sum_of_blue_cubes <= blue_cubes:
            succesful_turns += 1

    if succesful_turns == len(cleaned_game_details):
        ids_of_succesful_games.append(game_id)

solution = sum(map(int, ids_of_succesful_games))
print(f'Solution: {solution}')