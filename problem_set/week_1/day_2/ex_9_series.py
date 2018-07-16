

input_num = int(input("Enter a number to determine the total in the series "))

if input_num == 0:
    print (0)
else:
    total = 0
    current = 1
    while current <= input_num:
        value = (2 * current) + 1
        total += value
        current += 1

    print (total)
