prime_numbers = [num for num in range(2, 1000) if all(num % num_2 for num_2 in range(2, num))]
