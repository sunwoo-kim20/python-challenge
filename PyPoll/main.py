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

# Dependencies
import os
import csv

# Specifying file path

csvpath = os.path.join('Resources', 'PyPoll_Resources_election_data.csv')
