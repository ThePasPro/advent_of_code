# https://adventofcode.com/2023/day/5


data = open('day_05_input.txt').read().split('\n\n')
print(data)

seeds = list(map(int, data[0].split(': ')[1].split()))
print(f'Seeds: {seeds}')

for line in data[1:]:
    ranges = []
    for line in line.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))

    print(ranges)

    new = []
    for seed in seeds:
        for destination_range_start, source_range_start, range_length in ranges:
            if  seed in range(source_range_start, source_range_start + range_length):
                new.append(destination_range_start - source_range_start + seed)
                break
        else:
            new.append(seed)
    seeds = new
    print(f'seed list: {seeds}')

print(min(seeds))





