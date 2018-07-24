#Write a script that takes a user inputted
#number and prints whether it is positive, negative or zero,
#with "The inputted number is (positive/negative/zero)" depending.


user_number = float(input('Enter a number to evaluate: '))

if user_number == 0:
    print ('The inputed number is 0')
elif user_number > 0:
    print ('The inputed number is positive')
elif user_number < 0:
    print ('The inputed number is negative')
