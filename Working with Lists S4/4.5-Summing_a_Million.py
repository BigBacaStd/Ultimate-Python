# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one
# and ends at one million. Also, use the sum() function to see how quickly
# Python can add a million numbers.

# TODO: Make a list of the numbers from one to one million.

one_to_million = list(range(1, 1000001))

# TODO: Use min() to find the minimum value in the list.

print(min(one_to_million))

# TODO: Use max() to find the maximum value in the list.
print(max(one_to_million))
# TODO: Use sum() to find the sum of all numbers in the list.

print(sum(one_to_million))
