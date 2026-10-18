from src.api_client import FrankfurterAPI

api = FrankfurterAPI()
currencies = api.get_currencies()

for currency in currencies[:160]:
    print(currency["iso_code"], "-", currency["name"])

print("Total mata uang:", len(currencies))