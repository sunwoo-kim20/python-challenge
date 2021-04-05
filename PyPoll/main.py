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

    # Counting total votes for each candidate
    vote_counts = [0, 0, 0, 0]

    #for vote in votes:
    #    if vote == KHAN:
    #        khan_count += 1
    #    elif vote == CORREY:
    #        correy_count += 1
    #    elif vote == LI:
    #        li_count += 1
    #    elif vote == OTOOLEY:
    #        otooley_count += 1
