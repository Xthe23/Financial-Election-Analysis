import csv
import os

# File paths
input_file = "Resources/budget_data.csv"
output_file = "Analysis/financial_analysis_output.txt"

# Create the directory if it doesn't exist
if not os.path.exists("Analysis"):
    os.makedirs("Analysis")

# Open the CSV file
with open(input_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Initialize variables
    total_months = 0
    total_profit_loss = 0
    profit_loss_changes = []
    previous_profit_loss = 0
    greatest_increase = ["", 0]
    greatest_decrease = ["", 999999999999999]

    # Loop through the rows of the CSV file
    for row in csvreader:
        # Skip the header row
        if csvreader.line_num == 1:
            continue

        # Increment the total_months variable
        total_months += 1

        # Add the Profit/Loss value to the total_profit_loss variable
        total_profit_loss += int(row[1])

        # Calculate the change in Profit/Loss from the previous row
        if csvreader.line_num > 2:
            profit_loss_change = int(row[1]) - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)

            # Update greatest_increase and greatest_decrease if necessary
            if profit_loss_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = profit_loss_change
            if profit_loss_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = profit_loss_change

        # Set the previous_profit_loss variable to the current row's Profit/Loss value
        previous_profit_loss = int(row[1])

    # Calculate the average of the profit_loss_changes list
    average_profit_loss_change = sum(
        profit_loss_changes) / len(profit_loss_changes)

    # Print the required values
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_loss}")
    print(f"Average Change: ${average_profit_loss_change:.2f}")
    print(
        f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
    print(
        f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
    # Export the analysis to a text file
    with open(output_file, "w") as textfile:
        textfile.write("Financial Analysis\n")
        textfile.write("------------------\n")
        textfile.write(f"Total Months: {total_months}\n")
        textfile.write(f"Total: ${total_profit_loss}\n")
        textfile.write(f"Average Change: ${average_profit_loss_change:.2f}\n")
        textfile.write(
            f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
        textfile.write(
            f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
