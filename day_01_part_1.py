# https://adventofcode.com/2023/day/1

import re

solution = []
for line in open('day_01_input.txt', 'r'):
    numbers = re.findall(r'\d', line)
    calibration = numbers[0] + numbers[-1]
    solution.append(calibration)

print(sum(map(int, solution)))