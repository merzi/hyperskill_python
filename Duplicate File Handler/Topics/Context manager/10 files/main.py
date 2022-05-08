# write your code here
first_file_number = 1
last_file_number = 10
for number in range(first_file_number, last_file_number + 1):
    with open("file{}.txt".format(number), "a") as file_opener:
        file_opener.write(str(number))
