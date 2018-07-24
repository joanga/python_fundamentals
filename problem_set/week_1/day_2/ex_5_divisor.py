

my_num = int(input('Enter a number to find the divisors: '))
current = my_num
while current >= 1:
    if my_num % current == 0:
        print (str(current) +  ' is a divisor of ' + str(my_num))
    current -= 1
