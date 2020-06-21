#Import modules
import os
import csv

#Create import path variable
csv_path = os.path.join('Resources','budget_data.csv')

#Initalize variables
TotalNumMonths = 0
NetTotalProfitLossesAllPeriods = int(0)
ChangeInProfitLosses = int(0)
GreatestIncreaseProfitsDate = int(0)
GreatestIncreaseProfitsAmount = int(0)
GreatestDecreaseLossesDate = int(0)
GreatestDecreaseLossesAmount = int(0)
AverageChange = int(0)

#Open csv file in read mode and apply handle
with open(csv_path, 'r') as csv_file:
    #Create recordsource variable with python csv.reader delimiting function
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Row 1 header function
    csv_header = next(csv_reader)

    #Iterate thru recordsource
    for row in csv_reader:
       #Increase number of months counter
       TotalNumMonths += 1
       #Add profit/loss to aggregate
       NetTotalProfitLossesAllPeriods += int(row[1])
       #Check for greatest profit month
       if int(row[1]) > GreatestIncreaseProfitsAmount:
            GreatestIncreaseProfitsDate = row[0]
            GreatestIncreaseProfitsAmount = int(row[1])
       #Check for greatest losses month
       if int(row[1]) < GreatestDecreaseLossesAmount:
            GreatestDecreaseLossesDate = row[0]
            GreatestDecreaseLossesAmount = int(row[1])

#Calculate average change            
AverageChange = (GreatestIncreaseProfitsAmount-GreatestDecreaseLossesAmount)/TotalNumMonths

#Apply currency formatting
currencyNetTotalProfitLossesAllPeriods = "${:,.2f}".format(NetTotalProfitLossesAllPeriods)
currencyAverageChange = "${:,.2f}".format(AverageChange)
currencyGreatestIncreaseProfitsAmount = "${:,.2f}".format(GreatestIncreaseProfitsAmount)
currencyGreatestDecreaseLossesAmount = "${:,.2f}".format(GreatestDecreaseLossesAmount)

#Print results
print(f"Total Months: {str(TotalNumMonths)}")
print(f"Total: {str(currencyNetTotalProfitLossesAllPeriods)}")
print(f"Average Change: {str(currencyAverageChange)}")
print(f"Greatest Increase in Profits: {str(GreatestIncreaseProfitsDate)} {str(currencyGreatestIncreaseProfitsAmount)}")
print(f"Greatest Decrease in Profits: {str(GreatestDecreaseLossesDate)} {str(currencyGreatestDecreaseLossesAmount)}")

#Output to new file section

#Output to new file section

#Create zip variables
statistics = ["Total Months:","Total:","Average Change:","Greatest Increase in Profits:","Greatest Decrease in Losses:"]
results = [TotalNumMonths, currencyNetTotalProfitLossesAllPeriods, currencyAverageChange, currencyGreatestIncreaseProfitsAmount, currencyGreatestDecreaseLossesAmount]
roster = zip(statistics, results)

#Create export path variable
output_path = os.path.join("analysis","new.csv")

#Open csv file in write mode and apply handle
with open(output_path, 'w', newline='') as csv_file:
    #Create output recordsource variable with python csv.writer delimiting function
    csv_writer = csv.writer(csv_file, delimiter=',')
    #Output header row 1
    csv_writer.writerow(["Statistics","Results"])
    #Output statistics and results
    csv_writer.writerows(roster)


