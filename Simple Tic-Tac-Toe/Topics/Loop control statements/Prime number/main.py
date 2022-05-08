number = int(input())
counter = number
is_prime = True

while counter > 0:
    if number == 1:
        is_prime = False
        break
    elif number % counter == 0 and counter not in [1, number]:
        is_prime = False
        break
    counter -= 1

print("This number is prime" if is_prime else "This number is not prime")
