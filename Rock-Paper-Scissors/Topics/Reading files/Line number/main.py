# read sample.txt and print the number of lines
file_name = "sample.txt"
file_opener = open(file_name, "r")

print(len(file_opener.readlines()))

file_opener.close()
