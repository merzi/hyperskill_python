# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
filled_groups = dict.fromkeys(groups)
number_filled_groups = int(input())

for key, group_name in enumerate(groups):
    if key < number_filled_groups:
        filled_groups[group_name] = int(input())

print(filled_groups)
