'''Write a program that takes a string and returns the number of words in it'''

#input string is given
input_string="Hello this is my practice session"

#using split method,list will be created
new_list=input_string.split()

#finding the length of new_list
print("The number of words in the given string is:",len(new_list))