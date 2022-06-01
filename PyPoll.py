#0 Import data we need to retrieve
import csv
import os

# to see all functions in csv module
#dir(csv)

#Assign a variable for the file to load and the path
file_to_load = os.path.join('Resources', 'election_results.csv')

#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#1. The total number of votes cast: initialize a vote counter
total_votes = 0

#2 Define the complete list of candidates who received votes (Candidate Options)
candidate_options = []

#3 Declare the empty dictionary
candidate_votes = {}

#5 Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    
    # #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # Read (and print for QC) the header row
    headers = next(file_reader)
    #print(headers)

    # print each row in the csv file.
    for row in file_reader:
        #1a. Add to the total vote count
        total_votes +=1

        #2a Print the candidate name from each row
        candidate_name = row[2]

        #2b Use nested if statement to determine if candidate names are already in the list
        if candidate_name not in candidate_options:

            #2c Append all new candidate names into a single list
            candidate_options.append(candidate_name)

            #3a Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        #3b add a vote to that candidate's count (outside of 'if' statement because that is just to determine if it is the first vote for that candidate, 
        # but inside 'for' loop so that it tallies each time we process a new row)
        candidate_votes[candidate_name] += 1


#4 Determine the percentage of votes each candidate won, by looping through counts
for candidate_name in candidate_votes:
    #4a Retrieve vote count of a candidate and assign it to a new value variable 
    votes = candidate_votes[candidate_name]
    #4b calculate the percentage of votes
    vote_percentage = float(votes)/float(total_votes) * 100
    #4c. Print the candidate name and percentage of votes
    print(f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")

#5 Determine winning vote count and candidate
    #5a Determine if the voters are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #5b if true, then set winning_count = votes and winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #5c set winning candidate equal to candidate's name
        winning_candidate = candidate_name

#5d Print the winner
winning_candidate_summary = (f"-----------------------------\n"
f"Winner: {winning_candidate}\n"
f"Winning Vote count: {winning_count:,}\n"
f"Winnning Percentage: {winning_percentage: .1f}%\n"
f"-----------------------------\n")
print(winning_candidate_summary)



# #Using the open() function with the "w" mode we will write data to the file
# # outfile = open(file_to_save, "w")
# #Use the with statement open the file as a text file
# with open(file_to_save, "w") as txt_file:
# #Write some data to the file
#     txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

#Close the file
# outfile.close()







#4 The total number of votes each candidate won (slicing)
#5 the winner of the election based on the popular vote