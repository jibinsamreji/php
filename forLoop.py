for item in 'Jibin Sam':
    print(item)

for itemList in ['Jibin', 'Sam', 'Reji']:
    print(itemList)

for rangeList in range(10):
    print(rangeList)
for rangeListR in range(1, 10, 2):
    print(rangeListR)

price = [10, 20, 30]

for total in price:
    total += total
print(f"Total at payout : {total}")

# Nested Loops
for x in range(3):
    for y in range(3):
        print(f"({x},{y})")

# Pattern using Nested Loops
numbers = [5, 2, 5, 2, 2]
for value in numbers:
    output = ''
    for count_x in range(value):
        output += 'x'
    print(output)

pattern_value_L = [2, 2, 2, 2, 7]
for each_value in pattern_value_L:
    output_string = ''
    for no_x in range(each_value):
        output_string += 'x'
    print(output_string)


