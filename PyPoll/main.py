import os
import csv

# In this challenge, you are tasked with helping a small, 
# rural town modernize its vote counting process.
# You will be given a set of poll data called election_data.csv.
# The dataset is composed of three columns: "Voter ID", "County",
# and "Candidate". 
def PyPollAnalysis():
    # Variable Declaration and Initialization for entire function
    csvPath = os.path.join('Resources', 'election_data.csv')
    totalVotes = 0
    candidateDict = {}
    winner = ""

    # Reads CSV File election_data.csv
    with open(csvPath) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        next(csvReader) # Skips first row of column names

        # Loads data into dictionary
        for row in csvReader:
            totalVotes += 1
            if row[2] in candidateDict.keys(): # If key already exists
                candidateDict[row[2]][0] += 1
            else: # If key doesn't exist
                candidateDict[row[2]] = [1]

        # Calculates vote percentage and identifies winner
        greatestCount = 0
        for candidate in candidateDict:
            candidateDict[candidate] += [round(((candidateDict[candidate][0] / totalVotes)*100),3)]

            # Checks if current candidate has the greatest count
            if candidateDict[candidate][0] > greatestCount:
                greatestCount = candidateDict[candidate][0]
                winner = candidate

    # Prints election results to terminal
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {str(totalVotes)}")
    print("-------------------------")
    for candidate in candidateDict:
        print(f"{candidate}: {candidateDict[candidate][1]}% ({candidateDict[candidate][0]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    # Writes election results to text file
    outputFile = os.path.join("Analysis", "PyPoll_Analysis.txt")

    f = open(outputFile, "w")
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {str(totalVotes)}\n")
    f.write("-------------------------\n")
    # Loops through dictionary to print all key-value pairs
    for candidate in candidateDict:
        f.write(f"{candidate}: {candidateDict[candidate][1]}% ({candidateDict[candidate][0]})\n")
    f.write("-------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("-------------------------\n")

    f.close()

# Calls to function
PyPollAnalysis()
