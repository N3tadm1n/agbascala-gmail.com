# This will  us to allowcreate file paths across operating systems
import os
from collections import Counter

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

#open csv file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
 
    #Total votes
    total_votes = []
    print("Election Results")
    print("------------------------")
    print("Winner: Khan")
    # Appending
    for row in csvreader:
        total_votes.append(row[2])
    print("Total votes",len(total_votes))
    count = {}
    for s in total_votes:
      if s in count:
        count[s] += 1
      else:
        count[s] = 1  
    for key in count:
      if count[key] >= 1:
        p = (count[key] * 100/len(total_votes))
        print(key+":",p,"%", (count[key]))
    
    
    
