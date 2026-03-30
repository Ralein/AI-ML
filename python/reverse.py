def reverse_odd_positions(n):
    num_str = str(n)
    digits = list(num_str)

    odd_pos_digits = [digits[i] for i in range(0, len(digits), 2)]
    
    odd_pos_digits.reverse()
    
    for i in range(0, len(digits), 2):
        digits[i] = odd_pos_digits[i // 2]
    
    return int(''.join(digits))


number = int(input("Enter a number: "))
result = reverse_odd_positions(number)
print(f"Result: {result}")