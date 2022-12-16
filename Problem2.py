'''
Elijah Morgan 12/16/2022

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.

'''

outPut = []

# Creates a list containing the values of the fibonacci sequence until the values exceed a given interger.
def fibonacci(stop=4_000_000):
    fibOutPut = [1, 2]
    i = 0

    while fibOutPut[-1] <= stop:
        fibOutPut.append(fibOutPut[i] + fibOutPut[i + 1])
        i += 1

    # Removes the last value of the output of the fibonacci function, because it's guaranteed to be > four million.
    fibOutPut.pop(-1)

    return fibOutPut

# removes all odd values from the final sum, and places the values into a new list.
for value in fibonacci():
    if value % 2 == 0:
        outPut.append(value)

# Outputs sum of all even fibonacci numbers under 4,000,000.
print(sum(outPut))
