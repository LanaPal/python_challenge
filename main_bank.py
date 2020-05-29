import os
import csv

budget_data_csvpath = os.path.join("Resources", "budget_data.csv")
file_toOutput = os.path.join("", "financial_analysis.csv")

#tracking and storing
month_count = 0
total_net = 0
change_per_month = []
net_change_list = []
great_increase = ["", 0]
great_decrease = ["", 9999999999]

with open(budget_data_csvpath) as fin_data:
    csvreader = csv.reader(fin_data, delimiter=",")

    csv_header = next(csvreader)
    #first row
    first_row = next(csvreader)
    month_count += 1
    total_net +=int(first_row[1])
    prev_net = int(first_row[1])

    for row in csvreader:
        #The total number of months included in the dataset
        month_count +=1
        #The net total amount of "Profit/Losses" over the entire period
        total_net += int(row[1])
        
        #The average of the changes in "Profit/Losses" over the entire period      
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change] 
        change_per_month += [row[0]]

        #calculate increase
        if net_change > great_increase[1]:
            great_increase[0] = row[0]
            great_increase[1] = net_change

        #calculate decrease
        if net_change < great_decrease[1]:
            great_decrease[0] = row[0]
            great_decrease[1] = net_change
#average
net_month_change_average = sum(net_change_list) / len(net_change_list)


print_output = (f"Financial Analysis\n"
                f"________________________________________________\n"
                f"Total months: {month_count}\n"
                f"Net P&L: {total_net}\n"
                f"Average change: {net_month_change_average}\n"
                f"Greatest Increase in profits: {great_increase[0]} (${great_increase[1]})\n"
                f"Greatest Decrease in profits: {great_decrease[0]} (${great_decrease[1]})\n")


print(print_output)
with open(file_toOutput, "w") as txt_file:
    txt_file.write(print_output)


   
