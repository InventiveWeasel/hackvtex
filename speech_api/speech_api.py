from watson_developer_cloud import TextToSpeechV1

text_to_speech = TextToSpeechV1(
    iam_apikey='_gdnDWoLtziIlxTRqmwD4O6wpI2Lh7pQP3lIaw-4t1so',
    url='https://stream.watsonplatform.net/text-to-speech/api'
)

with open('hello_world.wav', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'Olá mundo',
            'audio/wav',
            'pt-BR_IsabelaVoice'
        ).get_result().content)
