#Write a script that computes the sum from 0 to a user inputted number.
#This time though, start at the user inputted number and work down.
#This answer will look very much like the example above,
#you'll just need to change a couple of things.


my_num = int(input('Enter a number to find the sum up to: '))
sum_result = 0
current = my_num
while current >= 0:
    sum_result += current
    current -= 1
    print(sum_result)
