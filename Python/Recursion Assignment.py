# Write a function printTillN(n) where n is a positive integer input n from the user and print 1 to n. Suppose n = 5 The output should be 1 2 3 4 5

def printTillN(n):
    if n == 0:
        return
    printTillN(n-1)
    print(n,end=" ")

# Write a recursive function to calculate the factorial of a given non-negative integer n.

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

# Write a recursive function to find the sum of digits of a positive integer num.

def sum_of_digits(n):
    if n < 10:
        return n
    return n%10 + sum_of_digits(n//10)

# Write a recursive function to calculate the power of a given base base raised to an exponent exponent. For example, if the function is called with base = 2 and exponent = 3, the result should be 2^3 = 8.

def power(base,exp):
    if exp == 0:
        return 1
    return base * power(base,exp-1)

# Take input from the user (n) and write a recursive function print_pattern(n, i =1) to print a pattern.

def print_pattern_1(n,i=1):
    if i <= n:
        print(str(i)*i)
        print_pattern_1(n,i+1)
    if i < n:
        print(str(i)*i)
        
# Take input from the user (n) and write a recursive function print_pattern(n, i =1) to print a pattern.

def print_pattern_2(n,i=1):
    if i <= n:
        for j in range(1,i+1):
            if j == i:
                print(j,end="")
            else:
                print(j,end=",")
        print()
        print_pattern_2(n,i+1)
    if i < n:
        for j in range(1,i+1):
            if j == i:
                print(j,end="")
            else:
                print(j,end=",")
        print()

# Take input from the user (n) and write a recursive function print_pattern(n, i =1) to print a pattern.

def print_pattern_3(n,i=1):
    if i <= n:
        for j in range(1,i+1):
            print(j,end="")
        print()
        print_pattern_3(n,i+1)
    if i < n:
        for j in range(1,i+1):
            print(j,end="")
        print()

# Given two integers, find and print the GCD (Greatest Common Divisor) of them. The function will return the GCD.

def gcd(num1,num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2,num1 % num2)
    