from pathlib import Path

import requests
from google.cloud import speech_v1
import base64


def transcriber(fpath: Path) -> str:
    with open(fpath, "rb") as fobj:
        fdata = fobj.read()

    audio_blob = base64.b64encode(fdata)
    # print(audio_blob)

    client = speech_v1.SpeechClient()

    config = speech_v1.RecognitionConfig()
    config.audio_channel_count = 1
    config.encoding = "FLAC"
    config.sample_rate_hertz = 48000
    config.language_code = "en-US"
    config.enable_word_time_offsets = False
    # config.model = "latest_short"
    # config.enable_word_confidence = True
    # config.metadata.recording_device_type = "SMARTPHONE"

    audio = speech_v1.RecognitionAudio()
    audio.content = audio_blob.decode("ascii")
    # audio.uri = "gs://cloud-samples-tests/speech/brooklyn.flac"

    request = speech_v1.RecognizeRequest(config = config, audio = audio)

    response = client.recognize(request=request)

    print("Billed Time:", response.total_billed_time)
    print("Results:", response.results)
    print("Adaptations:", response.speech_adaptation_info)


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
    result = transcriber(Path("./audio/ums_and_uhs.flac"))
