#Write a function to print all prime numbers between two numbers a and b, but skip those primes whose digit sum is also a prime number.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            
            return False
    return True

def digit_sum(n):
    sum_digits = 0
    while n > 0:
        sum_digits += n % 10
        n //= 10
    return sum_digits

def prime_between(a, b):
    print(f"The prime numbers between {a} and {b} are:")
    for num in range(a, b + 1):
        if is_prime(num):
            if not is_prime(digit_sum(num)):
                print(num, end=" ")
                
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
prime_between(a, b)
