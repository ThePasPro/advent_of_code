# https://adventofcode.com/2023/day/6

data = open('day_06_input.txt').readlines()
match_time = list(map(int, data[0].split()[1:]))
record_distance = list(map(int, data[1].split()[1:]))

print(f'Time: {match_time}')
print(f'Distance: {record_distance}')
print(match_time)

score = []
for index, match in enumerate(match_time):
    match_time = match
    
    count_of_beating_record = 0
    for second in range(1, match_time):
        speed = 1
        power = 1
        time_left = match_time - second
        speed = power * second
        distance = speed * time_left
        
        if distance > record_distance[index]:
            count_of_beating_record += 1   
    score.append(count_of_beating_record)

solution = 1
for winners in score:
    solution *= winners

print(f'Solution: {solution}')