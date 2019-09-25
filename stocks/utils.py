from decouple import config
from iexfinance.stocks import Stock


IEX_TOKEN = config('IEX_TOKEN')


def search_stock(symbol):
    stock = Stock(symbol, token=IEX_TOKEN)
    price = stock.get_price()
    company_name = stock.get_company_name()
    return price, company_name
