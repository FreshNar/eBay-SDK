from django.views.generic import TemplateView
from django.shortcuts import render, redirect
import requests 
import json
from statistics import mean

class eBay:
    """
    eBay SDK for finding similar item prices
    """
    
    def __init__(self, app_id):
        self.endpoint = 'https://svcs.ebay.com/services/search/FindingService/v1'
        self.app_id = app_id
        self.global_id = 'EBAY-US'
        self.response_data_format = 'JSON'
        self.pagination_input = 3

    def findItemsByKeywords(self, keywords, entries_per_page):
        """
        Find and identify catalog products that match the provided search
        criteria.
        """
        keywords = keywords.replace(' ', '%20')
        url = '{endpoint}?OPERATION-NAME=findItemsByKeywords&SECURITY-APPNAME={app_id}&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&keywords={keywords}&paginationInput.entriesPerPage={entries_per_page}'.format(endpoint=self.endpoint, app_id=self.app_id, keywords=keywords, entries_per_page=entries_per_page)
        r = requests.get(url)

        return r.text
    
def call_api_example(keywords, entries_per_page):
    """
    An example of how you would make a request to the eBay api.
    """
    production_key = "Flipwedg-GolfValu-PRD-69f1e332f-91f382a6"

    ebay = eBay(app_id=production_key)
    x = ebay.findItemsByKeywords(keywords, entries_per_page)
    return x

def value(data):
    data = json.loads(data)
    search_results = data['findItemsByKeywordsResponse'][0]['searchResult']
    item_prices = [float(item['sellingStatus'][0]['currentPrice'][0]['__value__']) for item in search_results[0]['item']]
    item_image = search_results[0]['item'][0]['galleryURL']
    fair_value = mean(item_prices)
    return {'value' : round(fair_value,2), 'img_url' : item_image}

# Create your views here.
class ValueGuideView(TemplateView):
    template_name = 'clubhouse/index.html'

def appraise(request):
    if request.method == 'POST':
        query =  request.POST.get('brand') + ' ' + request.POST.get('product') + ' ' + request.POST.get('type')
        data = call_api_example(query, 10)
        results = value(data)
        context = {
            'query' : query,
            'value' : results['value'],
            'img_src' : results['img_url'][0]
        }
        return render(request, 'clubhouse/value.html', context)
    else:
        return redirect('/')