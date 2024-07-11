from google.cloud import texttospeech
from pydub import AudioSegment
from pydub.playback import play
from tqdm import tqdm
import json
import io
import shutil
import os

class Loading:
    def __init__(self) -> None:
        pass

    def setting_progress_bar(self):
        total_steps = 100   
        progress_bar = tqdm(total=total_steps)
        return progress_bar, total_steps

    def update_progress_bar(self, total_steps, progress_bar, percentage):
        steps_to_add = (total_steps * percentage) / 100
        progress_bar.update(steps_to_add)

class TextToSpeech:
    def __init__(self) -> None:
        self.client = texttospeech.TextToSpeechClient()
        self.voicement = texttospeech.VoiceSelectionParams(
            language_code='ko-KR', ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
        )
        self.audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
        self.Loading = Loading()

    def convert_prepare(self, target_data) -> str:
        input_text = texttospeech.SynthesisInput(text=target_data)
        self.response = self.client.synthesize_speech(input=input_text, voice=self.voicement, audio_config=self.audio_config)
    
    def downloading(self):
        folder_path = 'Siosk/assets/audio'
        if os.path.isdir(folder_path):
            shutil.rmtree(folder_path)
            os.mkdir(folder_path)
        else:
            os.mkdir(folder_path)
        progress_bar, total_steps = self.Loading.setting_progress_bar()
        with open('SioskServer/conversation.json', 'r', encoding='utf-8') as file:
            target_datas = json.load(file)
            for target_data_index, target_data_val in enumerate(target_datas):
                target_data_que = str(target_data_val).split(' | ')[0]
                target_data_ans = str(target_data_val).split(' | ')[1]
                input_text = texttospeech.SynthesisInput(text=target_data_ans)
                response = self.client.synthesize_speech(input=input_text, voice=self.voicement, audio_config=self.audio_config)    
                with open(f'Siosk/assets/audio/{target_data_que}' + '.mp3', 'wb') as w:
                    w.write(response.audio_content)
                self.Loading.update_progress_bar(total_steps, progress_bar, 100 / len(target_datas))
    
    def voice(self, resultment, flag):
        if flag == True:
            audio = AudioSegment.from_file(resultment, format="mp3")
            play(audio)
        elif flag == False:
            audio = AudioSegment.from_file(io.BytesIO(self.response.audio_content), format="mp3")
            play(audio)