import os
import csv

# In this challenge, you are tasked with creating a Python script 
# to analyze the financial records of your company. You will give a
# set of financial data called budget_data.csv. The dataset is
# composed of two columns: "Date" and "Profit/Losses".
def PyBankAnalysis():
    # Variable Declaration and Initialization for entire function
    csvPath = os.path.join('Resources', 'budget_data.csv')
    date = []
    profitLoss = []
    profitLossChange = []
    totalMonths = 0
    netTotal = 0
    averageProfitLoss = 0
    greatestIncrease = 0
    greatestDecrease = 0
    greatestIncreaseDate = ""
    greatestDecreaseDate = ""

    # Reads CSV File budget_data.csv
    with open(csvPath) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        next(csvReader) # Skips first row of column names

        # Loads data into corresponding lists for further analysis
        for row in csvReader:
            date.append(row[0])
            profitLoss.append(row[1])
        
        # Variable Declaration and Initialization for with statement
        totalMonths = len(date)
        change = 0
        previousMonthValue = 0
        countForDateList = 0

        # Calculates change between entries and loads values into a new list and identifies greatest increase/decrease
        for x in profitLoss:
            currentMonthValue = int(x)
            netTotal += currentMonthValue
            change = currentMonthValue - previousMonthValue
            profitLossChange.append(change)
            previousMonthValue = currentMonthValue

            # Identifies greatest increase between entries
            if change > greatestIncrease:
                greatestIncrease = change
                greatestIncreaseDate = date[countForDateList]

            # Identifies greatest decrease between entries
            if change < greatestDecrease:
                greatestDecrease = change
                greatestDecreaseDate = date[countForDateList]

            # Incremental variable to recall date for a particular iteration
            countForDateList += 1

        # Calculates average of profit/loss changes
        averageProfitLoss = round(sum(profitLossChange) / len(profitLossChange), 2)

    # Prints analysis to terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {str(totalMonths)}")
    print(f"Total: {str(netTotal)}")
    print(f"Average Change: {str(averageProfitLoss)}")
    print(f"Greatest Increase in Profits: {greatestIncreaseDate} (${str(greatestIncrease)})")
    print(f"Greatest Decrease in Profits: {greatestDecreaseDate} (${str(greatestDecrease)})")

    # Writes analysis to text file
    outputFile = os.path.join("Analysis", "PyBank_Analysis.txt")

    f = open(outputFile, "w")
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write("Total Months: " + str(totalMonths) + "\n")
    f.write("Total: " + str(netTotal) + "\n")
    f.write("Average Change: " + str(averageProfitLoss) + "\n")
    f.write("Greatest Increase in Profits: " + greatestIncreaseDate + " ($" + str(greatestIncrease) + ")\n")
    f.write("Greatest Decrease in Profits: " + greatestDecreaseDate + " ($" + str(greatestDecrease) + ")\n")

    f.close()

# Calls to function
PyBankAnalysis()
