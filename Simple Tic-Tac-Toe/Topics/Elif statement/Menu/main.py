menu = ["pizza", "salad", "soup"]
pizza = "Margherita, Four Seasons, Neapolitan, Vegetarian, Spicy"
salad = "Caesar salad, Green salad, Tuna salad, Fruit salad"
soup = "Chicken soup, Ramen, Tomato soup, Mushroom cream soup"
meal = input()

if meal in menu:
    if meal == "pizza":
        print(pizza)
    elif meal == "salad":
        print(salad)
    else:
        print(soup)
else:
    print("Sorry, we don't have it in the menu")
