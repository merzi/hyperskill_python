with open("users.json", "r") as file_opener:
    user_dict = json.load(file_opener)

print(len(user_dict["users"]))