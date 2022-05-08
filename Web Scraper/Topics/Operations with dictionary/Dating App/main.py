def select_dates(potential_dates):
    age = 30
    hobby = 'art'
    city = 'Berlin'
    arr = [e['name'] for e in potential_dates if e['age'] > age and hobby in e['hobbies'] and e['city'] == city]
    return ", ".join(arr)
