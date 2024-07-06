class SpeechToTextConverter:
    def __init__(self):
        import speech_recognition
        self.detection = speech_recognition
        self.detector = self.detection.Recognizer()
        self.recognizer = self.detection.Recognizer()
        self.error_non = speech_recognition.exceptions.UnknownValueError
        self.error_wait = speech_recognition.exceptions.WaitTimeoutError

    def check_microphone(self):
        detected = []
        for index, name in enumerate(self.detection.Microphone.list_microphone_names()):
            detected.append(str(f"[{index}] {name}")) # 존재하는 마이크 append
        return detected
    
    def Detecting(self, index):
        mic = self.detection.Microphone(device_index=index) # 지정된 마이크로 음성 인식 시작
        try:
            with mic as source:
                audio = self.detector.listen(source, timeout = 10, phrase_time_limit = 1.5)
                result = self.detector.recognize_google(audio, language='ko-KR')
                return result
        except self.error_non:
            print("Non Voice Detected")
            return None
        except self.error_wait:
            print("Non Voice Detected")
            return None