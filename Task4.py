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

possible_marketers = []
call_sending_numbers = []
call_receiving_numbers = []
text_sending_numbers = []
text_receiving_numbers = []

for call_record in calls:
    call_sending_numbers.append(call_record[0])
    call_receiving_numbers.append(call_record[1])

for text_record in texts:
    text_sending_numbers.append(text_record[0])
    text_receiving_numbers.append(text_record[1])

for number in call_sending_numbers:
    if number not in possible_marketers:
        if number not in call_receiving_numbers:
            if number not in text_sending_numbers:
                if number not in text_receiving_numbers:
                    possible_marketers.append(number)

possible_marketers.sort()
print("These numbers could be telemarketers: ")
for number in possible_marketers:
    print(number)
