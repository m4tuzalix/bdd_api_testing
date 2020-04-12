from reporter import Reporter
import requests

class Api_GET(Reporter):
    def __init__(self, url):
        self.url = url
        Reporter.__init__(self)
        self.headers = {
            'Content-Type': 'application/json',
        }

    def api_response(self, *args):
        if len(args) > 0:
            self.url += args[0]
        self.response = requests.get(url=self.url, headers=self.headers)
        return self.response
        
    def get_api_response(self):
        code = self.api_response()
        if code.status_code != 200:
            self.add_log(f"{self.get_api_response.__name__}: {code.json()['detail']}")
            return False
        return True

    def get_api_all_content(self):
        for single in self.api_response().json():
            try:
                self.add_log(f"{self.get_api_all_content.__name__}: {single['detail']}")
                return False
            except KeyError:
                return True

    def get_api_single_response(self, id):
        code = self.api_response(id)
        if code.status_code != 200:
            self.add_log(f"{self.get_api_single_response.__name__}: {code.json()['detail']}")
            return False
        return True

    def get_api_single_content(self, id):
        content = self.api_response(id).json()
        try:
            self.add_log(f"{self.get_api_single_content.__name__}: {content['detail']}")
            return False
        except KeyError:
            return True

