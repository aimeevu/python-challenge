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
    totalChange = 0
    greatestIncrease = 0 #Month - previous month
    greatestDecrease = 0

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

        for x in profitLoss:
            currentMonthValue = int(x)
            netTotal += currentMonthValue
            change = currentMonthValue - previousMonthValue
            profitLossChange.append(change)
            previousMonthValue = currentMonthValue
        
        totalChange = sum(profitLossChange)
        averageProfitLoss = totalChange / len(profitLossChange)

    print(totalMonths)
    print(netTotal)
    print(date[0])
    print(profitLossChange[1])
    print(averageProfitLoss)

PyBankAnalysis()
