'''
Elijah Morgan Problem 3 - largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

# This function creates a list of all factors of an integer, within a reasonable timeframe.
def factor(dividend):
    output = []
    factor = 3

    while factor*factor <= dividend:

        if dividend % factor == 0:
            output.append(factor)

            if dividend//factor != factor:
                output.append(dividend//factor)

        factor += 2
    return output

# This function returns ONLY the prime factors of an integer.
def primeFactors(integer):
    primeList = []

    # Uses previous factor() function to find ALL of the factors of the input integer.
    for num in factor(integer):
        # Checks each factor if it can be factored further. If it can, it's NOT a prime number.
        if len(factor(num)) == 0:
            primeList.append(num)

    # Sorts remaining prime values just in case they're out of order
    primeList.sort()
    return primeList

# Prints the last and highest prime value into the console.
print(primeFactors(600851475143)[-1])