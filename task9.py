"""
In mathematics, the factorial of an integer n, denoted by n! is the following
product:
n!=1×2×...×n
For the given integer n
calculate the value n!. Don't use math module in this exercise.
"""


n = int(input("введите число:"))
fact = 1
while n>0:
    fact = fact * n
    n = n - 1
print(fact)