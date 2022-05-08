weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
current_day = 1
current_time = 10.5
new_offset = input()
if new_offset.startswith('+'):
    offset = int(new_offset.replace('+', ''))
    if current_time + offset > 24:
        current_day += 1
elif new_offset.startswith('-'):
    offset = int(new_offset.replace('-', ''))
    if current_time - offset < 0:
        current_day -= 1

print(weekdays[current_day])
