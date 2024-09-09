list_test = [
    [3, '3S'], [7, '7S'], [9, '9H'], [9, '9S'], [10, '10D'], [6, '6S'], [5, '5H'], [10, '10S'], [8, '8D'], [8, '8S'], [10, '10D'], [7, '7C'], [7, '7H'], [5, '5S'], [4, '4S'], [3, '3D'], [7, '7D'], [11, 'AS']
]

value = 11

for sublist in list_test:
    if 11 in sublist:
        target = list_test.index(sublist)
        list_test[target][0] = 1

print(list_test)
