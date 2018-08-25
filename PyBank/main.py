import os
import csv

#import datetime to deal with dates column
from datetime import datetime

#Path to the budget_data.csv file. Note script is in different area than .csv
PyBankCSV = os.path.join("../..","RutgersDataBootCamp/Homework/03-Python/PyBank/Resources","budget_data.csv")

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
print(f"Financial Analysis   \n----------------------  \nTotal Months: {str(num_months)} \nTotal: ${str(totalprofit)} \nAverage Change: ${str(averageprofit)} \nGreatest Increase in Profits: {str(maxprofitdate)} (${str(maxprofit)})  \nGreatest Decrease in Profits: {str(minprofitdate)} (${str(minprofit)})")


#locate the output file
analysis_path = os.path.join("Output","Analysis.txt")


#open the output text file
with open()
