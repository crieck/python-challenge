import pandas as pd

#Reads CSV file in local directory to pandas DataFrame & appends new column for month-to-month change
df = pd.read_csv('election_data.csv', names=['Voter_ID','County','Candidate'], header=0, index_col=0)

#Calculates total votes
totVotes = len(df.index)

#Groups count of vote for each candidate, puts output into new DataFrame
candVotes = df.groupby('Candidate').size().sort_values(ascending=False).reset_index(name='Votes')

#Pulls vote totals for each candidate
votesK = candVotes.at[0,'Votes']
votesC = candVotes.at[1,'Votes']
votesL = candVotes.at[2,'Votes']
votesO = candVotes.at[3,'Votes']

#Computes percentage share of total vote for each candidate
shareK = (votesK / totVotes) * 100
shareC = (votesC / totVotes) * 100
shareL = (votesL / totVotes) * 100
shareO = (votesO / totVotes) * 100

#Creates variable to hold list of output lines
outputLines = [
    '|----------------------------------------|',                                         
    '|         ELECTION RESULTS SUMMARY       |',
    '|                                        |',
    '|----------------------------------------|',
    '|Total Votes:            ' + f"{totVotes:,.0f}" + '       |',
    '|----------------------------------------|',
    '|Khan:        ' + f"{shareK:,.03f}" + '%    ' + f"{votesK:,.0f}" + '       |',
    '|Correy:      ' + f"{shareC:,.03f}" + '%      ' + f"{votesC:,.0f}" + '       |',
    '|Li:          ' + f"{shareL:,.03f}" + '%      ' + f"{votesL:,.0f}" + '       |',
    '|O\'Tooley:     ' + f"{shareO:,.03f}" + '%      ' + f"{votesO:,.0f}" + '       |',
    '|----------------------------------------|',
    '|             WINNER: KHAN               |',
    '|----------------------------------------|']

#Prints output line by line
print(*outputLines, sep='\n')

#Writes output to text file in local directory ***If file already exists, it will be overwritten***
with open('electionResults.txt', mode='w') as outfile:  
    for s in outputLines:
        outfile.write('%s\n' % s)