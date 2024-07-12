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
        mic = self.detection.Microphone(device_index=index)
        try:
            with mic as source:
                self.detector.dynamic_energy_threshold = True
                print("Listening...")  # 사용자에게 듣고 있음을 알림
                audio = self.detector.listen(source, timeout=15, phrase_time_limit=2.5)
                print("Recognizing...")  # 인식 중임을 알림
                result = self.detector.recognize_google(audio, language='ko-KR')
                return result
        except self.error_non:
            print("음성이 감지되지 않았습니다.")
            return None
        except self.error_wait:
            print("시간 초과되었습니다.")
            return None