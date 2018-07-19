list_1 = [0, 3, 6, 9, 10, 2, 5]
list_2 = [2, 6, 4, 7, 8, 1, 15]

common= []
for number_1 in list_1:
    for number_2 in list_2:
        if number_1 == number_2:
            common.append(number_1)
print ('These are the common numbers between the lists {comunes} '.format(comunes = common))
