from .neuron import NeuronAggregate
from google_speech import Speech
from Siosk.package.anoask import Api
from Siosk.package.TTS import TextToSpeech
import time
from Siosk.package.error_manage import ConnectionRefusedError
from Siosk.package.error_manage import ServerDownedError
import os
import six
import socket
import requests
import webbrowser

class API:
    def __init__(self, token, url) -> str:
        self.token = token # Api Token
        self.url = url # Sending url
        self.TextToSpeech = TextToSpeech()

    def access_server(self):
        start_time = time.time()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(("pwnbit.kr", 443))
            response = requests.get(f"{self.url}:9460/access?token={self.token}&host={os.getlogin()}&ip={sock.getsockname()[0]}", verify=False) # 쿼리문자열을 활용한 Get 요청을 보냄 
            result = response.json()['message'] # json 데이터로 추출하여 detail 키에 대한 값을 변수에 저장
            if result == 'error': # 토큰이 부적절한 경우 에러 메세지를 띄움
                webbrowser.open(self.url)
                print("\033[31m" + '403 Refused Error' + "\033[0m" + ': None Coincide Token values, Please check if your token is expired')
                print('to get new token, please visit https://anoask.site and login to issue')
                raise ConnectionRefusedError
        except KeyError: # 키에러인 경우, 적절하게 반환된 결과이기 때문에, 추출
            result = response.json()['message'] # 결과 추출
            end_time = time.time() # 종료
            embedding_time = end_time - start_time # 임배디드 시간 측정
            return result, embedding_time # 결과나 임배디드 시간 반환
        except requests.exceptions.ConnectionError:
            print("\033[31m" + '404 Refused Error' + "\033[0m" + ': Server is downed... Please Contact us we will found problem immediately') # 연결 에러인 경우, 서버 다운 메세지 출력
            raise ServerDownedError

    def load_models(self):
        api = Api(url=self.url) 
        Neuron = NeuronAggregate() # 음성관련 class 호출 
        return api, Neuron

    def preparing(self): # 준비 함수 
        api, Neuron = self.load_models() # api -> get 요청할때 사용, Neuron -> 마이크 선택과 음성 변환
        index = Neuron.Detection() # 마이크 선택
        self.api = api # 인스턴스 변수로 선언
        self.index = index # 인스턴스 변수로 선언
        self.Neuron = Neuron # 인스턴스 변수로 선언

    def texture_load_models(self):
        api = Api(url=self.url) # 클래스 매게변수로써 지정
        return api # 클래쓰 변수를 return 

    def texture_preparing(self):
        api = self.texture_load_models() # return한 클래쓰 변수를 변수에 저장
        self.api = api # 인스턴스 변수로써 클래쓰를 호출하여 저장

    def texture(self, keyword):
        if isinstance(keyword, six.string_types):  # keyword의 종류가 문자열인지 확인
            result, embedding_time = self.api.send_response(self.token, keyword) # 위에서 매개변수로 삼은 token과 받은 keyword를 매개변수로써 전송
            return result, embedding_time # 다시 결과와 시간을 return
        else:
            os._exit(0) # 문자의 종류가 str이 아닌 경우 exit

    def detection(self, result):
        filename = "./SioPackage/Siosk/assets/audio/" + result + ".mp3" 
        if os.path.isfile(filename):
            self.TextToSpeech.voice(resultment=filename, flag=True)
        else:
            self.TextToSpeech.convert_prepare(target_data=result)
            self.TextToSpeech.voice(resultment=False, flag=False)
    
    def detecting(self):
        print("Talking...")
        self.keyword = self.Neuron.Trans(self.index) # 음성 정보를 keyword로써 변환후 변수에 저장
        print("Speaking...")
        keywords = str(self.keyword).split(" ") # 문자 하나하나 모두 각각 배열로 분할
        for i in range(len(keywords)):
            if keywords[i] == "멈춰": # 멈춰 단어가 인식되면 종료
                speech = Speech(str("프로그램 가동을 멈춥니다."), "ko") # TTS
                speech.play()
                print("Stopping and Exiting...")
                os._exit(0)
        print(self.keyword) # 단어 출력
        result, embedding_time = self.api.send_response(self.token, self.keyword) # 위에서 매개변수로 삼은 token과 받은 keyword를 매개변수로써 전송
        print(embedding_time) # 시간 출력
        self.detection(result)