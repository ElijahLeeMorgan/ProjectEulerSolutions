'''
Elijah Morgan Problem 4- Largest Palindrome Product

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

# Originally I looked into a solution utilizing the patterns described in sequence A002113 on oeis.org...
# ...but, decided to just go with brute force for now. I'll return to this question again.

# The list of number is done in reverse order to save time, as I only need the LARGEST palindrome product.
unfilteredMultiples = list(range(1000,100,-1))
palindromes = []

# Removes all values ending in 0, because a natural number cannot begin with 0 it cannot be a palindrome.
for multiple in unfilteredMultiples:
    if multiple % 10 == 0:
        unfilteredMultiples.remove(multiple)


# Gives us every possible permutation of [101, 999] * [101, 999] excluding numbers ending in 0.
for multiple in unfilteredMultiples:
    for multiple2 in unfilteredMultiples:
        num = str(multiple * multiple2)
        paList = []
        RpaList = []

        for char in num:
            paList.append(char)

        RpaList = list(reversed(paList))

        if paList == RpaList:
            palindromes.append(int(num))

print('Solution: ',sorted(palindromes)[-1])
