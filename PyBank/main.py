### UCI Data Analytics Bootcamp: Homework 3 - Python Challenge
# Main script for PyBank Analysis
# Author: Sunwoo Kim
# Files: main.py, budget_data.csv

# Headers

title_header = "Financial Analysis"
line_header = "---------------------"
months_header = "Total Months:"
total_header = "Total:"
change_header = "Average Change:"
greatest_inc_header = "Greatest Increase in Profits:"
greatest_dec_header = "Greatest Decrease in Profits:"
nl = "\n"

# Dependencies

import os
import csv

# Specifying file path

csvpath = os.path.join('Resources', 'budget_data.csv')

# Reading csv file

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Skip header

    next(csvreader)

    # Organize column data into two lists: one for the dates, one for profits/
    # losses

    dates = []
    profits_losses = []

    for row in csvreader:
        dates.append(row[0])
        profits_losses.append(int(row[1]))

    # Count total number of Months

    total_months = len(dates)

    # Calculate net total amount of profit/losses

    net_total = sum(profits_losses)

    # Calculate average change

    changes = []

    for i in range(total_months-1):
        change = (profits_losses[i] - profits_losses[i+1])*(-1)
        changes.append(change)

    avg_change = round(sum(changes)/(total_months-1),2)

    # Find largest increase and decrease

    greatest_increase = profits_losses[0]
    greatest_decrease = profits_losses[0]
    GI_month = dates[0]
    GD_month = dates[0]

    for i in range(total_months):
        if profits_losses[i] > greatest_increase:
            greatest_increase = profits_losses[i]
            GI_month = dates[i]
        if profits_losses[i] < greatest_decrease:
            greatest_decrease = profits_losses[i]
            GD_month = dates[i]

    # Print analysis to the terminal
    month_result = f"{months_header} {total_months}"
    total_result = f"{total_header} ${net_total}"
    change_result = f"{change_header} ${avg_change}"
    increase_result = f"{greatest_inc_header} {GI_month} (${greatest_increase})"
    decrease_result = f"{greatest_dec_header} {GD_month} (${greatest_decrease})"
    print(title_header)
    print(line_header)
    print(month_result)
    print(total_result)
    print(change_result)
    print(increase_result)
    print(decrease_result)

    # Print analysis to text file

    analysis_file = open("analysis/pybank-analysis.txt","w")
    lines = [title_header + nl, line_header + nl, month_result + nl,
             total_result + nl, change_result + nl, increase_result + nl,
             decrease_result + nl]
    analysis_file.writelines(lines)
    analysis_file.close()
