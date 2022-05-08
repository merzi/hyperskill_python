# read test_file.txt
file_name = "test_file.txt"

try:
    file_opener = open(file_name, 'r', encoding='utf-16')
    print(file_opener.readline())
    file_opener.close()
except:
    print("an error occurred!")
