numbers = [1234, 5678, 90]
# save this list in `file_with_list.txt`
file_name = "file_with_list.txt"
file_opener = open(file_name, "w")
print(str(numbers), file=file_opener, end="")
file_opener.close()
