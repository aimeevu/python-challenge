import os
import csv

def PyBankAnalysis():
    csvPath = os.path.join('Resources', 'budget_data.csv')
    date = []
    profitLoss = []
    profitLossChange = []
    totalMonths = 0
    netTotal = 0
    averageProfitLoss = 0
    greatestIncrease = 0 #Month - previous month
    greatestDecrease = 0
    greatestIncreaseDate = ""
    greatestDecreaseDate = ""

    with open(csvPath) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        for row in csvReader:
            date.append(row[0])
            profitLoss.append(row[1])
        
        date.pop(0)
        profitLoss.pop(0)

        totalMonths = len(date)
        change = 0
        previousMonthValue = 0
        countForDateList = 0

        for x in profitLoss:
            currentMonthValue = int(x)
            netTotal += currentMonthValue
            change = currentMonthValue - previousMonthValue
            profitLossChange.append(change)
            previousMonthValue = currentMonthValue

            if change > greatestIncrease:
                greatestIncrease = change
                greatestIncreaseDate = date[countForDateList]

            if change < greatestDecrease:
                greatestDecrease = change
                greatestDecreaseDate = date[countForDateList]

            countForDateList += 1

        averageProfitLoss = sum(profitLossChange) / len(profitLossChange)

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(totalMonths))
    print("Total: " + str(netTotal))
    print("Average Change: " + str(averageProfitLoss))
    print("Greatest Increase in Profits: " + greatestIncreaseDate + " ($" + str(greatestIncrease) + ")")
    print("Greatest Decrease in Profits: " + greatestDecreaseDate + " ($" + str(greatestDecrease) + ")")

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

def PyPollAnalysis():
    print("This is for PyPoll")

PyBankAnalysis()
PyPollAnalysis()
