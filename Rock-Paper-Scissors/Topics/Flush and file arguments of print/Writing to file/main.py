f_name = "test.txt"
my_string = "A string to be written to a file!"

# what to do with the file and the string
file_opener = open(f_name, "w")
print(my_string, file=file_opener)
file_opener.close()
