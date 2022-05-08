# read sums.txt
file_name = "sums.txt"
file_opener = open(file_name, "r")
for line in file_opener.readlines():
    a, b = line.split(" ")
    print(int(a) + int(b))

file_opener.close()
