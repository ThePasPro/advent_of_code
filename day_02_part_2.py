# https://adventofcode.com/2023/day/2

sum_of_power_of_all_games = []
for game in open('day_02_input.txt', 'r'):
    game_id = game.strip().split(': ')[0][-1]
    game_turns = game.strip().split(': ')[1].split('; ')

    minimum_amount_of_red_cubes_required = 0
    minimum_amount_of_green_cubes_required = 0
    minimum_amount_of_blue_cubes_required = 0

    for cube in game_turns: 
        cubes = cube.strip().split(',')

        red_cubes = 0
        green_cubes = 0
        blue_cubes = 0

        for cube_element in cubes:
            cube_elements = cube_element.strip().split(' ')
     
            count = int(cube_elements[0])
            colour = cube_elements[1]

            if colour == 'red':
                red_cubes += count
            elif colour == 'green':
                green_cubes += count
            elif colour == 'blue':
                blue_cubes += count

        if red_cubes > minimum_amount_of_red_cubes_required:
            minimum_amount_of_red_cubes_required = red_cubes
        if green_cubes > minimum_amount_of_green_cubes_required:
            minimum_amount_of_green_cubes_required = green_cubes        
        if blue_cubes > minimum_amount_of_blue_cubes_required:
            minimum_amount_of_blue_cubes_required = blue_cubes

    power_of_cubes_per_game = minimum_amount_of_red_cubes_required * minimum_amount_of_green_cubes_required * minimum_amount_of_blue_cubes_required
    sum_of_power_of_all_games.append(power_of_cubes_per_game)

solution = sum(map(int, sum_of_power_of_all_games))
print(f'Solution: {solution}')
