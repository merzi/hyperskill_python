lines = int(input())

results = []
for _ in range(lines):
    res = input().split(" ")
    if res[1] == 'win':
        results.append(res[0])

print(results)
print(len(results))
