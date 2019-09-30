from decouple import config
from iexfinance.stocks import Stock


IEX_TOKEN = config('IEX_TOKEN')


def search_stock(symbol):
    stock = Stock(symbol, token='sk_c8589e5108e741ad8d4c98a2b003bf3b')
    company_name = stock.get_company_name()
    quote = stock.get_quote()
    price = quote['latestPrice']
    return price, company_name
