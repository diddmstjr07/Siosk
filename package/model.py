from .neuron import NeuronAggregate
from google_speech import Speech
from .client.anoask import Api
import os
import subprocess

class API:
    def __init__(self, token) -> None:
        self.token = token
        pass

    def load_models(self):
        api = Api()
        Neuron = NeuronAggregate()
        return api, Neuron

    def siosk(self):
        api, Neuron = self.load_models()
        index = Neuron.Detection()
        while True:
            print("Talking...")
            keyword = Neuron.Trans(index)
            print("Speaking...")
            if keyword == None:
                pass
            else:
                keywords = str(keyword).split()
                for i in range(len(keywords)):
                    if keywords[i] == "멈춰":
                        speech = Speech(str("프로그램 가동을 멈춥니다."), "ko")
                        speech.play()
                        print("Stopping and Exiting...")
                        os._exit(0)
            print(keyword)
            result, embedding_time = api.send_response(self.token, keyword)
            speech = Speech(result, "ko")
            speech.play()
        