#Write a script that takes two user inputted numbers and prints
#"The first number is larger" or "The second number is larger"
#depending on which is larger. (**Hint**: you'll need to use `input()` twice.)


user_number_1 = float(input('Enter a number to evaluate: '))
user_number_2 = float(input('Enter a second number to evaluate: '))

if user_number_1 > user_number_2:
    print ('The first number is larger')
elif user_number_1 < user_number_2:
    print ('The second number is larger')
elif user_number_1 == user_number_2:
    print ('The numbers are equal')
