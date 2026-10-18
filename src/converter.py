class CurrencyConverter:
    def __init__(self,api):
        self.api = api
        
    def convert(self,amount, base,quote):
        rate = self.api.get_rate(base,quote)
        result = amount * rate

        return result