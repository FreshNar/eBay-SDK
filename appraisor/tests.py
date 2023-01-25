import json
from statistics import mean
from src.eBay import eBay

def call_api_example(keywords, entries_per_page):
    """
    An example of how you would make a request to the eBay api.
    """
    with open('api_keys.json') as file:
        credentials = json.loads(file.read())
        production_key = credentials['app_id']['production']

    ebay = eBay(app_id=production_key)
    x = ebay.findItemsByKeywords(keywords, entries_per_page)
    return x

def value(data):
    data = json.loads(data)
    search_results = data['findItemsByKeywordsResponse'][0]['searchResult']
    item_prices = [float(item['sellingStatus'][0]['currentPrice'][0]['__value__']) for item in search_results[0]['item']]

    fair_value = mean(item_prices)
    return round(fair_value,2)

keywords = input('What would you like to value?: ')
data = call_api_example(keywords, 10)
print('$' + str(value(data)))
