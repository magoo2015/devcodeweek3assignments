"""
1.	Reverse a string
a.	Write code that takes a string as input and returns the string reversed
b.	i.e. “Hello” will be returned as “olleH”

"""

from itertools import count


def reverse(word): # parameter will be string taken from input within function
    reversed_word = "" #empty string to hold characters from loop

    for index in range(len(word)-1, -1, -1):
        reversed_word += word[index]
    print(reversed_word)

#reverse("California")


"""
2.	Capitalize letter
a.	Write code that takes a string as input and capitalize the first letter of each word. Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”
"""


string_word = "Hello World"

new_string_word = string_word.capitalize() # can use captilize() to capitalize first character, how can I with additional words?
# python split string might be useful  https://www.w3schools.com/python/ref_string_split.asp
split_string_word = string_word.split(" ") #A loop should help now.

def capitilize(words):
    new_word = words.title()
    return new_word
#This capitalizes each word but its just one word....
#capitilize("hello world")


"""
3.	Compress a string of characters
a.	For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a"

"""
#Iterate through string and count same characters add to new string/list
#Count identical characters
#If next character is different restart count
#Need to a first char to holder then start loop


def compression(compression_string):
    string_holder = ""
    string_count = 1

    string_holder += compression_string[0]

#So far this list each string.  Need to figure out count.
    for i in range(len(compression_string) -1):
        if compression_string[i] == compression_string[i +1]:
            string_count += 1
        elif compression_string[i] != compression_string[i +1] and string_count > 1:
            string_holder += str(string_count)
            string_holder += compression_string[i +1]
            string_count = 1

            










"""Write code that takes a user input and checks to see if it is a palindrome and reports the results"""
#Get user input in main.py
#Get reverse word stored in variable
#https://www.w3schools.com/python/python_howto_reverse_string.asp  Use [::1] to print string in reverse

def palindrome(word):
    new_word = word[::-1]
    
    if word == new_word:
        print(f"Your word {word}, is a palindrome: {new_word}")
    else:
        print(f"Your word {word}, is not a palindrome: {new_word}")
    
    