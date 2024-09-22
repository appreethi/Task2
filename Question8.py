'''Write a program that takes a string and returns true if it is an anagram of another string , false otherwise'''

#two strings are given
mystring1="Silent"
mystring2="Listen"

#converting the strings to lower case
mystring1=mystring1.lower()
mystring2=mystring2.lower()

#check if lengths of both the strings are same or different
if len(mystring1) != len(mystring2):
    print(False)

#convert strings to list and then sort them
sorted_string1=sorted(mystring1)
sorted_string2=sorted(mystring2)

#compare sorted version of the strings

if sorted_string1==sorted_string2:
    print(True)
else:
    print(False)