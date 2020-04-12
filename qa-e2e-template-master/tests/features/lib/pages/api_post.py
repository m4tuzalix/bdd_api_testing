from reporter import Reporter
import requests

class Api_POST(Reporter):
    def __init__(self, url):
            self.url = url
            Reporter.__init__(self)
            self.headers = {
                'Content-Type': 'application/json',
            }
    
    def api_post(self,name=None,element_type=None,urls=None):
        content = {
            "name":f"{name}",
            "type":f"{element_type}",
            "urls":urls
        }
        response = requests.post(self.url, json=content, headers=self.headers)
        return response
    
    def api_post_response(self,name,element_type,urls):
        code = self.api_post(name=name,element_type=element_type,urls=urls)
        if code.status_code != 200:
            self.add_log(f"{self.api_post_response.__name__}: {code.json()['detail']}")
            return False
        return True

    def api_post_content(self,name):
        content = self.api_post(name).json()
        try:
            self.add_log(f"{self.api_post_content.__name__}: {str(content['detail'])}")
            return True
        except KeyError:
            return False
