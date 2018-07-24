

my_num_1 = int(input('Enter the first number: '))
my_num_2 = int(input('Enter the second number: '))

if my_num_1 > my_num_2:
    current = my_num_1
elif my_num_2 > my_num_1:
    current = my_num_2


while current >= 1:
    if my_num_1 % current == 0 and my_num_2 % current == 0:
        print (str(current) +  ' is the GCD divisor of ' + str(my_num_1) + ' and ' + str(my_num_2))
        break
    current -= 1
