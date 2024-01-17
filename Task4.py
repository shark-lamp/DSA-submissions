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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

import csv

outgoing = set()
incoming = set()
sent = set()
received = set()

for row in calls:
    outgoing.add(row[0])
    incoming.add(row[1])

for row in texts:
    sent.add(row[0])
    received.add(row[1])

possible = outgoing - (incoming | sent | received)
sorted_telemarketers = sorted(possible)

print("These numbers could be telemarketers:")
for number in sorted_telemarketers:
    print(number)



