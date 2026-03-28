def hello():
    print("Hellow")
hello()

def name():
    name=input("Enter your name: ")
    print("Welcome",name)
name()

def add(a,b):
    print("The sum is",a+b)
add(10,20)  

def odd_even(num):
    if num%2==0:
        print(num,"is even")
    else:
        print(num,"is odd")
odd_even(10)