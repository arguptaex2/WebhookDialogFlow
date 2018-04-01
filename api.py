import urllib.request, json
"""TODO hit the api and get relevant data"""
API_URL = 'https://api.newhomesource.com/api/v2/Search/Homes?partnerid=1&marketid=269&SortBy=Random&SortSecondBy=None'
def fetchHomeDetails(cities):
    global API_URL
    API_URL += '&Cities='+cities+"&PageSize=10"
    with urllib.request.urlopen(API_URL) as url:
        data = json.loads(url.read().decode())
        return data

