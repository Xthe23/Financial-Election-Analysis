import csv
import os

# File paths
input_file = "Resources/election_data.csv"
output_file = "Analysis/election_analysis_output.txt"

# Create the directory if it doesn't exist
if not os.path.exists("Analysis"):
    os.makedirs("Analysis")

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winning_votes = 0

# Read the csv file
with open(input_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip header row

    # Process each row
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidates:
            candidates[candidate_name] = 0
        candidates[candidate_name] += 1

# Write the results to terminal and text file
with open(output_file, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")

    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
        print(f"{candidate}: {percentage:.3f}% ({votes})")

        if votes > winning_votes:
            winning_votes = votes
            winner = candidate

    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")

    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")
