# write your code here
import string

months_in_year = 12
line_template = string.Template("$salary\n")
with open("salary.txt") as file_opener, open("salary_year.txt", "a") as file_opener_2:
    for number in file_opener.readlines():
        yearly_salary = str(int(number) * months_in_year)
        file_opener_2.write(line_template.substitute(salary=yearly_salary))
