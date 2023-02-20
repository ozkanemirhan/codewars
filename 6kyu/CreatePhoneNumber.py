# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.

# Don't forget the space after the closing parentheses!

# My solution:
def create_phone_number(numbers):
    if len(numbers) != 10:
        raise ValueError()
    for num in numbers:
        if num<0 or num>9:
            raise ValueError()
            
    area_code = ''.join(map(str, numbers[:3]))
    prefix = ''.join(map(str, numbers[3:6]))
    line_number = ''.join(map(str, numbers[6:]))
    
    return f"({area_code}) {prefix}-{line_number}"