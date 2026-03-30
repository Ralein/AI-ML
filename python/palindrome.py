def palindrome_number_remove(n):
    num_str = str(n)
    num_str = ''.join(filter(str.isdigit, num_str))
    return num_str == num_str[::-1]

def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def can_become_palindrome(n):
    num_str = ''.join(filter(str.isdigit, str(n)))
    left = 0
    right = len(num_str) - 1

    while left < right:
        if num_str[left] != num_str[right]:
            skip_left  = is_palindrome(num_str, left + 1, right)
            skip_right = is_palindrome(num_str, left, right - 1)
            return skip_left or skip_right
        left += 1
        right -= 1

    return True  

number = input("Enter a number: ")

if palindrome_number_remove(number):
    print(f"{number} is already a palindrome.")
elif can_become_palindrome(number):
    print(f"{number} is NOT a palindrome, but CAN become one by removing 1 digit.")
else:
    print(f"{number} cannot become a palindrome by removing just 1 digit.")
