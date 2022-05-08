from __future__ import annotations
import requests


# write your code here!
import json
import string


class ConiCoinCalculator:
    exchange_rates = {
        "RUB": 2.98,
        "ARS": 0.82,
        "HNL": 0.17,
        "AUD": 1.9622,
        "MAD": 0.208
    }

    coin_amount: float

    def load_currency_file(self: ConiCoinCalculator):
        url_template = string.Template("http://www.floatrates.com/daily/$currency_code.json")
        currency = input()
        currency_request = requests.get(url_template.substitute(currency_code=currency))
        currency_dictionary = currency_request.json()
        print(currency_dictionary["usd"])
        print(currency_dictionary["eur"])

    def read_coin_amount(self: ConiCoinCalculator):
        try:
            self.coin_amount = float(input())
        except ValueError:
            print("no integer given")
        else:
            self.print_exchanges()

    def calculate_conicoin_currency(self, currency: str):
        return self.exchange_rates[currency] * self.coin_amount

    def print_exchanges(self):
        for currency in self.exchange_rates:
            print("I will get {} {} from the sale of {} conicoins.".format(self.calculate_conicoin_currency(currency),
                                                                           currency, self.coin_amount))


exchanger = ConiCoinCalculator()
exchanger.load_currency_file()
