import time
import hashlib
import requests
from Modifier import Modifier


class Marvel:
    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key
        self.id = 0
        self.endpoint = ''
        self.sub_endpoint = ''
        self.modifier = ''
        self.modifiers = []

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
        new_modifier = Modifier(name, value)
        self.modifiers.append({'name': new_modifier.name, 'value': new_modifier.value})
        # print('modified', self.modifiers)


    def get_info(self):
        hex, ts = self._api_builder()
        if len(self.modifiers) != 0:
            if self.id != 0:
                url = f'https://gateway.marvel.com/v1/public/{self.endpoint}/{self.id}?ts={ts}&apikey={self.public_key}&hash={hex}'
                for i in range(len(self.modifiers)):
                    url += f'&{self.modifiers[i]["name"]}={self.modifiers[i]["value"]}'
                    results = requests.get(url).json()
                    if(results['code'] != 200):
                        return results
                    return results['data']['results']
            url = f'https://gateway.marvel.com/v1/public/{self.endpoint}?ts={ts}&apikey={self.public_key}&hash={hex}'
            for i in range(len(self.modifiers)):
                url += f'&{self.modifiers[i]["name"]}={self.modifiers[i]["value"]}'
            results = requests.get(url).json()
            if(results['code'] != 200):
                return results
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

    





    

