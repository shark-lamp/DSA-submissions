"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# create a dictionary with set(telephone numbers) and list(total time in seconds) from call column:
# the "value" of seconds from the list will be from both calling and answering end. also since, a num can't call itself.
# return max(value) from the dictionary

call_duration = {}
long_duration = 0
number = None

for record in calls:
    duration = int(record[3])  # Assuming the call duration is in the fourth column
    if record[0] not in call_duration:
        call_duration[record[0]] = duration
    else:
        call_duration[record[0]] += duration

    if call_duration[record[0]] > long_duration:
        long_duration = call_duration[record[0]]
        number = record[0]

for record in calls:
    duration = int(record[3])  # Assuming the call duration is in the fourth column
    if record[1] not in call_duration:
        call_duration[record[1]] = duration
    else:
        call_duration[record[1]] += duration

    if call_duration[record[1]] > long_duration:
        long_duration = call_duration[record[1]]
        number = record[1]

print(f"{number} spent the longest time, {long_duration} seconds, on the phone during September 2016.")



