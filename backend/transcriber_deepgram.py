from pathlib import Path
import requests
from dataclasses import dataclass


@dataclass
class WordDurations:
    word: str
    start: float
    end: float

@dataclass
class TranscriptionAlternatives:
    transcript: str
    word_timestamps: list[WordDurations]

@dataclass
class TranscriptionData:
    duration: float
    alternatives: list[TranscriptionAlternatives]


def transcriber(fpath: Path) -> TranscriptionData:
    with open(fpath, "rb") as fobj:
        fdata = fobj.read()

    res = requests.post(
        url = 'https://api.deepgram.com/v1/listen?model=nova-2&filler_words=true',
        data = fdata,
        headers = {
            'Content-Type': 'audio/flac',
            "Authorization": "Token b7d9cf74ae136b9cf8bf4532352358ff830533df",
        }
    )
    data = res.json()
    print(data)
    # return data["results"]["channels"][]

    return TranscriptionData(
        duration = data["duration"],
        alternatives = [
            TranscriptionAlternatives(
                transcript = alt["transcript"],
                word_timestamps = [
                    WordDurations(
                        word = wd["word"],
                        start = wd["start"],
                        end = wd["end"],
                    )
                    for wd in alt["words"]
                ]
            )
            for alt in data["results"]["channels"][0]["alternatives"]
        ]
    )


# if __name__ == '__main__':

#     transcriber(Path("audio/old/ums_and_uhs_2.flac"))
#     return(result)

