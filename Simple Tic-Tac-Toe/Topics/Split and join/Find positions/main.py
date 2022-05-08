# put your python code here
def find_list_number(numbers_list, searched_number):
    found_positions = []
    for num in range(len(numbers_list)):
        if numbers_list[num] == searched_number:
            found_positions.append(str(num))
    return found_positions


numbers = input().split(" ")
search_number = input()
positions = find_list_number(numbers, search_number)
if positions:
    print(" ".join(positions))
else:
    print("not found")
