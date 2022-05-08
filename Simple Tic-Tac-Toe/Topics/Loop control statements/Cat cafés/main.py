max_cats = ""
count = 0

while True:
    cats = input()
    if cats == "MEOW":
        break
    elif int(cats.split(" ")[1]) > count:
        max_cats = cats.split(" ")[0]
        count = int(cats.split(" ")[1])

print(max_cats)
