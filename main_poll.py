import os
import csv

poll_csvpath = os.path.join("Resources", "election_data.csv")
file_toOutput = os.path.join("", "poll_analysis.csv")  #OUTPUT

#assign the key variables
total_votes = 0
candidate_names_list = []

#open the csv file
with open(poll_csvpath) as poll_data:
    csvreader = csv.reader(poll_data, delimiter=",")
    print(csvreader)
    header = next(csvreader)

#loop to calculate total votes based on number od rows
    for row in csvreader:
        #calculate total votes
        total_votes += 1

    #create the list of uniqiecandidate names   
        name = row[2]
        if name not in candidate_names_list:
            candidate_names_list.append(name)    
    for name in candidate_names_list:
        print(name)

#votes for the 1st candidate- Khan
with open(poll_csvpath) as poll_data:
    csvreader = csv.reader(poll_data, delimiter=",")
    print(csvreader)
    header = next(csvreader)
   
    votes_Khan = 0
    for row in csvreader:
        if row[2] == candidate_names_list[0]:
            votes_Khan += 1
    percents_Khan = round((votes_Khan/total_votes*100),2)

#votes for the 2nd candidate Correy
with open(poll_csvpath) as poll_data:
    csvreader = csv.reader(poll_data, delimiter=",")
    print(csvreader)
    header = next(csvreader)
    
    votes_Correy = 0
    for row in csvreader:
        if row[2] == candidate_names_list[1]:
            votes_Correy += 1
    percents_Correy = round((votes_Correy/total_votes*100),2)

#votes for the 3rd candidate- Li
with open(poll_csvpath) as poll_data:
    csvreader = csv.reader(poll_data, delimiter=",")
    print(csvreader)
    header = next(csvreader)
    
    votes_Li = 0
    for row in csvreader:
        if row[2] == candidate_names_list[2]:
            votes_Li += 1
    percents_Li = round((votes_Li/total_votes*100),2)

#votes for the 4th candidate- O'Tooley
with open(poll_csvpath) as poll_data:
    csvreader = csv.reader(poll_data, delimiter=",")
    print(csvreader)
    header = next(csvreader)

    votes_Tooley = 0
    for row in csvreader:
        if row[2] == candidate_names_list[3]:
            votes_Tooley += 1
    percents_Tooley = round((votes_Tooley/total_votes*100),2)

    votes_list = {}
    votes_list = {candidate_names_list[0]:percents_Khan, candidate_names_list[1]:percents_Correy, 
    candidate_names_list[2]:percents_Li, candidate_names_list[3]:percents_Tooley}
    
    winner = max(votes_list.values())


    print_output = (f"Election Results\n"
                    f"________________________________________________\n"
                    f"Total Votes: {total_votes}\n"
                    f"{candidate_names_list[0]}: {percents_Khan}% ({votes_Khan})\n"
                    f"{candidate_names_list[1]}: {percents_Correy}% ({votes_Correy})\n"
                    f"{candidate_names_list[2]}: {percents_Li}% ({votes_Li})\n"
                    f"{candidate_names_list[3]}: {percents_Tooley}% ({votes_Tooley})\n"
                    f"{winner}")

print(print_output)
with open(file_toOutput, "w") as txt_file:
    txt_file.write(print_output)