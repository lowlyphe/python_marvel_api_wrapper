import time
import hashlib
import requests


class Marvel:
    def __init__(self, public_key):
        self.public_key = public_key
        self.private_key = ''
        self.id = 0
        self.endpoint = ''
        self.sub_endpoint = ''
        self.modifier = ''

    def set_id(self, id):
        self.id = id

    def set_endpoint(self, endpoint):
        self.endpoint = endpoint

    def set_sub_endpoint(self, sub_endpoint):
        self.sub_endpoint = sub_endpoint

    def _api_builder(self):
        public_encoded = self.public_key.encode()
        private_encoded = self.private_key.encode()
        hash = hashlib.md5()
        ts = str(time.time())
        ts_bytes = bytes(ts, 'utf-8')
        hash.update(ts_bytes)
        hash.update(private_encoded)
        hash.update(public_encoded)
        hex = hash.hexdigest()
        return hex, ts
    
    def set_modifier(self, name, value):
        self.modifier = name
        self.value = value

    def get_info(self):
        hex, ts = self._api_builder()
        if self.modifier != '':
            results = requests.get(f'https://gateway.marvel.com/v1/public/{self.endpoint}?ts={ts}&apikey={self.public_key}&hash={hex}&{self.modifier}={self.value}').json()
            return results['data']['results']
        if (self.id == 0):
            if (self.sub_endpoint == ''):
                response = requests.get(f'https://gateway.marvel.com/v1/public/{self.endpoint}?ts={ts}&apikey={self.public_key}&hash={hex}').json()
                result_list = response['data']['results']
                results = []
                return result_list
            return("In order to pass in a sub endpoint, you must provide an ID argument")
        if (self.sub_endpoint == ''):
            response = requests.get(f'https://gateway.marvel.com/v1/public/{self.endpoint}/{self.id}?ts={ts}&apikey={self.public_key}&hash={hex}').json()
            return response['data']['results']
        response = requests.get(f'https://gateway.marvel.com/v1/public/{self.endpoint}/{self.id}/{self.sub_endpoint}?ts={ts}&apikey={self.public_key}&hash={hex}').json()

    





    

