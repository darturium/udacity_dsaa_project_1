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

max_time = 0
max_number = None
call_time_per_number = {}

for record in calls:
    for i in range(2):
        if record[i] not in call_time_per_number.keys():
            call_time_per_number[record[i]] = int(record[3])
        else:
            call_time_per_number[record[i]] += int(record[3])

for number in call_time_per_number.keys():
    if call_time_per_number[number] > max_time:
        max_time = call_time_per_number[number]
        max_number = number

print("{} spent the longest time, {} seconds, on the phone during September 2016"
    .format(max_number, max_time))