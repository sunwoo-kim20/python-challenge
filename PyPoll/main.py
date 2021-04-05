### UCI Data Analytics Bootcamp: Homework 3 - Python Challenge
# Main script for PyPoll Analysis
# Author: Sunwoo Kim
# Files: main.py, PyPoll_Resources_election_data.csv

# Headers
line_header = "------------------------"
title_header = "Election Results"
total_header = "Total Votes:"
khan_header = "Khan:"
correy_header = "Correy:"
li_header = "Li:"
tooley_header = "O'Tooley:"
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

    # Counting total votes for each candidate and hold values in a list
    vote_counts = [0, 0, 0, 0]

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

    for i in range(len(vote_counts)):
        if vote_counts[i] > vote_counts[winner_index]:
            winner = vote_counts[i]
            winner_index = i
    print(winner)
    # Print analysis to terminal
