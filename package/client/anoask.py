import requests
from urllib3.exceptions import InsecureRequestWarning
import time
from package.error_manage import ConnectionRefusedError
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import webbrowser

url = "https://anoask.site"

class Api:
    def __init__(self) -> None:
        pass

    def send_response(self, token, ques):
        start_time = time.time()
        response = requests.get(f"https://anoask.site:9460/api?token={token}&ques={ques}", verify=False)
        try:
            result = response.json()['detail']
            if result == 'error':
                webbrowser.open(url)
                print('403 Refused Error: None Coincide Token values, Please check if your token is expired')
                print('to get new token, please visit https://anoask.site and login to issue')
                raise ConnectionRefusedError
        except KeyError:
            result = response.json()['message']
            end_time = time.time()
            embedding_time = end_time - start_time
            return result, embedding_time