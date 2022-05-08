# add Turkey to countries.txt
country = "Turkey\n"
file_name = "countries.txt"
file = open(file_name, "a")
file.writelines(country)
file.close()
