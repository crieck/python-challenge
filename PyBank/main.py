import pandas as pd

#Reads CSV file in local directory to pandas DataFrame & appends new column for month-to-month change
df = pd.read_csv('budget_data.csv', names=['Month','Profit'], header=0, index_col=0)
df['Change'] = df['Profit'].diff()

#Uses pandas to calculate & store needed values into variables
totMonth = len(df.index)
totProfit = df['Profit'].sum()
avgMonthlyChange = df['Change'].sum() / (totMonth - 1)
maxInc = df['Change'].max()
minDec = df['Change'].min()
monthInc = df['Change'].idxmax()
monthDec = df['Change'].idxmin()

#Creates variable to hold list of output lines
outputLines = [
    '|--------------------------------------------|',                                         
    '|          SUMMARY FINANCIAL ANALYSIS        |',
    '|                                            |',
    '|--------------------------------------------|',
    '|Total Months:                        ' + str(totMonth) + '     |',
    '|                                            |',
    '|Total Profit:                  $ ' + f"{totProfit:,d}" + ' |',
    '|                                            |',
    '|Average Monthly Change:         $ ' + f"{avgMonthlyChange:,.02f}" + ' |',
    '|                                            |',
    '|Greatest Increase: ' + str(monthInc) + '     $ ' + f"{maxInc:,.0f}" + ' |',
    '|                                            |',
    '|Greatest Decrease: ' + str(monthDec) + '    $ ' + f"{minDec:,.0f}" + ' |',
    '|                                            |',
    '|--------------------------------------------|']

#Prints output line by line
print(*outputLines, sep='\n')

#Writes output to text file in local directory ***If file already exists, it will be overwritten***
with open('summaryAnalysis.txt', mode='w') as outfile:  
    for s in outputLines:
        outfile.write('%s\n' % s)