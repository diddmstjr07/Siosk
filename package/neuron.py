from .converter import SpeechToTextConverter

class NeuronAggregate:
    def __init__(self) -> None:
        import google_speech 
        import speech_recognition
        import os
        import time
        self.converter = SpeechToTextConverter() # 모델 로드, Google_Speech, SpeechRecognition converter 변수에 저장
        self.detection = speech_recognition
        self.TTS = google_speech
        self.time = time
        self.os = os
    
    def Neuron(self):
        pass

    def Detection(self):
        micro_result = self.converter.check_microphone() # 반환한 마이크 배열 데이터를 변수에 저장
        # for i in range(len(micro_result)):
        #     if "MacBook Pro 마이크" in micro_result[i]:
        #         return int(str(micro_result[i])[1])
        print("\n-----------------------------------")
        for i in range(len(micro_result)): 
            print(micro_result[i]) # 마이크 정보 출력
        print("-----------------------------------\n")
        index = int(input("Please Select Microphone and Type number of index: "))
        return index # 선택한 인덱스 반환

    def Trans(self, index):
        text_result = self.converter.Detecting(index) # 인식된 text를 다시 변환
        print("text_result: " + str(text_result)) # String으로 변환하여 결과 출력
        if text_result == None: # 아무것도 인식되어지지 않은 경우
            while True:
                text_result = self.converter.Detecting(index) # 인식될때까지 무한 반복
                if text_result != None:
                    print(text_result)
                    return text_result # 인식되면 return
        else:
            return text_result # 바로 인식된 경우, 바로 반환
