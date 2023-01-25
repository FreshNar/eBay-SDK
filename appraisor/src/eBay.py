import requests 

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