import requests

class FrankfurterAPI :
    def __init__(self):
        self.base_url = "https://api.frankfurter.dev/v2"

    def get_rate(self, base, quote):
         url = f"{self.base_url}/rate/{base}/{quote}"

         response = requests.get(url, timeout=10)
         response.raise_for_status()    

         data = response.json()
    
         return data["rate"]
     
    def get_currencies(self):
        url = f"{self.base_url}/currencies"

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        return response.json()

