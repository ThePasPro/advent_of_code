# https://adventofcode.com/2023/day/4

cards_data = {}

for index, card in enumerate(open('day_04_input.txt', 'r')):
    if index not in cards_data:
        cards_data[index] = 1

    card_number = card.strip().split(': ')[0].split(' ')[1]
    winning_numbers = card.strip().split(': ')[1].split('| ')[0].strip().split()
    available_numbers = card.strip().split(': ')[1].split('| ')[1].strip().split()

    number_of_winning_cards = 0
    for number in available_numbers:
        if number in winning_numbers:
            number_of_winning_cards += 1

    for card in range(index + 1, index + 1 + number_of_winning_cards):
        cards_data[card] = cards_data.get(card, 1) + cards_data[index]

print(f'Solution: {sum(cards_data.values())}')