import os

# Get the input from a txt file
try:
    with open('./Day 4/WordSearch.txt', 'r') as file:
        rawInput = file.read()
except FileNotFoundError:
    print("File not found. Please check the file path.")

if rawInput:
    # Split the input into a list of lines so we can address any single character
    wordSearch = rawInput.splitlines()
    columnCount = len(wordSearch[0])
    rowCount = len(wordSearch)
    matchingMap = [[False for _ in range(columnCount)] for _ in range(rowCount)]

    # Initialize the variables
    totalWords = 0
    targetString = "XMAS" # Define the test string
    directions = [
        [0, 1], # Right
        [0, -1], # Left
        [1, 0], # Down
        [-1, 0], # Up
        [1, 1], # Down Right
        [1, -1], # Down Left
        [-1, 1], # Up Right
        [-1, -1] # Up Left
    ]

    def checkWord(row, column):
        """
        Check if the target string is present in the word search starting from the given row and column.

        Args:
            row (int): The row to start the search from.
            column (int): The column to start the search from.
        Returns:
            int: The number of matches found.
        """
        
        # If the first character is not an X, return False
        if wordSearch[row][column] != targetString[0]:
            return 0
        
        # Check each direction for a match
        matches = 0
        for direction in directions:
            testString = targetString[0] # Always start with the first character
            try: # Use try to catch any out of bounds errors
                for i in range(1,len(targetString)): # Get remaining characters
                    newRow = row + (direction[0] * i)
                    newColumn = column + (direction[1] * i)
                    if newRow < 0 or newColumn < 0:
                        raise IndexError # Prevent rollover to the other side of the grid
                    testString += wordSearch[newRow][newColumn]
                
                # If the test string matches the target string, increment the matches
                if testString == targetString:
                    matches += 1

                    # Mark the characters as found for visualisation
                    matchingMap[row][column] = True # Mark the first character
                    for i in range(1,len(targetString)): # Mark the remaining characters
                        matchingMap[row + (direction[0] * i)][column + (direction[1] * i)] = True

            except IndexError:
                continue # If we get an error, continue to the next direction
        
        # After checking all directions, return the number of matches
        return matches

    # Loop through the rows & columns and check how many matches we can find
    for row in range(0, rowCount):
        for column in range(0, columnCount):
                totalWords += checkWord(row, column)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Total matches of '{targetString}' found: {totalWords}, having searched {row + 1} rows and {column + 1} columns.")

def print_grid():
    GREEN = '\033[92m'  # green text
    RESET = '\033[0m'   # reset color
    
    print("\nGrid Visualization:")
    print("-" * (columnCount * 2))
    
    for r in range(rowCount):
        for c in range(columnCount):
            if matchingMap[r][c]:
                print(f"{GREEN}{wordSearch[r][c]}{RESET}", end=" ")
            else:
                print(wordSearch[r][c], end=" ")
        print()
    print("-" * (columnCount * 2))

# Add after the search loop:
print_grid()