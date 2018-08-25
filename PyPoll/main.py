#import modules
import os
import csv

#import collections to get "Counter"
from collections import Counter, OrderedDict

#Path to the election_data.csv file
PyPollCSV = os.path.join("Resources","election_data.csv")

#create lists to store the three columns of CSV data
#create list of unique candidates so we can then tally info
voterID = []
County = []
candidateList = []


#create variables showing the vote counts
Totalvotes = 0


#Read CSV file using "with open" and csv module
with open(PyPollCSV, newline="") as csvfile:
    
    Pollreader = csv.reader(csvfile, delimiter=",")
    
    #read the header row first
    poll_header = next(Pollreader)
    
    #for loop to process CSV file and work with data
    for row in Pollreader:
        
        #generate list of candidates (this is all that matters)
        candidateList.append(row[2])

#generate list of unique candidates
#uniquecandidates = list(set(candidateList))
#print(uniquecandidates)
    
#generate count of votes by candidate using Counter. is a dictionary
CountCandidates_unsorted = Counter(candidateList)

#create sorted dictionary so we know the first candidate on list is winner
CountCandidates = OrderedDict(CountCandidates_unsorted.most_common())

#get the number of unique candidates in the list
numvotes = len(candidateList)

#figure out the first half of the CountCandidates dictionay for coding
candidate_uniques = list(CountCandidates.keys())[:]

# Go through the counter dictionary & candidate name list and 
#get the candidate names and votes as variables.

candidate1_votes = CountCandidates[(candidate_uniques[0])]
candidate1_name = candidate_uniques[0]
candidate1_percent = round(((candidate1_votes / numvotes)*100),3)

candidate2_votes = CountCandidates[(candidate_uniques[1])]
candidate2_name = candidate_uniques[1]
candidate2_percent = round(((candidate2_votes / numvotes)*100),3)

candidate3_votes = CountCandidates[(candidate_uniques[2])]
candidate3_name = candidate_uniques[2]
candidate3_percent = round(((candidate3_votes / numvotes)*100),3)

candidate4_votes = CountCandidates[(candidate_uniques[3])]
candidate4_name = candidate_uniques[3]
candidate4_percent = round(((candidate4_votes / numvotes)*100),3)

#print out the results.
print("Election Results")
print("---------------------")
print(f"Total Votes: {str(numvotes)}")
print("---------------------")
print(f"{str(candidate1_name)}: {str(candidate1_percent)}% ({str(candidate1_votes)})")
print(f"{str(candidate2_name)}: {str(candidate2_percent)}% ({str(candidate2_votes)})")
print(f"{str(candidate3_name)}: {str(candidate3_percent)}% ({str(candidate3_votes)})")
print(f"{str(candidate4_name)}: {str(candidate4_percent)}% ({str(candidate4_votes)})")
print("---------------------")
print(f"Winner: {str(candidate1_name)}")
print("---------------------")

#locate the output file
election_path = os.path.join("Output","ElectionResults.txt")

#open the output text file and write lines to file
electionout = open(election_path, "w")
electionout.write("Election Results\n")
electionout.write("---------------------\n")
electionout.write(f"Total Votes: {str(numvotes)}\n")
electionout.write("---------------------\n")
electionout.write(f"{str(candidate1_name)}: {str(candidate1_percent)}% ({str(candidate1_votes)})\n")
electionout.write(f"{str(candidate2_name)}: {str(candidate2_percent)}% ({str(candidate2_votes)})\n")
electionout.write(f"{str(candidate3_name)}: {str(candidate3_percent)}% ({str(candidate3_votes)})\n")
electionout.write(f"{str(candidate4_name)}: {str(candidate4_percent)}% ({str(candidate4_votes)})\n")
electionout.write("---------------------\n")
electionout.write(f"Winner: {str(candidate1_name)}\n")
electionout.write("---------------------\n")
electionout.close()


