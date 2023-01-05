'''
Elijah Morgan 1/5/2023
Project Euler Problem 6, Sum square difference

The sum of the squares of the first ten natural numbers is,
1^2 + 2^3 +...+ 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 +...+ 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
# Finds the sum of the first 100 squares of natural numbers.
sqNum = 0
for num in range(101):
    sqNum += num**2

# Finds the difference between the sum of squares and square of the sum.
print(sqNum - sum(range(101))**2)
