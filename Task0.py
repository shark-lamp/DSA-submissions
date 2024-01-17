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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
# text
firsttext = texts[0]
lastcall = calls[-1]

#print(firsttext)
#print(lastcall)
incoming_number = firsttext[0]
answering_number = firsttext[1]
time = firsttext[2]
print(f"First record of texts, {incoming_number} texts {answering_number} at time {time}")
incoming_number = lastcall[0]
answering_number = lastcall[1]
time = lastcall[2]
during = lastcall[3]
print(f"Last record of calls, {incoming_number} calls {answering_number} at time {time}, lasting {during} seconds")



