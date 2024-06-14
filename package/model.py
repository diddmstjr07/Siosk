from .neuron import NeuronAggregate
from google_speech import Speech
from Siosk.package.anoask import Api
import os
import six

class API:
    def __init__(self, token) -> None:
        self.token = token
        pass

    def load_models(self):
        api = Api()
        Neuron = NeuronAggregate()
        return api, Neuron

    def preparing(self):
        api, Neuron = self.load_models()
        index = Neuron.Detection()
        self.api = api
        self.index = index
        self.Neuron = Neuron

    def texture_load_models(self):
        api = Api()
        return api

    def texture_preparing(self):
        api = self.texture_load_models()
        self.api = api

    def texture(self, keyword):
        if isinstance(keyword, six.string_types): 
            result, embedding_time = self.api.send_response(self.token, keyword)
            return result, embedding_time
        else:
            os._exit(0)
    
    def detecting(self):
        print("Talking...")
        self.keyword = self.Neuron.Trans(self.index)
        print("Speaking...")
        if self.keyword == None:
            pass
        else:
            keywords = str(self.keyword).split()
            for i in range(len(keywords)):
                if keywords[i] == "멈춰":
                    speech = Speech(str("프로그램 가동을 멈춥니다."), "ko")
                    speech.play()
                    print("Stopping and Exiting...")
                    os._exit(0)
        print(self.keyword)
        result, embedding_time = self.api.send_response(self.token, self.keyword)
        print(embedding_time)
        speech = Speech(result, "ko")
        speech.play()