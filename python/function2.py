def largest(a,b,c):
    if a>b and a>c:
        print(a,"is the largest")
    elif b>a and b>c:
        print(b,"is the largest")
    else:
        print(c,"is the largest")
        print("Both numbers are equal")
largest(10,20,30)

def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
result=largest(10,20,30)
print("The largest number is",result)