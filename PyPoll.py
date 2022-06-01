#0 Import data we need to retrieve
import csv
import os

#see all functions in csv module
#dir(csv)

#Assign a variable for the file to load and the path
file_to_load = os.path.join('Resources', 'election_results.csv')

#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Open the election results and read the file
with open(file_to_load) as election_data:
    
    # #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # Read and print the header row
    headers = next(file_reader)
    print(headers)

    # # print each row in the csv file.
    # for row in file_reader:
    #     print(row)


# #Using the open() function with the "w" mode we will write data to the file
# # outfile = open(file_to_save, "w")
# #Use the with statement opent the file as a text file
# with open(file_to_save, "w") as txt_file:
# #Write some data to the file
#     txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

#Close the file
# outfile.close()




#1. The total number of votes cast
#2 The complete list of candidates who received votes
#3 The percentage of votes each candidate won
#4 The total number of votes each candidate won (slicing)
#5 the winner of the election based on the popular vote