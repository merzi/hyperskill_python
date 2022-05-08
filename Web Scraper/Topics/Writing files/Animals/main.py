# read animals.txt
# and write animals_new.txt
old_file_name = "animals.txt"
new_file_name = "animals_new.txt"
animals = []
file = open(old_file_name, 'r')
for line in file:
    animals.append(line.replace("\n", ""))

file.close()
file = open(new_file_name, "w")
file.write(" ".join(animals))
file.close()
