# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def fib(n):
    if n < 0:
        print("number should not be smaller than 0.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = 0
even_sum = 0

while fib(n) < 4000000:
    if fib(n) % 2 == 0:
        even_sum += fib(n)
    n += 1

print(even_sum)
     
