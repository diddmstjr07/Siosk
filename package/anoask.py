import requests
from urllib3.exceptions import InsecureRequestWarning
import time
from Siosk.package.error_manage import ConnectionRefusedError
from Siosk.package.error_manage import ServerDownedError

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import webbrowser

class Api:
    def __init__(self, url) -> None:
        self.url = url
        pass

    def send_response(self, token, ques):
        start_time = time.time()
        try:
            response = requests.get(f"{self.url}:9460/api?token={token}&ques={ques}", verify=False)
            result = response.json()['detail']
            if result == 'error':
                webbrowser.open(self.url)
                print("\033[31m" + '403 Refused Error' + "\033[0m" + ': None Coincide Token values, Please check if your token is expired')
                print('to get new token, please visit https://anoask.site and login to issue')
                raise ConnectionRefusedError
        except KeyError:
            result = response.json()['message']
            end_time = time.time()
            embedding_time = end_time - start_time
            return result, embedding_time
        except requests.exceptions.ConnectionError:
            print("\033[31m" + '404 Refused Error' + "\033[0m" + ': Server is downed... Please Contact us we will found problem immediately')
            raise ServerDownedError
