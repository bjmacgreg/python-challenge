#References
#https://www.guru99.com/reading-and-writing-files-in-python.html

#dependencies
import pandas as pd
import os.path

#import csv, convert to df
data_file = "Resources/budget_data.csv"
data_file_df = pd.read_csv(data_file)

#remove header, count entries
data_file_df.head()
count = len(data_file_df["Date"])

#find net profit/loss
Net_profit_loss = data_file_df["Profit/Losses"].sum()

#find monthly changes in profit/loss, excluding Jan-10 
r= 1
while r <= 85:
    data_file_df.loc[r,"Previous Profit/Losses"] = data_file_df.loc[r-1, "Profit/Losses"]    
    r=r+1
data_file_df['Change in Profit/Losses, exclude Jan-10'] = data_file_df['Profit/Losses'].sub(data_file_df['Previous Profit/Losses'])
change_no_Jan10 = pd.Series(data_file_df['Change in Profit/Losses, exclude Jan-10'])  

#find monthly changes in profit/loss, including Jan-10 
data_file_df.loc[0,"Previous Profit/Losses"] = 0
r= 1
while r<=85:
    data_file_df.loc[r,"Previous Profit/Losses"] = data_file_df.loc[r-1, "Profit/Losses"]    
    r=r+1
data_file_df['Change in Profit/Losses'] = data_file_df['Profit/Losses'].sub(data_file_df['Previous Profit/Losses'])
change = pd.Series(data_file_df['Change in Profit/Losses'])  

#find biggest monthly gain and loss
max = data_file_df['Change in Profit/Losses'].idxmax(axis=0)
min = data_file_df['Change in Profit/Losses'].idxmin(axis=0)

#find months of biggest monthly gain and loss
date = pd.Series(data_file_df['Date'])  

#print to terminal
print(f"Financial Analysis")
print(f"---------------------------------------")
print(f"Total Months: {count}")
print(f"Total: ${Net_profit_loss}") 
print(f"Average change including Jan-10 (maybe was new company): ${round(data_file_df['Change in Profit/Losses'].mean(), 2)}")
print(f"Average change excluding Jan-10: ${round(data_file_df['Change in Profit/Losses, exclude Jan-10'].mean(), 2)}")
print(f"Greatest Increase in Profits: {date[max]} (${int(change[max])})")
print(f"Greatest Decrease in Profits: {date[min]} (${int(change[min])})")

#print to text file

def main():
    f=open('/Users/bmacgreg/Documents/Bootcamp/Homework_3/python-challenge/PyBank/Analysis/PyBank.txt', "w+")
    f.write(f"Financial Analysis\r\n")
    f.write(f"---------------------------------------\r\n")
    f.write(f"Total Months: {count}\r\n")
    f.write(f"Total: ${Net_profit_loss}\r\n") 
    f.write(f"Average change including Jan-10 (maybe was new company): ${round(data_file_df['Change in Profit/Losses'].mean(), 2)}\r\n")
    f.write(f"Average change excluding Jan-10: ${round(data_file_df['Change in Profit/Losses, exclude Jan-10'].mean(), 2)}\r\n")
    f.write(f"Greatest Increase in Profits: {date[max]} (${int(change[max])})\r\n")
    f.write(f"Greatest Decrease in Profits: {date[min]} (${int(change[min])})\r\n")
if __name__=="__main__":
        main()
