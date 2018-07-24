# #Write a function that computes and prints all of the divisors of a user inputted number.
# Here we won't take a user inputted number, but build a function that accepts one parameter,
# a number, and then computes all the divisors of that number.
# The solution to the previous assignment might need to be modified for it to work in a function.


def get_divisors(n):
    current = n
    divisors = []
    while current >= 1:
        if n % current == 0:
            divisors.append(str(current))
        current -= 1

    return divisors


print ('The divisors are: ' + ' '.join(get_divisors(45)))


    # my_num = int(input('Enter a number to find the divisors: '))
    # current = my_num
    # while current >= 1:
    #     if my_num % current == 0:
    #         print (str(current) +  ' is a divisor of ' + str(my_num))
    #     current -= 1
