import os
import csv

#import datetime to deal with dates column
from datetime import datetime

#Path to the budget_data.csv file. Note script is in different area than .csv
PyBankCSV = os.path.join("Resources","budget_data.csv")

#create lists to store the two columns of CSV data
dates = []
profit_loss = []

#set total profit to 0 to start
totalprofit = 0

#set max and min profit variables
maxprofit = 0
minprofit = 0

#define a function that gives the sum of the profit and losses
#def summary(ProfitBank):

    
    

#Read CSV file using "with open" and csv module
with open(PyBankCSV, newline="") as csvfile:
    
    #specify delimiter and holder of contents
    Bankreader = csv.reader(csvfile, delimiter=",")
    
    #Read the header row first.
    bank_header = next(Bankreader)
    
    
    #for loop to gather data into the lists
    for row in Bankreader:
        
        #put dates in list
        monthdate = datetime.strptime((row[0]),'%b-%Y').strftime('%Y/%m')
        dates.append(monthdate)
 

        #put profit and loss in list
        profit_loss.append(row[1])
        
        #set totalprofit to iteratively add per loop
        totalprofit = totalprofit + int(row[1])
        
        #get max profit and date by iteratively comparing to current row
        if int(row[1]) > maxprofit:
            maxprofit = int(row[1])
            maxprofitdate = datetime.strptime((row[0]),'%b-%Y').strftime('%Y/%m')
        
        #get min profit and date by iteratively comparing to current row
        if int(row[1]) < minprofit:
            minprofit = int(row[1])
            minprofitdate = datetime.strptime((row[0]),'%b-%Y').strftime('%Y/%m')
        
#Calculate the average profit
averageprofit = totalprofit / len(profit_loss)

#calculate the total number of months
num_months = len(dates)

#print the results to the terminal
print("Financial Analysis")
print("----------------------")
print(f"Total Months: {str(num_months)}")
print(f"Total: ${str(totalprofit)}")
print(f"Average Change: ${str(averageprofit)}")
print(f"Greatest Increase in Profits: {str(maxprofitdate)} (${str(maxprofit)})")
print(f"Greatest Decrease in Profits: {str(minprofitdate)} (${str(minprofit)})")

#locate the output file
analysis_path = os.path.join("Output","Analysis.txt")


#open the output text file and write lines to file
Bankout = open(analysis_path, "w")
Bankout.write("Financial Analysis\n")
Bankout.write("----------------------\n")
Bankout.write(f"Total Months: {str(num_months)}\n")
Bankout.write(f"Total: ${str(totalprofit)}\n")
Bankout.write(f"Average Change: ${str(averageprofit)}\n")
Bankout.write(f"Greatest Increase in Profits: {str(maxprofitdate)} (${str(maxprofit)})\n")
Bankout.write(f"Greatest Decrease in Profits: {str(minprofitdate)} (${str(minprofit)})\n") 
Bankout.close()
