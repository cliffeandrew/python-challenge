#Import modules
import os
import csv

#Create import path variable
csv_path = os.path.join('Resources','election_data.csv')

#Initialize variables
total_votes = int(0)
results_data = {}
results_data_export = {}
results_data_winner = {}
candidate_list_output = []

#Open csv file in read mode and apply handle
with open(csv_path, 'r') as csv_file:
    #Create recordsource variable with python csv.reader delimiting function
    csv_reader = csv.reader(csv_file, delimiter=",")
    #Row 1 header function
    csv_header = next(csv_reader)

    #Iterate thru recordsource 
    for row in csv_reader:
        #Increment number of votes
        total_votes += 1
        
        #Candidate in column 3
        CandidateList = row[2]
        if CandidateList not in results_data:
            results_data[CandidateList] = 1
            results_data_export[CandidateList] = 1
            results_data_winner[CandidateList] = 1
            candidate_list_output.append(row[2])
        else:
            results_data[CandidateList] += 1
            results_data_export[CandidateList] += 1
            results_data_winner[CandidateList] += 1

#Print output
print("Election Results")
winner = max(results_data_winner, key=results_data_winner.get)
print(winner)

print(f"Total Votes: {str(total_votes)}")
print(candidate_list_output)

#print(f"Khan: {results_data[Khan]/total_votes:.4%} ({results_data[Khan]}")
#print(f"Correy: {results_data[Correy]/total_votes:.4%} ({results_data[Correy]}")
#print(f"Li: {results_data[Li]/total_votes:.4%} ({results_data[Li]}")
#print(f"'O'Tooley: {results_data['O'Tooley']/total_votes:.4%} ({results_data['O'Tooley']}")

#Output to new file section

roster = zip(candidate_list_output, results_data_export)

#Create export path variable
output_path = os.path.join("analysis","new.csv")

#Open csv file in write mode and apply handle
with open(output_path, 'w', newline='') as csv_file:

    #Output statistics and results
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(["Election Results"])
    csv_writer.writerow(["--------------------------"])
    csv_writer.writerow(["Total Votes",total_votes])
    csv_writer.writerow(["--------------------------"])
    csv_writer.writerows([roster])
    csv_writer.writerow(["--------------------------"])
    csv_writer.writerow(["Winner: ",winner])
    csv_writer.writerow(["--------------------------"])
