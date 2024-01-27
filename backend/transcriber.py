import requests
from google.cloud import speech_v1


def transcriber() -> str:
    client = speech_v1.SpeechClient()

    config = speech_v1.RecognitionConfig()
    config.encoding = "FLAC"
    config.sample_rate_hertz = 16000
    config.language_code = "en-US"
    config.enable_word_time_offsets = False

    audio = speech_v1.RecognitionAudio()
    # audio.content = b'content_blob'
    audio.uri = "gs://cloud-samples-tests/speech/brooklyn.flac"

    request = speech_v1.RecognizeRequest(config = config, audio = audio)

    response = client.recognize(request=request)

    print(response)


    # resp = requests.post(
    #     "https://speech.googleapis.com/v1/speech:recognize",
    #     # headers = {'Authorization': 'TOK:<MY_TOKEN>'}
    #     data = {
    #         "config": {
    #             "encoding": "FLAC",
    #             "sampleRateHertz": 16000,
    #             "languageCode": "en-US",
    #             "enableWordTimeOffsets": False,
    #         },
    #         "audio": {
    #             "uri": "gs://cloud-samples-tests/speech/brooklyn.flac"
    #         }
    #     }
    # )
    #
    # print(resp.json())



if __name__ == '__main__':
    result = transcriber()
