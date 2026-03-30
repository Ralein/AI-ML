def frequency_number(n):
    num_str = str(n)
    frequency = {}
    
    for digit in num_str:
        if digit in frequency:
            frequency[digit] += 1
        else:
            frequency[digit] = 1
            
    return frequency
number = int(input("Enter a number: "))
result = frequency_number(number)
print("Digit Frequency:")   
for digit, freq in result.items():
    print(f"Digit {digit}: {freq} times")