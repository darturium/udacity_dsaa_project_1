# Run Time Explanations

## Task 0

The first print statement uses the string format() which itself reads 3 values from the texts dictionary. Each one of those statements that reads a value has an efficiency of `O(1)`. I assume that the print statement itself has an efficiency of `O(1)` as well, and that the format method has an efficiency of `O(1)` as well. This would then give me `O(4)`. Therefore, the first print statement has an efficiency of `O(1)`.

The second print statement would have an efficiencey of `O(5)` which is reduced to `O(1)`.

## Task 1

The first statement takes `O(1)` time since it's just an assignment.

The first loop that goes through the records in the `calls` dictionary has to iterate `N` number of times so it takes `O(n)` time.

Inside this loop, it then iterates through a constant range of 2 items. This will be constant because it's always 2 items so it have `O(2)` complexity, simplified to `O(1)`.

We then have a statement that checks if `record[i]` is found in the `phone_numbers` array which takes `O(n)` time.

If the item is not found, the value is appended to the array which takes `O(1)` time.

In total, we end with `O(n * n + 2)` which is `O(n^2)`.

The second block of code is very similar to the first one and it also runs in `O(n^2)` time.

The print statement takes `O(1)` time.

In total, the solution takes `O(2n^2 + 2)` which we can simplify to `O(n^2)`.

## Task 2

Solution begins with 3 assignment operations which will take `O(3)`.

We then loop through every record in calls. This will take `O(n)`. Inisde this for loop is another for loop which only loops twice, taking `O(2)` times the time of the lines inside the loop. The if statement inside this loops takes `O(n)` because it has to look through all elements in a list in the worst-case scenario. Depending on the outcome of the if statement, a line will be executed which in both cases (true or false) will take `O(n)` in the worst case because it is adding an alement to a dictionary and according to https://wiki.python.org/moin/TimeComplexity, it looks like setting a value in a dictionary takes `O(n)` in the worst case. Therefore, this first block of code takes `O(n * n * n + 2)` in the worst case, or `O(n^3)`.

The second block of code will take `O(n + 3)` time because it loops through all keys of `call_time_per_number`, then peforms a comparison, and if true, peforms 2 operations. We can say that the second block takes `O(n)` time.

The print statement will take `O(1)`.

The total time for the solution will be `O(n^3 + n + 4)` which can be simplified to `O(n^3)`.

## Task 3

The first 4 statements have an `O(1)` complexity each, including the statment that gets the length of `calls` since getting the length of a list takes `O(1)` time.

The block of code that loops through the `calls` list will, in the worst case scenario, have a complexity of `O(n^2)`. This is because if the number begins with (080) or if the numbers starts with 7, 8, or 9, we will check if the number already exists in the `area_codes` array using Python's `in` statement. This means we'll have to loop through all of the elements in the `area_codes` array in the worst-case scenario, and through all of th elements in `calls`, making the complexity `O(n^2)`.

Sorting the `area_codes` array will take `O(n log n)` time (according to https://wiki.python.org/moin/TimeComplexity).

Printing the statement for PART A will take `O(n)` because we'll have to lop through `area_codes` to print each element on its own line.

Printing the statement for PART B will take `O(1)` since we are not looping through anything and just printing the values.

## Task 4

The first 5 statements are just assignments statements, which will take `O(5)` simplified to `O(1)`.

Looping through the `calls` array will take `O(n)` time. The 2 statements in side the loop will take `O(1)` each.

Looping through the `texts` array will also take `O(n)` time.

The block of code where we loop through `call_sending_numbers` will take `O(n^4)` time. I come to this conclusion because inside this loop, we might have to look through all of the elements in `call_receiving_numbers`, and through all elements of `text_sending_numbers`, and through all elements of `text_receiving_numbers`. Each one of those would take `O(n)`, therefore, `O(n * n * n * n)` would be `O(n^4)`.

The print operation will take `O(1)` plus `O(n)` because we loop through `possible_marketers` to print each element on its own line. 