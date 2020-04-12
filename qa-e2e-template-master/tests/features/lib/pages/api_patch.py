from reporter import Reporter
import requests

class Api_PATCH(Reporter):
    def __init__(self, url):
        self.url = url
        Reporter.__init__(self)
        self.headers = {
            'Content-Type': 'application/json',
        }

    def patch_api(self, id, key, value, **kwargs):
        content = requests.patch(self.url+id, json={key:value}, headers=self.headers, **kwargs)
        return content

    def api_patch_response(self, id, key, value):
        code = self.patch_api(id, key, value)
        if code.status_code != 200:
            self.add_log(f"{self.api_patch_response.__name__}: {code.json()['detail']}")
            return False
        return True

    def api_patch_content(self, id, key, value):
        content = self.patch_api(id, key, value).json()
        try:
            self.add_log(f"{self.del_api_element_content.__name__}: {content['detail']}")
            return False
        except:
            return True
