# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
print("min:", min(test_dict, key=lambda key: test_dict[key]))
print("max:", max(test_dict, key=lambda key: test_dict[key]))
