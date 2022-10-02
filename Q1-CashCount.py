# Liam Fitzgerald - Parket Technical Assessment Q1

# Create dictionary with initial conditions to store currency value and count
# Dictionaries are ordered, therefore, it is intialized in ascending order
# This allows a loop to cycle through the dictionary in currency ascending order
class var: # Class to store global variables
    currency = {
        "0.05": 0, "0.10": 0, "0.20": 0, 
        "0.50": 0, "1": 0, "2": 0, 
        "5": 0, "10": 0, "20": 0, 
        "50": 0, "100": 0, "200": 0
        }
    total = 0 # Declare the total change count
    countTxt = "C:\\Users\\liams\\Desktop\\count.txt" # Set count.txt path

#----------
# Functions
#----------
def readFile(path):
    try:
        file = open(path, 'r') # Open the text file for reading
        change_arr = file.read().split(',') # Read the contents and split the change into an array
        file.close() # Close the file
        return change_arr # Return array of change
    except:
        print("Error while reading file")
        input("Press enter to END")
        exit(1)


def addToDictionary(change_arr):
    # Cycle through the change array to sort the change into the dictionary
    for i in change_arr:
        if i == "": # Continue to the next item if the item is blank
            continue
        # Exit program if non valid currency is found
        # Additional option could ignore invalid currencies and just count valid currencies
        if i not in var.currency: 
            print("Incorrect currency found {}".format(i))
            input("Press enter to END")
            exit(1)
        var.currency[i] = var.currency[i] + 1 # Add change to dictionary
        var.total = var.total + float(i) # Add amount to total change


def outputCurrencyCount():
    # Cycle through the currency dictionary and count the number of coins/notes for each change value
    # Then print the output to the console (could be outputted anywhere)
    for change in var.currency:
        count = var.currency[change] # Get the number of coins/notes

        if float(change) < 1:  # Working with a Cent Coin
            if count == 1:
                print("There is {} {:.0f}c coin".format(count, float(change)*100))
            elif count > 1:
                print("There are {} {:.0f}c coins".format(count, float(change)*100))
            # else: There are no coins. Therefore, ignore

        elif 1 <= float(change) < 10:  # Working with a Rand Coin
            if count == 1:
                print("There is {} R{} coin".format(count, change))
            elif count > 1:
                print("There are {} R{} coins".format(count, change))
            # else: There are no coins. Therefore, ignore

        else:       # Working with a Rand Note
            if count == 1:
                print("There is {} R{} note".format(count, change))
            elif count > 1:
                print("There are {} R{} notes".format(count, change))
            # else: There are no notes. Therefore, ignore

    # Print total change
    print("Total change is R{:.2f}".format(var.total))


#---------
# Main
#---------
def main():
    change_arr = readFile(var.countTxt) # Could pass file path using config file
    addToDictionary(change_arr)
    outputCurrencyCount()
    input("\nPress enter to END:") # END


#----------
# Start
#----------
main() # Call main

