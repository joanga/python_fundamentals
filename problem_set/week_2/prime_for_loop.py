

my_num= int(input('Enter the a number to determine if it is prime: '))

if my_num == 1:
    print ('The number is not prime')
elif my_num == 2 or my_num == 3:
    print ('The number is prime')



else:
    ranger = int(my_num / 2)
    #print (ranger)
    for number in range(2,ranger + 1):
        if my_num % number == 0:
            print ('not prime')
            quit()


print ('The number is prime')
