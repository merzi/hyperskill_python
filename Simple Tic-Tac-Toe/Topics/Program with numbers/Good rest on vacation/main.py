# put your python code here
duration_days = int(input())
daily_food_cost = int(input())
one_fly_cost = int(input())
hotel_cost = int(input())

print((duration_days * daily_food_cost)
      + (one_fly_cost * 2)
      + (hotel_cost * (duration_days - 1)))
