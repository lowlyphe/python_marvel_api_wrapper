import requests


class API(object):
    def __init__(self):
        self.url = "https://api.nasdaq.com/api/"
        self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
        
    def get_option_chain(self, quote):
        print(quote)
        url = self.url + 'quote/{}/option-chain?assetclass=stocks&' \
                         'fromdate=all&todate=undefined&excode=oprac&callput=callput&money=all&type=all'.format(quote)
        response = requests.get(url, headers=self.headers).json()
        if (response['message'] is not None or response['data'] is None):
            output_dict = {'current_price': 'Data not available', 'option_data': 'data not available'}
            print()
            return output_dict
        current_stock_price = response['data']['lastTrade'].split(" ")[2]
        output_list = 'response'
        output_dict = {'current_price': current_stock_price, 'option_data': output_list}
        return output_dict
      
    def get_all_stocks(self):
        url = self.url + 'screener/stocks?tableonly=true&download=true'
        response = requests.get(url, headers=self.headers)
        return response

nasdaq = API()
all_stocks = nasdaq.get_all_stocks().json()
# print(all_stocks['data']['rows'][0])

# print(nasdaq.get_option_chain('ABDE'))

my_option_chains = []
for stock in all_stocks['data']['rows']:
    y = nasdaq.get_option_chain(stock['symbol'])
    my_option_chains.append(y)
    
print(my_option_chains)