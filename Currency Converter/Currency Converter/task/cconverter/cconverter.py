from __future__ import annotations
from typing import Union, Optional, Dict
import requests
import string


class CurrencyConverter:
    exchange_rates: dict = {
        "conicoin": {"RUB": 2.98,
                     "ARS": 0.82,
                     "HNL": 0.17,
                     "AUD": 1.9622,
                     "MAD": 0.208}
    }
    primary_currency_code: str = None
    url_template = string.Template("http://www.floatrates.com/daily/$currency_code.json")
    coin_amount: float

    def start(self: CurrencyConverter):
        while self.primary_currency_code is None:
            self.primary_currency_code = self.read_currency_code()
            if self.add_exchange_rates(self.primary_currency_code) is False:
                self.primary_currency_code = None

        while True:
            foreign_currency_code = self.read_currency_code()
            amount = self.read_currency_amount()
            print("Checking the cache...")
            search_result = self.check_rates_includes_foreign_code(foreign_currency_code)
            if search_result:
                print("Oh! It is in the cache!")
            else:
                print("Sorry, but it is not in the cache!")
                search_result = self.add_exchange_rates(self.primary_currency_code, foreign_currency_code)

            if search_result is True:
                print("You received {} {}.".format(round(self.convert_currency(foreign_currency_code, amount), 2),
                                                   foreign_currency_code.upper()))

    def check_rates_includes_foreign_code(self: CurrencyConverter, foreign_currency_code: str) -> bool:
        if foreign_currency_code in self.exchange_rates[self.primary_currency_code]:
            return True
        return False

    def convert_currency(self: CurrencyConverter, foreign_currency_code: str, amount: float) -> float:
        return self.exchange_rates[self.primary_currency_code][foreign_currency_code]["rate"] * amount

    def read_currency_amount(self: CurrencyConverter) -> float:
        amount: float = None
        while amount is None:
            try:
                amount = float(input())
            except ValueError:
                print("invalid input! pls enter a valid amount!")
                amount = None
        return amount

    def read_currency_code(self: CurrencyConverter):
        code = None
        while code is None:
            code = input()
            if len(code.strip()) < 1:
                code = None
        return code

    def load_from_url(self: CurrencyConverter, currency_code: str) -> Union[bool, dict]:
        currency_request = requests.get(self.url_template.substitute(currency_code=currency_code))
        if currency_request.status_code == 200:
            return currency_request.json()
        elif currency_request.status_code == 403 or currency_request.status_code == 404:
            print("request forbidden oder file not found! maybe incorrect currency code!")
        else:
            print("unknown error!")
        return False

    def add_exchange_rates(self: CurrencyConverter, currency_code: str, foreign_currency_code: str = None) -> bool:
        request_result = self.load_from_url(currency_code)
        if not request_result:
            return False

        if foreign_currency_code is None:
            foreign_currency_code = ["USD", "EUR"]

        if currency_code not in self.exchange_rates:
            self.exchange_rates.update({currency_code: {}})

        if type(foreign_currency_code) == type([]):
            for code in foreign_currency_code:
                if code.lower() in request_result:
                    self.exchange_rates[currency_code].update({code.upper(): request_result[code.lower()]})
                else:
                    print("unknown foreign currency code '{}'!".format(code))
                    return False
            return True
        elif foreign_currency_code in request_result:
            self.exchange_rates[currency_code][foreign_currency_code.lower()] = request_result[request_result]
            return True
        else:
            print("unknown foreign currency code '{}'!".format(foreign_currency_code))
            return False

    def load_currency_file(self: CurrencyConverter) -> bool:
        currency = input()
        if self.add_exchange_rates(currency):
            print(self.exchange_rates[currency]["usd"])
            print(self.exchange_rates[currency]["eur"])
            return True
        return False

    def read_coin_amount(self: CurrencyConverter):
        try:
            self.coin_amount = float(input())
        except ValueError:
            print("no integer given")
        else:
            self.print_exchanges()

    def calculate_conicoin_currency(self, currency: str):
        return self.exchange_rates["conicoin"][currency] * self.coin_amount

    def print_exchanges(self):
        for currency in self.exchange_rates["conicoin"]:
            print("I will get {} {} from the sale of {} conicoins.".format(self.calculate_conicoin_currency(currency),
                                                                           currency, self.coin_amount))


exchanger = CurrencyConverter()
exchanger.start()
