#https://www.kaggle.com/kashnitsky/topic-1-exploratory-data-analysis-with-pandas

#dependencies
import pandas as pd

#import csv, convert to df
data_file = "Resources/election_data.csv"
data_file_df = pd.read_csv(data_file)

#The total number of votes cast
votes_cast = len(data_file_df["Voter ID"])

#(Primitive) fraud check: number of unique voter IDs
Unique_IDs = data_file_df['Voter ID'].nunique()
if votes_cast == Unique_IDs:
    fraud_check = "One person, one vote"
elif votes_cast > Unique_IDs:
    fraud_check = "Repeat voters found"
else:
    fraud_check = "Some voters couldn't decide?"

#A complete list of candidates who received votes (not used for anything)
all_candidates = data_file_df["Candidate"].unique()

#The total number of votes each candidate won
votes = data_file_df['Candidate'].value_counts()
votes_df = pd.DataFrame({'Candidate':votes.index, 'Votes':votes.values})

#The percentage of votes each candidate won
vote_percentage = round(100*(votes/votes_cast))
vote_percentage_df = pd.DataFrame({'Candidate':vote_percentage.index, 'Votes(%)':vote_percentage.values})

#Make summary table
summary_df = pd.merge(vote_percentage_df, votes_df, on='Candidate')
summary_df.set_index('Candidate', inplace=True)
summary_df = summary_df.rename_axis(None)

#The winner of the election based on popular vote.
max_votes = votes_df['Votes'].idxmax(axis=0)
candidate = pd.Series(votes_df['Candidate'])

#Votes by county: looks like Khan won decisively everywhere, not too interesting
votes_by_county = pd.crosstab(data_file_df['County'], data_file_df['Candidate'], normalize = True, margins = True)

#Print results to terminal
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {votes_cast}")
print(f"Unique Voter IDs: {Unique_IDs}")
print(f"{fraud_check}")
print(f"-------------------------")
print(summary_df)
print(f"*************************")
print(f"Winner: {candidate[max_votes]}")
print(f"*************************")
print(f"   ")
print(f"Results by County")
print(f"   ")
print(votes_by_county)

#Print results to text file
def main():
    f=open("/Users/bmacgreg/Documents/Bootcamp/Homework_3/python-challenge/PyPoll/Analysis/PyPoll.txt", "w+")
    f.write(f"Election Results\r\n")
    f.write(f"-------------------------\r\n")
    f.write(f"Total Votes: {votes_cast}\r\n")
    f.write(f"Unique Voter IDs: {Unique_IDs}\r\n")
    f.write(f"{fraud_check}\r\n")
    f.write(f"-------------------------\r\n")
    f.write(f"{summary_df.to_string()}\r\n")
    f.write(f"*************************\r\n")
    f.write(f"Winner: {candidate[max_votes]}\r\n")
    f.write(f"*************************\r\n")
    f.write(f"   \r\n")
    f.write(f"Results by County\r\n")
    f.write(f"   \r\n")
    f.write(f"{votes_by_county}\r\n")
if __name__=="__main__":
        main()
