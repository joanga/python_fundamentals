def lcm(n1,n2):
    if n1 > n2:
        current = n1
    else:
        current = n2
    while True:
        if current % n1  == 0 and current % n2 == 0:
            print (str(current) +  ' is the LCD  of ' + str(n1) + ' and ' + str(n2))
            break
        current += 1

lcm(10,25)



# my_num_1 = int(input('Enter the first number: '))
# my_num_2 = int(input('Enter the second number: '))
#
# if my_num_1 >= my_num_2:
#     current = my_num_1
# else:
#     current = my_num_2
#
# while current:
#     if current % my_num_1  == 0 and current % my_num_2 == 0:
#         print (str(current) +  ' is the LCD  of ' + str(my_num_1) + ' and ' + str(my_num_2))
#         break
#     current
