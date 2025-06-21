# contains honey importing data for an year and month
class HoneyImportInfomation:
    def __init__ (self, year, month, countries):
        self.year = year
        self.month = month
        self.country_amount_map = {}
        self.country_price_map = {}
        for country in countries:
            self.country_amount_map[country] = int(0)
            self.country_price_map[country] = int(0)