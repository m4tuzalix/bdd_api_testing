from reporter import Reporter
import requests

class Api_DELETE(Reporter):
    def __init__(self, url):
        self.url = url
        Reporter.__init__(self)
        self.headers = {
            'Content-Type': 'application/json',
        }

    def del_api(self, id):
        content = requests.delete(self.url+id, headers=self.headers)
        return content

    def del_api_response(self, id):
        code = self.del_api(id)
        if code.status_code != 204:
            self.add_log(f"{self.del_api_content.__name__}: {code.json()['detail']}")
            return False
        return True

    def del_api_content(self, id):
        content = self.del_api(id).json()
        try:
            self.add_log(f"{self.del_api_content.__name__}: {content['detail']}")
            return False
        except IndexError:
            return True
