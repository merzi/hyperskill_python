scores = input().split()
# put your python code here
lives = 3
count = 0

for char in scores:
    if lives == 0:
        break
    elif char == "C":
        count += 1
    else:
        lives -= 1

print("You won" if lives > 0 else "Game over")
print(count)
