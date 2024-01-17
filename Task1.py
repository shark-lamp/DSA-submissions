"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
#print(len(texts))
#print(len(calls))
# telephone numbers means both sending and answering telephone numbers
# records mean text + calls 
## so we have to check both sending and answering telephone numbers from both arrays (texts, calls)
count = 0
# concatinate the two arrays-
list = texts + calls
#print(len(list))
#print(list)
cache = set()
for i in list:
    if i[0] not in cache:
        #print(i[0])
        cache.add(i[0])
        #print(cache)
        count += 1
print("count 1: ",count)

for i in list: 
    if i[1] not in cache:
        cache.add(i[1])
        #print(cache)
        count += 1
print("count 2: ",count)   


print(f"There are {count} different telephone numbers in the records.")
