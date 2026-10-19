from src.api_client import FrankfurterAPI



def get_currencies():
    api = FrankfurterAPI()
    currencies = api.get_currencies()
    
    result = []
    for currency in currencies[:160]:
        result.append(
        {
            "code" : currency["iso_code"],
            "name": currency["name"]
        })
    return result