#strong num 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def strong_num(n):
    sum_factorials = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum_factorials += factorial(digit)
        temp //= 10
    return sum_factorials == n

n = int(input("Enter a number: "))
if strong_num(n):
    print(n, "is a strong number")
else:
    print(n, "is not a strong number")
    