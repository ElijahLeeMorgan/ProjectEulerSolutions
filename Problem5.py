'''
Elijah Morgan Problem 5 - Smallest Multiple
1/5/2023

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

'''
Notes:
Number MUST:

Be more than 20
Be an even number
Be a multiple of 20
More than 2520 (2520 = 20 * 126)

There's no need to check for divisors 10 and below because all of those numbers are divisors of 11-20.
EX: 14 = 7 * 2, so if 28 % 14 == 0 then 28 % 7 == 0 should be true too.
'''

solution = None
divisors = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
num = 2520

while solution != True:
    num += 20

    for divisor in divisors:
        if num % divisor == 0:
            solution = True
        else:
            solution = False
            break

    if solution:
        print(num)
        break
