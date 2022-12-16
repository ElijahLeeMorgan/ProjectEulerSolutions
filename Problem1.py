'''
Elijah Morgan 12/16/2022
Project Euler Problem 1, Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

# Utilizing the built-in range function, we collect a set of every multiple of 3 and 5.
multiplesSet = set(range(0, 1000, 5)).union(set(range(0, 1000, 3)))

# Prints out final sum into the terminal.
print(sum(multiplesSet))
