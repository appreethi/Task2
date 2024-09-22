''' 
Write a python program to calculate the total number of vowels and count of each individual vowel A,E,I,O,U in 
the string "Guvi Geeks Network Private Limited"

'''

#The input string
input_string="Guvi Geeks Private Limited"

vowel_string="aeiouAEIOU"

# Initializing counters for each vowel and total number of vowels
total_count=0
vowel_count={'a':0,'i':0,'o':0,'e':0,'u':0}

#Iterate through character from the given string
for char in input_string:
    if char in vowel_string:
        if vowel_count.get(char):
            vowel_count[char]+=1
        else:
            vowel_count[char]=1
        total_count+=1

#printing the results

print("The total number of vowels in the given string",total_count)
print("count of each individual in the given string",vowel_count)
    



