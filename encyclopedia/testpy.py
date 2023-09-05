entry_list = ["ben", "kenny", "toms"]
total_in_entryList = len(entry_list)
counter = 0

querySubString = []

while counter <= total_in_entryList-1:
    for entry in entry_list[counter]:
        querySubString.append(entry)
    counter +=1

print(querySubString)