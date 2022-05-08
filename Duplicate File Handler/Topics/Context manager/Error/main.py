start_year = 2010
end_year = 2020
with open('years.txt', 'w', encoding='utf-8') as f:
    for i in range(start_year, end_year + 1):
        f.write("{} ".format(i))
