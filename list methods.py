numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
max = numbers[0]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)