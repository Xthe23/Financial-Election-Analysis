# Python Challenge: Data Analytics
This repository contains Python scripts that analyze financial data (budget_data.csv) and election poll data (election_data.csv). The aim of the project is to showcase the ability to handle large datasets and perform comprehensive data analysis using Python.

## Table of Contents

- [PyBank Financial Analysis](#pybank-financial-analysis)
- [PyPoll Election Results](#pypoll-election-results)
- [Running the Scripts](#running-the-scripts)

- ## PyBank Financial Analysis

The `budget_analysis.py` script analyzes the financial records of a company. Given a dataset with profit/loss data over several months, the script calculates:

- Total number of months in the dataset
- Net total amount of Profit/Loss
- Average change in Profit/Loss over the entire period
- Greatest increase in profits (date and amount)
- Greatest decrease in losses (date and amount)

![Financial Analysis Image](https://github.com/Xthe23/python-challenge/blob/main/Images/revenue-per-lead.png)

---

## PyPoll Election Results

The `election_analysis.py` script assists a small, rural town in modernizing its vote-counting process. Given a dataset with voter IDs, county, and candidate names, the script calculates:

- Total number of votes cast
- List of candidates who received votes
- Percentage of votes each candidate won
- Total number of votes each candidate won
- Winner of the election based on the popular vote

![Election Analysis Image](https://github.com/Xthe23/python-challenge/blob/main/Images/Vote_counting.png)

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
