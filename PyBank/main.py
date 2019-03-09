# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#Set path of CSV file to be read
csvpath = ('budget_data.csv')

#Set initial variable balance to zero
months = 0
totalamount = 0
yoy = []
data = {"month": [], "profit" : []}

# Read in CSV 
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    
    #loop though open CSV, calculate months, totalamount, and append data dictionary which we will use for further calculations
    for row in csvreader:
            months +=  1
            totalamount += int(row[1])
            data["month"].append(row[0])
            data["profit"].append(row[1])

#cast totalamount in currnecy format
totalamount = '${:,.2f}'.format(totalamount)

#convert the dictionary elements for profit into a list
profit_values = data["profit"]

#Loop through elements to create values for yoy change
for i in range(0,months):
        #skip the first change calculation since theres no back data to use to determine the variance
        if i == 0:
            next
        #special case for the last month, so nothing goes out of range... the minus 1 is needed because the lists are slightly different sizes (by 1)
        elif i == months-1:
            prev = profit_values[i-1]
            current = profit_values[i]
            nxt = 0
            change = int(current) - int(prev)
            yoy.append(int(change))
        #calculate the variances from month to month and append them into a list ---- this is where most of the work is being done
        else:
            prev = profit_values[i-1]
            current = profit_values[i]
            nxt = profit_values[i+1]
            change = int(current) - int(prev)
            yoy.append(int(change))

#Calculate the average yoy change
avg_change = sum(yoy)/len(yoy)
if avg_change >= 0:
    avg_change = '${:,.2f}'.format(avg_change)
else:
    avg_change = '-${:,.2f}'.format(-avg_change)

#Calculate the max and min change
maxchange = max(yoy)
minchange = min(yoy)

#Cast max and min in currency format
maxchange = '${:,.2f}'.format(maxchange)
minchange = '-${:,.2f}'.format(-minchange)

#Get month that max and min occured in
max_profit_index = yoy.index(max(yoy))+1
min_profit_index = yoy.index(min(yoy))+1
max_profit_month = data["month"][max_profit_index]
min_profit_month = data["month"][min_profit_index]

#print results to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: {totalamount}")
print(f"Average Change: {avg_change}")
print(f"Greatest Increase in Profits: {max_profit_month} ({maxchange})")
print(f"Greatest Decrease in Profits: {min_profit_month} ({minchange})")

#export results to Text file
# Specify the file to write to
output_path = os.path.join("Financial Results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as text_file:

    # Write the financial results to the CSV
    text_file.write ("Financial Analysis\n")
    text_file.write ("----------------------------\n")
    text_file.write (f"Total Months: {months}\n")
    text_file.write (f"Total: {totalamount}\n")
    text_file.write (f"Average Change: {avg_change}\n")
    text_file.write (f"Greatest Increase in Profits: {max_profit_month} ({maxchange})\n")
    text_file.write (f"Greatest Decrease in Profits: {min_profit_month} ({minchange})\n")

