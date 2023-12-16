import re

letters = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def convert_letter_to_number(letter):
    if letter in letters:
        return str(letters.index(letter) + 1)
    return letter

solution = []
for line in open('day_01_input.txt', 'r'):
    numbers = [*map(convert_letter_to_number, re.findall(r"(?=(" + "|".join(letters) + "|\\d))", line))]
    calibration = numbers[0] + numbers[-1]
    solution.append(calibration)

print(sum(map(int, solution)))