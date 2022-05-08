import os  # import os module

# capture file name
file_name = input("Please write the name of the file to work with:\n")

# check file exists
if os.path.exists(file_name):
    # if file exists read the file and write to content to variable
    with open(file_name) as file:
        content = file.read()

    # process the content
    new_content = process(content)

    # write processed content to a new file
    with open(f'{file_name}_processed.txt', 'w') as new_file:
        new_file.write(new_content)

    print("All done!")

else:
    # if file not exists print error message
    print("The file you entered does not exist!")