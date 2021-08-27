# Have user enter Fahrenheit or Celsius, then convert user provided temperature to opposite temperature scale.
# Step 1 - Display message saying "Type f for fahrenheit or c for celsius" and get input
# Step 2 - store input
# Step 3 - determine if inuput is fahrenheit or celsius
# Step 4 - get input and store input for temp
# Step 5 - Convert input to f or c 
# Test
import sys

# Get temperature scale input from user
degree = input("Enter F for Fahrenheit or C for Celsius: ").strip().lower()

# Get temperature value input from user
temp = float(input("Enter temperature: ").strip())

if degree[0] == "f": # Check if fahrenheit
    convTemp = (temp - 32.0) * 5.0 / 9.0
    print(str(round(convTemp, 2)) + " C")
elif degree[0] == "c": # Check if celsius
    convTemp = (temp * 9.0 / 5.0) + 32.0
    print(str(round(convTemp, 2)) + " F")
else: # Error on anything else, and quit
    print("Invalid input.")
    sys.exit(1)