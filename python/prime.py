def prime (n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
num=int(input("Enter a number: "))
if prime(num):
    print(num,"is a prime number")
else:    print(num,"is not a prime number")
print("The prime numbers between 1 and 100 are:")
for i in range(1,101):
    if prime(i):
        print(i,end=" ")