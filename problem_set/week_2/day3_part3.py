#Write a script that creates a list of only the even numbers
#between 0 and a user inputted number.

num = int(input('Enter a number '))
divisor = int(input('Enter a number to divide by '))

even_numbers = []
for number in range(2,num +1, 2):
    even_numbers.append(number)
print ('These is the even numbers list ' + str(even_numbers))


#Write a script that creates a list of only numbers divisible
#by a user inputted number that are between 0 and a user inputted number
#(Hint: Use input() twice to get both of the user inputs)

divisible_nums = []
for number in range(1,num +1):
    if number % divisor == 0:
        divisible_nums.append(number)
print ('These are the numbers that can be divided by {divisor_out} : \
 {div_nums_out}'.format(divisor_out = divisor , div_nums_out = divisible_nums))

#Given the list [0, 3, 6, 9, 10, 2, 5] and [2, 6, 4, 7, 8, 1, 15],
#write a script that finds the common elements between them.
#Store them in a list, and print that list, sorted, as the final output
#(if you'd like you can go ahead and hard code those lists in your script).

list_1 = [0, 3, 6, 9, 10, 2, 5]
list_2 = [2, 6, 4, 7, 8, 1, 15]

common= []
for number_1 in list_1:
    for number_2 in list_2:
        if number_1 == number_2:
            common.append(number_1)
print ('These are the common numbers between the lists {comunes} '.format(comunes = common))


#For a user inputted number,
#write a script that outputs a list of multiples of that number from 0 up to another user inputted number.
#For example, given the numbers 4 and 20, your script should print the numbers 4, 8, 12, and 16.

inputed_num = 4
up_to_num = 20

multiples =[]

for number in range(1, up_to_num +1):
    if number % inputed_num == 0:
        multiples.append(number)
print (multiples)
