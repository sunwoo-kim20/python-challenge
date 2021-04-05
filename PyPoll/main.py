### UCI Data Analytics Bootcamp: Homework 3 - Python Challenge
# Main script for PyPoll Analysis
# Author: Sunwoo Kim
# Files: main.py, PyPoll_Resources_election_data.csv

# Headers
line_header = "------------------------"
title_header = "Election Results"
total_header = "Total Votes:"
winner_header = "Winner:"
nl = "\n"
candidate_vote_index = 2
percent_multiplier = 100

# Dependencies
import os
import csv

# Specifying file path

csvpath = os.path.join('Resources', 'PyPoll_Resources_election_data.csv')

# Reading csv file

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Skip header
    next(csvreader)

    # Organize candidate column into a list

    votes = []
    for row in csvreader:
        votes.append(row[candidate_vote_index])

    # Counting total Votes

    total_votes = len(votes)

    # Identifying candidates who received votes
    candidates = []
    for vote in votes:
        if not (vote in candidates):
            candidates.append(vote)
    candidates_num = len(candidates)
    # Counting total votes for each candidate and hold values in a list
    vote_counts = [0]*candidates_num

    for vote in votes:
        if vote == candidates[0]:
            vote_counts[0] += 1
        elif vote == candidates[1]:
            vote_counts[1] += 1
        elif vote == candidates[2]:
            vote_counts[2] += 1
        elif vote == candidates[3]:
            vote_counts[3] += 1

    # Calculating percentage of votes for each candidate and storing in list

    vote_percentages = []
    for count in vote_counts:
        vote_percentages.append(f"{round((count/total_votes)*percent_multiplier, 2)}%")

    # Find the winner
    winner_index = 0
    winner = candidates[winner_index]

    for i in range(candidates_num):
        if vote_counts[i] > vote_counts[winner_index]:
            winner = vote_counts[i]
            winner_index = i
    print(winner)

    # Print analysis

    total_result = f"{total_header} {total_votes}"
    winner_result = f"{winner_header} {winner}"

    # Print to terminal

    print(title_header)
    print(line_header)
    print(total_result)
    print(line_header)
    for i in range(candidates_num):
        print(f"{candidates[i]}: {vote_percentages[i]} ({vote_counts[i]})")
    print(line_header)
    print(winner_result)
    print(line_header)

    # Print to text file

    analysis_file = open("analysis/pypoll-analysis.txt","w")
    analysis_file.write(title_header + nl)
    analysis_file.write(line_header + nl)
    analysis_file.write(total_result + nl)
    analysis_file.write(line_header + nl)
    for i in range(candidates_num):
        analysis_file.write(f"{candidates[i]}: {vote_percentages[i]} ({vote_counts[i]})" + nl)
    analysis_file.write(line_header + nl)
    analysis_file.write(winner_result + nl)
    analysis_file.write(line_header + nl)
    analysis_file.close()
