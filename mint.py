import datetime
import pandas as pd
from calendar import monthrange


#Standard tandard Mint transaction CSV file
CSV_LOCATION = r'transactions.csv'

#Import CSV file
masterFrame = pd.read_csv(CSV_LOCATION)

#Reset dates to standard format
masterFrame.Date = pd.to_datetime(masterFrame.Date)


#Parse down dataframe for the month requested
def getDebitsForMonth(year, month):
    numberOfDaysInMonth = str(monthrange(year, month)[1])
    year = str(year)
    month = str(month)
    parsedData = masterFrame[(masterFrame['Date'] >= year + '-' + month + '-01') & (masterFrame['Date'] <= year + '-' + month + '-' + numberOfDaysInMonth)]

    getDebits(parsedData)

#Find all debits in a dataframe that are not credit card payments or transfers between accounts
def getDebits(dataToParse):
    allDebits = dataToParse[(dataToParse['Transaction Type'] == 'debit') & (dataToParse['Category'] != 'Credit Card Payment') & (dataToParse['Category'] != 'Transfer')]
    print(allDebits.sort_values(['Amount'], ascending=False))
    print("Total Amount of Debits: " + str(len(allDebits.index)))
    print("Total Spent: " + str(allDebits['Amount'].sum()))


#Return sample for March of 2020
print("March: ")
getDebitsForMonth(2020,3)

