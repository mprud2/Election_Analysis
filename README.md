# Election_Analysis
Module 3 work with Python

## Election Audit Overview
A Colorado Board of Electors employee has given me the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on the popular vote.
6. Calculate the total number of votes from each county
7. Calculate the percentage of votes that came from each county
8. Determine which county had the biggest turnout.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.13, Visual Studio Code 3.7.13

## Summary

<img width="239" alt="Screenshot_of_election_results" src="https://user-images.githubusercontent.com/104801614/171552259-98f4376a-69bf-4958-8170-474191578265.png">

### Election Audit Results
- There were 369,711 votes cast in the election

#### County Breakdown
- Jefferson County tallied 38,855 votes, which were 10.51% of ballots cast.
- Denver County tallied 306,055 votes, which were  82.78% of ballots cast.
- Arapahoe County tallied 24,801 voles, which were 6.71% of ballots cast.
Denver was the biggest vote contributor to this election.

#### Candidate Breakdown
- The field of candidates were:
  -   Charles Casper Stockham
  -   Diana DeGette
  -   Raymon Anthony Doane
- The results were:
  -   Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  -   Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  -   Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  -   Diana DeGette received 73.8% of the vote and 272,892 number of votes.

### Election Audit Summary
This audit was meant to demonstrate that meaningful statistics could be pulled from a csv file and then output to a text file of summary statistics.  As long as data is provided with similar headers, this code can be used to replicate similar outputs.  This script could be used on both smaller or larger elections, if the desired results are the same.  However, this code could also be updated to output other meaningful statistics, such as polling location, if the data is collected and included in the csv file.  Likewise, this code could also be modified to tabulate results in a place like Maine where ranked-choice voting creates a somewhat more involved tabulation process.  This could be achieved using additional for loops and if statements to eliminate candidates from the pool, if they did not receive enough votes, and then the voter's second or third choice could be tabulated instead.
