#Write a script that computes the factorial of a user inputted number.
#If you don't know what a factorial is or need a review,
#check [this](https://en.wikipedia.org/wiki/Factorial) link out. Again, your solution is going to look a lot like the code above. Things you should think about:
#    * What is the process of computing a factorial if you were to compute it by hand?
#    * What is the common starting place when trying to compute the factorial of any number?<br><br>

my_num = int(input('Enter a number to find the factorial: '))
sum_result = my_num
current = my_num
while current > 1:
    sum_result = sum_result * (current-1)
    current -= 1
print(sum_result)
