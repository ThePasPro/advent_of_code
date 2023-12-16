def predict_next_number(sequence):
    if all(x == 0 for x in sequence):
        return 0
    
    deltas = [y - x for x, y in zip(sequence, sequence[1:])]
    difference = predict_next_number(deltas)
    return sequence[-1] + difference

sum_of_predictions = 0
for line in open("day_09_input.txt", 'r'):
    sequence = list(map(int, line.split()))
    sum_of_predictions += predict_next_number(sequence)

print(sum_of_predictions)