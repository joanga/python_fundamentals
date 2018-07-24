

my_num= int(input('Enter the a number to determine if it is prime: '))

if my_num == 1:
    print ('The number is not prime')
elif my_num == 2 or my_num == 3:
    print ('The number is prime')



else:
    current = 2
    while current < (my_num / 2) :
        if my_num % current == 0:
            print ('not prime')
            quit()
        current += 1

print ('The number is prime')
