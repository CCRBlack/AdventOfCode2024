#Get the input from a txt file
try:
    with open('./Day 1/Day1_Input.txt', 'r') as file:
        rawInput = file.read()
except FileNotFoundError:
    print("File not found. Please check the file path.")
    rawInput = ""

#If file is not empty, calculate the difference
if rawInput:
    # Split the input into lines
    lines = rawInput.split('\n')

    # Split each line into left and right 5 characters and convert to integers
    list1 = sorted([int(line[:5]) for line in lines if line[:5].strip().isdigit()])
    list2 = sorted([int(line[5:]) for line in lines if line[5:].strip().isdigit()])

    # Assuming the lists are the same length
    difference = sum(abs(l1 - l2) for l1, l2 in zip(list1, list2))

    print("Total difference is: " + str(difference))