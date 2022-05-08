seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# create a list of days here
day_in_seconds = 24 * 60 * 60

print([days // day_in_seconds for days in seconds])
