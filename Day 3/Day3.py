import re

# Get the input from a txt file
try:
    with open('./Day 3/Day3_Input.txt', 'r') as file:
        rawInput = file.read()
except FileNotFoundError:
    print("File not found. Please check the file path.")
    rawInput = ""

if rawInput:
    # Keep only tokens that are allowed
    allowedTokens = re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", rawInput)

    # Initialize the variables
    enabled = True # Start with enabled
    totalMul = 0

    for token in allowedTokens:
        if token == "do()":
            enabled = True
        elif token == "don't()":
            enabled = False
        else:
            if enabled:
                # Extract the numbers from the mul instruction and add to the running total
                nums = token.split('(')[1].split(')')[0].split(',')
                totalMul += int(nums[0]) * int(nums[1])
    
    print("Sum of multiplications:", str(totalMul))