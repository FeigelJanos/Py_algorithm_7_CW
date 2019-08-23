# Py_algorithm_7_CW
Code Wars Kata 

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.

The input string will only consist of lower case letters and/or spaces.

Best solution:

def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")
    
    OR
    
def getCount(s):
    return sum(c in 'aeiou' for c in s)
