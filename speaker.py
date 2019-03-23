from watson_developer_cloud import TextToSpeechV1
from playsound import playsound

class Speaker:
    def __init__(self):
        self.text_to_speech = TextToSpeechV1(
            iam_apikey='_gdnDWoLtziIlxTRqmwD4O6wpI2Lh7pQP3lIaw-4t1so',
            url='https://stream.watsonplatform.net/text-to-speech/api'
        )

    def getAudioFile(self, descString, filename):
        with open(filename+'.wav', 'wb') as audio_file:
            audio_file.write(
                self.text_to_speech.synthesize(
                    descString,
                    'audio/wav',
                    'pt-BR_IsabelaVoice'
                ).get_result().content)

    def playDescription(self, filename):
        playsound(filename+".wav")
