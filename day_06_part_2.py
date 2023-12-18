# https://adventofcode.com/2023/day/6

data = open('day_06_input.txt').readlines()
match_time = int(data[0].split(':')[1].strip().replace(' ', ''))
record_distance = int(data[1].split(':')[1].strip().replace(' ', ''))

score = []

count_of_beating_record = 0
for second in range(1, match_time):
    speed = 1
    power = 1
    time_left = match_time - second
    speed = power * second
    distance = speed * time_left
    
    if distance > record_distance:
        count_of_beating_record += 1
        score.append(count_of_beating_record)

solution = len(score)
print(f'Solution: {solution}')
