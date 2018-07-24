the_string = input("Provide a string to evaluate ").lower()
#the_letter = input("Provide a letter to search for ").lower()

#letter_count = the_string.count(the_letter)
#print (letter_count)

if the_string[-1] == '!':
    print (the_string.upper())
else:
    print (the_string.lower())

consonants = []

for letter in the_string:
    if letter != 'a' and letter != 'e' and letter != 'i' and letter != 'o' and letter != 'u':
        consonants.append(letter)
s = ''
print (s.join(consonants))

#Write a script that makes every other letter of a user inputted string capitalized.
cap_letters = []
for indx,letter in enumerate(the_string):
    if indx == 0:
        cap_letters.append(letter.upper())
    elif indx % 2 != 0:
        cap_letters.append(letter.lower())
    else:
        cap_letters.append(letter.upper())

print (s.join(cap_letters))
