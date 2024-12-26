# Get the input from a txt file
try:
    with open('./Day 2/Day2_Input.txt', 'r') as file:
        rawInput = file.read()
except FileNotFoundError:
    print("File not found. Please check the file path.")
    rawInput = ""

# If file is not empty, calculate the number of safe reports
if rawInput:
    # Split the input into lines
    reports = rawInput.split('\n')

    # Initialize the number of safe reports
    safeReports = 0
    unsafeReports = 0

    # Define the check function
    def checkValues(values):
        if (sorted(values) == values or sorted(values, reverse=True) == values) \
        and all( 1<= abs(values[i] - values[i+1]) <= 3 for i in range(len(values) - 1)):
            return True
        else:
            return False

    # For each report check it meets the "safe" criteria: all ascending or descending, and every delta is between 1 and 3 then it is safe
    for report in reports:
        # Split the report into values
        values = [int(value) for value in report.split() if value.strip().isdigit()]
        
        # Check the base set of values
        if checkValues(values):
            safeReports = safeReports + 1
        else:
            # Now check if removing any value from the list will make it safe
            for i in range(len(values)):
                tempValues = values.copy()
                tempValues.pop(i)
                thisReportSafe = False
                if checkValues(tempValues):
                    thisReportSafe = True
                    break
            if thisReportSafe:
                safeReports = safeReports + 1
            else:
                unsafeReports = unsafeReports + 1

    # Print the number of safe reports
    print("Total reports: " + str(len(reports)))
    print("Number of safe reports: " + str(safeReports))
    print("Number of unsafe reports: " + str(unsafeReports))

    if len(reports) != safeReports + unsafeReports:
        print("Warning: Calculation error, the number of reports does not match the sum of safe and unsafe reports.")