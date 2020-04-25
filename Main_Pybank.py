# First we'll import the os module
# This will  us to allowcreate file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Method 2: Improved Reading using CSV module

# First solution
#Total_number_of_months = 0
#Net_total_amount = 0
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #for row in csvreader:
        #Total_number_of_months += 1
        #float_current_amount = float(row[1])
        #Net_total_amount += float_current_amount
       
    #print("Financial Analysis")
    #print("--------------------------------")
    #print("Total months is:",Total_number_of_months)
    #print("Total: $",Net_total_amount)
    
    # Alternate and cleaner solution
    total_profit_loss = []
    date = []
    Change_in_profit = []

    # Appending
    for row in csvreader:
        total_profit_loss.append(float(row[1]))
        date.append(row[0]) 
    print("Total Months is:", len(date))
    print("Total : $", sum(total_profit_loss))
    
 # Total profit and loss Change_in_profit. 
    for i in range(1,len(total_profit_loss)):
        Change_in_profit.append(total_profit_loss[i] - total_profit_loss[i-1])   
        avg_change = sum(Change_in_profit)/len(Change_in_profit)

 # maximum Change_in_profit and maximum loss Change_in_profit
        max_profit_loss_change = max(Change_in_profit)

        min_profit_loss_change = min(Change_in_profit)

 # Add 1 to match the date position and the postion where 
 # maximum change_in_profit occured i.e change_in_profit[i]
        max_change_date = str(date[Change_in_profit.index(max(Change_in_profit))+1])
        min_change_date = str(date[Change_in_profit.index(min(Change_in_profit))+1])


    print("Average Revenue Change: $", avg_change)
    print("Greatest Increase in Profits:", max_change_date,"($", max_profit_loss_change,")")
    print("Greatest Decrease in Profits:", min_change_date,"($", min_profit_loss_change,")")






    