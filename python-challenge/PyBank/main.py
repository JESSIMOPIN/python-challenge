#PyBank Instructions
#In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".
#Your task is to create a Python script that analyzes the records to calculate each of the following values:
#•	The total number of months included in the dataset
#•	The net total amount of "Profit/Losses" over the entire period
#•	The changes in "Profit/Losses" over the entire period, and then the average of those changes
#•	The greatest increase in profits (date and amount) over the entire period
#•	The greatest decrease in profits (date and amount) over the entire period

import csv
with open ('./Starter_Code/PyBank/resources/budget_data.csv') as pybank:
    csvreader=csv.reader (pybank)
    header=next(csvreader)

    #Lists

    total_number_months= []
    net_profit_losses=[]
    changes_profit_losses=[]
    average_changes=[]
    greatest_increase_profit=[]
    greatest_decrease_profit=[]

#iteration to iterate on the data and return an outcome
    for row in pybank:
        total_number_months.append(row[0])
        net_profit_losses.append(int(row[0]))
        
#changes 
changes_profit_losses= + row["Profit/Losses"]

#average
mean=(changes_profit_losses)

greatest_increase_profit=max (changes_profit_losses)
greatest_increase_profit=min(changes_profit_losses)



