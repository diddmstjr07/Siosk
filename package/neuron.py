from .converter import SpeechToTextConverter
import os

class NeuronAggregate:
    def __init__(self) -> None:
        import google_speech
        import speech_recognition
        import os
        import time
        self.detection = speech_recognition
        self.TTS = google_speech
        self.time = time
        self.os = os
    
    def Neuron(self):
        pass

    def Detection(self):
        converter = SpeechToTextConverter()
        micro_result = converter.check_microphone()
        for i in range(len(micro_result)):
            if "MacBook Pro 마이크" in micro_result[i]:
                return int(str(micro_result[i])[1])
        # print("\n-----------------------------------")
        # for i in range(len(micro_result)):
        #     print(micro_result[i])
        # print("-----------------------------------\n")
        # index = int(input("Please Select Microphone and Type number of index: "))
        # return index

    def Trans(self, index):
        converter = SpeechToTextConverter()
        text_result = converter.Detecting(index)
        if text_result == None:
            os._exit(0)
        else:
            return text_result
