import os
import argparse

# Parse command line arguments so we can run in debug mode
parser = argparse.ArgumentParser(description='Process page order updates.')
parser.add_argument('--debug', action='store_true', help='Enable debug mode')
args = parser.parse_args()
debugMode = args.debug

# Get the input from a txt file
try:
    with open('./Day 5/Day5_Input.txt', 'r') as file:
        rawInput = file.read()
except FileNotFoundError:
    print("File not found. Please check the file path.")

if rawInput:

    # Initialise variables
    middlePageSum = 0

    # Split input at the empty line
    pageOrderRules = rawInput.split("\n\n")[0].splitlines() # targetPage | proceedingPage
    updatePages = rawInput.split("\n\n")[1].splitlines() # Update pages comma separated

    def checkPageOrder(update):
        # Initialise the local variables
        isGoodOrder = True
        update = update.split(",") # Split the update into a list of pages

        # Check each number in the update list
        for page in range(1, len(update)): # Skip the first page as it is always the first page
            # Check if the page is in the pageOrderRules
            for rule in pageOrderRules:
                if not isGoodOrder:
                    break # Previous page order was not good, no need to check further
                if update[page] in rule.split("|")[0]:
                    # If the page is in the pageOrderRules, ensure the proceeding page is not preceding the current page in the update list
                    if rule.split("|")[1] in update[:page]: # Check preceding pages for the proceeding page from the rule
                        isGoodOrder = False # If the proceeding page is preceding the current page, the order is not good
                        
                        # Print the debug message
                        if debugMode:
                            debugString = ""
                            for debugPage in range(0, len(update)):
                                if debugPage == page:
                                    debugString += f"\033[94m{update[debugPage]}\033[0m" # Preceding page blue
                                elif update[debugPage] == rule.split("|")[1]:
                                    debugString += f"\033[91m{update[debugPage]}\033[0m" # Proceeding page red
                                else:
                                    debugString +=  f"{update[debugPage]}"
                                debugString += ", "
                            print(f"{debugString} | \033[91m Rule '{rule}' violated as page {rule.split('|')[1]} found before page {rule.split('|')[0]} \033[0m")
                        break
        if isGoodOrder:
            
            # If the order is good, add the middle page to the sum
            global middlePageSum
            middlePageIndex = int(len(update)/2)
            middlePageSum += int(update[middlePageIndex])

            if debugMode:
                debugString = ""
                for page in range(0, len(update)):
                    if page == middlePageIndex:
                        debugString += f"\033[93m{update[page]}\033[0m, "
                    else:
                        debugString += f"{update[page]}, "
                print(f"{debugString} | \033[92mOK\033[0m")
            
            
    
    # Check the page orders
    for update in updatePages:
        checkPageOrder(update)

    # Print the result
    if debugMode: print("")
    
    print(f"The sum of the middle pages for the good updates is: {middlePageSum}")
    
    if debugMode:
        print("")
        print("Debug mode is on: See \033[93myellow\033[0m for middle pages, \033[91mred\033[0m for the pages found preceding the \033[94mblue\033[0m page when they should be proceeding.")