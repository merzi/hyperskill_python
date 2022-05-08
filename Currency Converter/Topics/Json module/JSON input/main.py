import json


# write your code here
json_string = input()
obj = json.loads(json_string)
print(type(obj))
print(obj)
