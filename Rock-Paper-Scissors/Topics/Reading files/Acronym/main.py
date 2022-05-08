# read test.txt
file = open("test.txt", "r")
for line in file.readlines():
    print(line[0])
file.close()
