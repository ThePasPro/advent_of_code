# https://adventofcode.com/2023/day/4

total_points = 0
for card in open('day_04_input.txt', 'r'):
    card_number = card.strip().split(': ')[0].split(' ')[1]
    winning_numbers = card.strip().split(': ')[1].split('| ')[0].strip().split()
    available_numbers = card.strip().split(': ')[1].split('| ')[1].strip().split()

    score = 0
    for number in available_numbers:
        if number in winning_numbers:
            if score == 0:
                score += 1
            else:
                score = score * 2

    total_points += score

print(f'Solution: {total_points}')