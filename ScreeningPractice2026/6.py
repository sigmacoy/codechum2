# Part Number Validation
"""
You are tasked with validating a series of part numbers. A valid
part number must adhere to a strict format: AAA-DDDD-C,
where 'A' represents an uppercase letter, 'D' represents a digit,
and 'C' is a special checksum digit. The hyphens must be
present at the exact positions.
The validation rules are as follows:
• The part number must be exactly 10 characters long.
• First 3 characters (positions 0-2) must be uppercase
letters.
• The 4th character (position 3) must be a hyphen (-).
• Next 4 characters (positions 4-7) must be digits.
• The 8th character (position 8) must be another hyphen
(-).
• The last character (position 9) must be a digit. This is
called the checksum.
To validate the checksum digit:
• Add up the 4 digits in the DDDD section (positions 4-7)
• Take the sum modulo 10 (sum % 10)
• The result must match the checksum digit at position 9
Input:
A single string representing the part number. The string will not
contain any spaces and will have a length between 1 and 20.
Output:
A single line of output: "VALID" if the part number meets all the
criteria, or "INVALID" otherwise.
"""

def validate_part_number(part):
    # 1. Check exact length
    if len(part) != 10:
        return "INVALID"
        
    # 2. Check hyphens at exact positions
    if part[3] != '-' or part[8] != '-':
        return "INVALID"
        
    # 3. Check the first 3 characters (0-2) are uppercase letters
    for i in range(3):
        if not part[i].isupper() or not part[i].isalpha():
            return "INVALID"
            
    # 4. Check the 4 characters (4-7) and the checksum (9) are digits
    # and calculate the sum of the DDDD section at the same time
    digit_sum = 0
    for i in range(4, 8):
        if not part[i].isdigit():
            return "INVALID"
        digit_sum += int(part[i])
        
    if not part[9].isdigit():
        return "INVALID"
        
    # 5. Validate the checksum
    checksum = int(part[9])
    if (digit_sum % 10) != checksum:
        return "INVALID"
        
    # If it passes all checks
    return "VALID"

part_number = input("Enter part number: ")

print(validate_part_number(part_number))