#First import some modules
import os
import csv

#csvpath
csvpath = os.path.join("C:/Users/melis/python-challenge/PyPoll/election_data.csv")

#create a writable text file for the output results
f= open("C:/Users/melis/python-challenge/PyPoll/Election Results.txt","w+")

#initialize some variables
votes=0
winning_number_of_votes = 0
voter = []
county = []
candidate = []
ucandidates = []

#open the csv and read it in
with open(csvpath, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
            #count the number of total rows
            votes = votes+1
            #append the data into lists
            voter.append(row[0])
            county.append(row[1])
            candidate.append(row[2])
            this_candidate = row[2]
            #identify unique candidates
            if ucandidates.count(this_candidate) == 0:
                ucandidates.append(this_candidate)
    
    #Print initial results to the terminal and text file
    print("Election Results")
    print("-------------------")
    print(f"Total Votes : {votes}")
    print("-------------------")
   
   #Write initial results to the text file
    f.write("Election Results \n")
    f.write("----------------- \n")
    f.write(f"Total Votes : {str(votes)}\n")
    f.write("-----------------\n")
    
    #use the list of unique candidates to figure out who won
    for person in ucandidates:
        
        #count the votes
        number_of_votes = candidate.count(person)
        
        #determine overall winner
        if number_of_votes > winning_number_of_votes:
                winner = person
                winning_number_of_votes = number_of_votes
        
        #calculate the percentages
        percent_of_votes = number_of_votes / votes *100
        percent_of_votes = round(percent_of_votes,2)
        
        # print and write candidate results
        print(f"{person} :  {number_of_votes}  ({percent_of_votes}%)")
        f.write(f"{str(person)}: {str(number_of_votes)} ({str(percent_of_votes)}%)\n")

#Print winner to the terminal and text file and close
print("-------------------")
f.write("-----------------\n")
print(f"Winner : {winner}")
f.write(f"Winner  :  {str(winner)}\n")
f.close