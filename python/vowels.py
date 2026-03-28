def string_vowels(s):
    vowels="aeiouAEIOU"
    count=0
    for char in s:
        if char in vowels:
            count+=1
    return count
string=input("Enter a string: ")
result=string_vowels(string)
print("The number of vowels in the string is",result)