# 1 tsp = 5 ml
# 1 TBL = 15 ml
# 1 Cup = 240 ml

# the function must be defined before it may be used
# tsp will behave as a local variable
teaspoon = 0
tablespoon = 0
cup = 0
runAgain = ' '


def convert(mils):
    teaspoon = round((float(mils) * 0.2), 2)
    return teaspoon


print("This program will convert milliliters to teaspoons, tablespoons, and cups.\n")

while runAgain != 'q':  # entering q will quit the program
    # accept user input
    milliliters = raw_input("How many milliliters do you wish to convert? \n")

    # call the function
    teaspoon = convert(milliliters)

    print (milliliters + " Milliliters is equal to " + str(teaspoon) + " teaspoons.\n")
    if teaspoon >= 3:
        if teaspoon < 48:
            tablespoon = teaspoon / 3
            print (str(teaspoon) + " teaspoons = " + str(tablespoon) + " tablespoons.")
        else:
            cup = teaspoon / 48
            print (str(teaspoon) + " teaspoons = " + str(cup) + " cups.")

    print("\nWould you like to try again? ")  # ask user if they would like to try again
    print("Enter 'q' for 'quit' or press enter to continue: ")  # explain how to quit or to continue
    runAgain = raw_input()  # accept input to determine if user wants to go again

# program wrap-up
print("\nThanks for running my Baking Conversion program! Goodbye!")
