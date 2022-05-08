# put your python code here
hours_first_event = int(input())
minutes_first_event = int(input())
seconds_first_event = int(input())
hours_second_event = int(input())
minutes_second_event = int(input())
seconds_second_event = int(input())

first_event = (hours_first_event * 60 + minutes_first_event) * 60 + seconds_first_event
second_event = (hours_second_event * 60 + minutes_second_event) * 60 + seconds_second_event

print(second_event - first_event)