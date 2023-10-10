# Python Challenge: Data Analytics
This repository contains Python scripts that analyze financial data (budget_data.csv) and election poll data (election_data.csv). The aim of the project is to showcase the ability to handle large datasets and perform comprehensive data analysis using Python.

## Table of Contents

- [PyBank Financial Analysis](#pybank-financial-analysis)
- [PyPoll Election Results](#pypoll-election-analysis)
- [Running the Scripts](#running-the-scripts)

- ## PyBank Financial Analysis
![Financial Analysis Image](https://github.com/Xthe23/python-challenge/blob/main/Images/revenue-per-lead.png)
The `budget_analysis.py` script analyzes the financial records of a company. Given a dataset with profit/loss data over several months, the script calculates:

- Total number of months in the dataset
- Net total amount of Profit/Loss
- Average change in Profit/Loss over the entire period
- Greatest increase in profits (date and amount)
- Greatest decrease in losses (date and amount)

Results:

```
Financial Analysis
------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
```

Below is a snippet of the `budget_analysis.py` file used in this project. For the complete code, please [click here](https://github.com/Xthe23/python-challenge/blob/main/PyBank/budget_analysis.py).

```python
# PyBank Financial Analysis
import csv
import os

# File paths
input_file = "Resources/budget_data.csv"
output_file = "Analysis/financial_analysis_output.txt"

# Create the directory if it doesn't exist
if not os.path.exists("Analysis"):
    os.makedirs("Analysis")
```

---

## PyPoll Election Analysis
![Election Analysis Image](https://github.com/Xthe23/python-challenge/blob/main/Images/Vote_counting.png)
The `election_analysis.py` script assists a small, rural town in modernizing its vote-counting process. Given a dataset with voter IDs, county, and candidate names, the script calculates:

- Total number of votes cast
- List of candidates who received votes
- Percentage of votes each candidate won
- Total number of votes each candidate won
- Winner of the election based on the popular vote

Results:

```
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
```



Below is a snippet of the `election_analysis.py` file used in this project. For the complete code, please [click here](https://github.com/Xthe23/python-challenge/blob/main/PyPoll/election_analysis.py).

```python
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
```
---

## Running the Scripts

Before generating the analysis results, each script checks for an `Analysis` directory in its respective location. If not found, the script will create one. This ensures that the output text files have a dedicated location.

To run the Python scripts, navigate to the directory containing the scripts and use the following commands:

For financial analysis:

```bash
python budget_analysis.py
```

For election results:

```bash
python election_analysis.py
```
