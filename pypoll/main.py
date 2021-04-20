import os
import csv

file_to_load = os.path.join('Resources', 'election_data.csv')

total_votes = []

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    for row in reader:
        total_votes.append(row)

num_votes = 0

for i in range(len(total_votes)):
    num_votes += 1
    print(total_votes[i][2])


#print(num_votes)

