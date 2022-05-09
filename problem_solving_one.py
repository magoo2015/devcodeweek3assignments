"""
1.	Reverse a string
a.	Write code that takes a string as input and returns the string reversed
b.	i.e. “Hello” will be returned as “olleH”

"""

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