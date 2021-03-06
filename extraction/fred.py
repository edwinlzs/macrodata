from fredapi import Fred

class fred_object():
    """
        get_historical(self, code)
    """
    def __init__(self, api_key):
        self.fred = Fred(api_key=api_key)

    def get_historical(self, code):
        return self.fred.get_series(code)
