import string

# put your code here
sentence = "Dear $username! It was really nice to meet you. Hopefully, you have a nice day! See you soon, $username!"
template = string.Template(sentence)
username = input()
print(template.substitute(username=username))
