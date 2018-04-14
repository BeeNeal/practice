# 1) write a function that finds all anagrams in a list of words and prints a list 
# of only those words. The output words can be in any order.  What is the runtime?

#    Sample input:  ['cat', 'eat', 'dare', 'bash', 'tea', 'dear', 'read']
#    Sample output: ['eat', 'dare', 'tea', 'dear', 'read']

# 2) You are given a list of integers. Write a function that returns a list with
 # original values ordered by largest int, smallest int, second largest int, second 
 # smallest int, third largest int, and so on.  You may modify the input list in 
 # place and return it or you may create and return a new list.
# Example input: [2, 5, -12, 24, 0, -1]
# Example output: [24, -12, 5, -1, 2, 0]

# Example input: [2, 5, -12, 24, 0, -1, 6]
# Example output: [24, -12, 6, -1, 5, 0, 2]

# 3) Using recursion, print integers 0 through n (n being a positive integer),
 # given an argument of n

def print_recursively(n):

    if n >= 0:
        print_recursively(n - 1)
        print n



# 4) Given a list of integers, return the unique integer in that list (no tricks,
 # there can only be one unique integer)

# 5) You have two sets. Find out if one of the sets is a subset of the other. Return  
# True/False. No sorting, no using built-in functions.  