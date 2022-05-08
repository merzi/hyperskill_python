# Write your code here
from __future__ import annotations
import math
import string
from typing import Union, Optional, Dict


class CoffeeMachine:
    """
    the coffee machine with all needed methods to get a fresh and good smelling coffee
    """
    water: int = 0
    """
    amount of water in the coffee machine
    """
    milk: int = 0
    """
    amount of milk in the coffee machine
    """
    coffee_beans: int = 0
    """
    amount of coffee beans in the coffee machine
    """
    cups: int = 0
    """
    amount of disposable cups in the coffee machine
    """
    money: int = 0
    """
    amount of money in the coffee machine
    """
    coffee_types = {1: {"name": "espresso",
                        "ingredients": {"water": 250,
                                        "milk": 0,
                                        "coffee": 16,
                                        "money": 4}},
                    2: {"name": "latte",
                        "ingredients": {"water": 350,
                                        "milk": 75,
                                        "coffee": 20,
                                        "money": 7}},
                    3: {"name": "cappuccino",
                        "ingredients": {"water": 200,
                                        "milk": 100,
                                        "coffee": 12,
                                        "money": 6}},
                    4: {"name": "coffee",
                        "ingredients": {"water": 200,
                                        "milk": 50,
                                        "coffee": 15,
                                        "money": 3}}}
    """
    contains the available coffee types and their ingredients
    """

    def __init__(self: CoffeeMachine, water: int, milk: int, coffee_beans: int,
                 disposable_cups: int, money: int) -> None:
        """
        initiate the instance of the coffee machine and start her
        :param water: amount of water in the machine
        :param milk: amount of milk in the machine
        :param coffee_beans: amount of coffee beans in the machine
        :param disposable_cups: amount of cups in the machine
        :param money: amount of money in the machine
        """
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = disposable_cups
        self.money = money

        while True:
            if not self.menu():
                break

    def __repr__(self: CoffeeMachine) -> str:
        """
        return current variable status of the instance
        :return: string with all values of all variables
        """
        output_template = "Instance of CoffeeMachine with water: {}, milk: {}, coffee_beans: {}, cups: {}, money: {}"
        return output_template.format(self.water, self.milk, self.coffee_beans, self.cups, self.money)

    def __str__(self: CoffeeMachine) -> str:
        output_template = "The coffee machine has:\n" \
                          "{} ml of water\n" \
                          "{} ml of milk\n" \
                          "{} g of coffee beans\n" \
                          "{} disposable cups\n" \
                          "${} of money"
        return output_template.format(self.water, self.milk, self.coffee_beans, self.cups, self.money)

    def menu(self: CoffeeMachine) -> bool:
        """
        print the start screen and the menu
        :return: boolean status of the program. True = Program still running, False = Program will stop
        """
        menu_options = ["buy", "fill", "take", "remaining", "exit"]
        option = None
        while option is None:
            print("\nWrite action (buy, fill, take, remaining, exit): ")
            option = input()
            if option not in menu_options:
                option = None
                print("invalid menu option")
            elif option == menu_options[0]:
                self.buy_menu()
            elif option == menu_options[1]:
                self.fill_ingredients()
            elif option == menu_options[2]:
                self.take_money()
            elif option == menu_options[3]:
                self.print_overview_screen()
            elif option == menu_options[4]:
                return False

        return True

    def print_overview_screen(self) -> None:
        """
        print the overview screen over the ingredients in the machine
        :return: nothing
        """
        print(self)

    def buy_menu(self: CoffeeMachine) -> CoffeeMachine:
        """
        ask for the wanted coffee and try to buy it
        :return: the instance of the coffee machine
        """

        type_strings = [str(key) + " - " + coffee["name"] for key, coffee in self.coffee_types.items()]
        print("What do you want to buy? {}, back - to main menu:".format(", ".join(type_strings)))
        coffee = input()
        amount = 1
        if coffee == "back":
            return self

        if int(coffee) in self.coffee_types:
            needed_ingredients = self.get_ingredient(int(coffee), amount)
            if not needed_ingredients:
                print("ingredients for coffee with number {} cannot find!".format(coffee))
                return self

            result = self.is_brewable(needed_ingredients)
            if result is True:
                print("I have enough resources, making you a coffee!")
                self.water -= needed_ingredients["water"]
                self.milk -= needed_ingredients["milk"]
                self.coffee_beans -= needed_ingredients["coffee"]
                self.money += needed_ingredients["money"]
                self.cups -= needed_ingredients["cups"]
            elif not result:
                print("Sorry, needed ingredients cannot be calculated!")
            else:
                print("Sorry, not enough {}!".format(", ".join(result)))
        else:
            print("unknown coffee!")
        return self

    def get_ingredient(self: CoffeeMachine, coffee_type: int, amount: int) -> Union[bool, Dict[str, str]]:
        """
        calculate the required amount for the ingredients for the wanted coffee type
        :param coffee_type: the wanted coffee type
        :param amount: amount of the wanted coffee
        :return: returns false if the coffee type is unknown, or the amount of ingredients for the wanted coffee type
        """
        if coffee_type not in self.coffee_types:
            return False

        return {"water": self.coffee_types[coffee_type]["ingredients"]["water"] * amount,
                "milk": self.coffee_types[coffee_type]["ingredients"]["milk"] * amount,
                "coffee": self.coffee_types[coffee_type]["ingredients"]["coffee"] * amount,
                "money": self.coffee_types[coffee_type]["ingredients"]["money"] * amount,
                "cups": 1 * amount}

    def is_brewable(self: CoffeeMachine, needed_ingredients: Union[bool, Dict[str, int]]) -> Union[bool, list]:
        """
        checks if the coffee is brewable
        :param needed_ingredients: dictionary which contains the needed ingredients for the coffee
        :return: True if coffee is brewable or list with missed ingredient
        """
        if type(needed_ingredients) == bool:
            return False

        missed_ingredients = []
        if self.water < needed_ingredients["water"]:
            missed_ingredients.append("water")
        if self.milk < needed_ingredients["milk"]:
            missed_ingredients.append("milk")
        if self.coffee_beans < needed_ingredients["coffee"]:
            missed_ingredients.append("coffee beans")
        if self.cups < needed_ingredients["cups"]:
            missed_ingredients.append("disposable cups")

        if len(missed_ingredients) > 0:
            return missed_ingredients
        return True

    def take_money(self: CoffeeMachine) -> CoffeeMachine:
        """
        takes the money from the ingredients
        :return: dictionary of the ingredients in the machine
        """
        print("I gave you ${}".format(self.money))
        self.money = 0
        return self

    def fill_ingredients(self: CoffeeMachine) -> CoffeeMachine:
        """
        fills the ingredients in the machine
        :return: dictionary of the ingredients in the machine
        """
        print("Write how many ml of water you want to add: ")
        self.water += int(input() or 0)
        print("Write how many ml of milk you want to add: ")
        self.milk += int(input() or 0)
        print("Write how many grams of coffee beans you want to add: ")
        self.coffee_beans += int(input() or 0)
        print("Write how many disposable cups of coffee you want to add: ")
        self.cups += int(input() or 0)
        return self

    def print_message(self: CoffeeMachine) -> None:
        """
        prints the standard output
        :return: nothing
        """
        print("Starting to make a coffee\n" +
              "Grinding coffee beans\n" +
              "Boiling water\n" +
              "Mixing boiled water with crushed coffee beans\n" +
              "Pouring coffee into the cup\n" +
              "Pouring some milk into the cup\n" +
              "Coffee is ready!")

    def max_brewable_quantity(self: CoffeeMachine, coffee_type: int) -> int:
        """
        calculate the quantity of the brewable coffee
        :param coffee_type: the wanted coffee type
        :return: quantity of coffee cups
        """
        ingredients = self.get_ingredient(coffee_type, 1)
        return min([math.floor(self.milk / int(ingredients["milk"])),
                    math.floor(self.water / int(ingredients["water"])),
                    math.floor(self.coffee_beans / int(ingredients["coffee"]))])

    def ingredient_calculator(self: CoffeeMachine) -> Optional[bool]:
        """
        ask for the amount of coffee and calculate the needed ingredients
        :return: false if something went wrong
        """
        type_strings = [str(key) + " - " + coffee["name"] for key, coffee in self.coffee_types.items()]
        print("What do you want to buy? {}, back - to main menu:".format(", ".join(type_strings)))
        coffee = input()
        if coffee not in self.coffee_types:
            print("unknown coffee type!")
            return False

        print("Write how many cups of coffee you will need:")
        amount = int(input())
        ingredient = self.get_ingredient(int(coffee), amount)

        if ingredient is False:
            print("Something went wrong!")
            return False

        output_template = string.Template("For $amount cups of coffee you will need:\n" +
                                          "$water ml of water\n" +
                                          "$milk ml of milk\n" +
                                          "$coffee g of coffee beans")

        print(output_template.substitute(amount=amount, water=ingredient["water"],
                                         milk=ingredient["milk"], coffee=ingredient["coffee"]))

    def request_available_ingredients(self: CoffeeMachine) -> None:
        """
        requests the actual amount of ingredients in the machine
        :return: nothing
        """
        print("Write how many ml of water the coffee machine has:")
        self.water = int(input())
        print("Write how many ml of milk the coffee machine has:")
        self.milk = int(input())
        print("Write how many grams of coffee beans the coffee machine has:")
        self.coffee_beans = int(input())
        print("Write how many cups of coffee you will need:")
        cups_needed = int(input())
        type_strings = [str(key) + " - " + coffee["name"] for key, coffee in self.coffee_types.items()]
        print("What do you want to buy? {}:".format(", ".join(type_strings)))
        coffee = input()
        if coffee not in self.coffee_types:
            print("unknown coffee type!")
            return None

        self.check_amount_brewable(int(coffee), cups_needed)

    def check_amount_brewable(self: CoffeeMachine, coffee_type: int, amount: int) -> bool:
        """
        check if the quantity of coffees are brewable
        :param coffee_type: the chosen coffee type
        :param amount: wanted amount of coffees to brew
        :return: True if wanted quantity is brewable, False if not
        """
        max_amount = self.max_brewable_quantity(coffee_type)

        if max_amount == amount:
            print("Yes, I can make that amount of coffee")
            return True
        elif max_amount > amount:
            print("Yes, I can make that amount of coffee (and even {} more than that)".format(max_amount - amount))
            return True
        print("No, I can make only {} cups of coffee".format(max_amount))
        return False


quantity_milk = 540
quantity_water = 400
quantity_coffee = 120
quantity_money = 550
quantity_cups = 9

CoffeeMachine(quantity_water, quantity_milk, quantity_coffee, quantity_cups, quantity_money)
