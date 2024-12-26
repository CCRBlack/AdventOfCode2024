import re

# Get the input from a txt file
try:
    with open('./Day 3/Day3_Input.txt', 'r') as file:
        rawInput = file.read()
except FileNotFoundError:
    print("File not found. Please check the file path.")
    rawInput = ""


if rawInput:
    # Use regex to extract only the "mul(000,111)" values where 000 and 111 are 1-3 digit numbers
    goodInstructions = re.findall(r'mul\(\d{1,3}\,\d{1,3}\)', rawInput)
    
    # Sum all the multiplication instructions
    totalMul = 0
    for i in range(len(goodInstructions)):
        totalMul = totalMul + (int(goodInstructions[i].split('(')[1].split(',')[0]) * int(goodInstructions[i].split(',')[1].split(')')[0]))
    print("Sum of multiplications: " + str(totalMul))