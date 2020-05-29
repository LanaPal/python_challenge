import os
import csv

budget_data_csvpath = os.path.join("Resources", "budget_data.csv")
file_toOutput = os.path.join("", "financial_analysis.csv")

#assign key variables
month_count = 0
total_pnl = 0
change_per_month = []
net_change_list = []
increase = ["", 0]
decrease = ["", 9999999999]

with open(budget_data_csvpath) as fin_data:
    csvreader = csv.reader(fin_data, delimiter=",")

    csv_header = next(csvreader)
    first_row = next(csvreader)
    month_count += 1
    total_pnl +=int(first_row[1])
    prev_pnl = int(first_row[1])

    for row in csvreader:
        #The total number of months included in the dataset
        month_count +=1
        #The net total amount of "Profit/Losses" over the entire period
        total_pnl += int(row[1])
        
        #The average of the changes in p&L over the entire period      
        net_change = int(row[1]) - prev_pnl
        prev_pnl = int(row[1])
        net_change_list += [net_change]
        change_per_month += [row[0]]

        #calculate increase
        if net_change > increase[1]:
            increase[0] = row[0] #increase month in array
            increase[1] = net_change #increase by one

        #calculate decrease
        if net_change < decrease[1]:
            decrease[0] = row[0] #increase month in array
            decrease[1] = net_change #increase by one
#average
net_month_change_average = sum(net_change_list) / len(net_change_list)


print_output = (f"Financial Analysis\n"
                f"________________________________________________\n"
                f"Total months: {month_count}\n"
                f"Net P&L: {total_pnl}\n"
                f"Average change: {net_month_change_average}\n"
                f"Greatest Increase in profits: {increase[0]} (${increase[1]})\n"
                f"Greatest Decrease in profits: {decrease[0]} (${decrease[1]})\n")


print(print_output)
with open(file_toOutput, "w") as txt_file:
    txt_file.write(print_output)