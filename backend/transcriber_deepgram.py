from pathlib import Path
import requests

def transcriber(fpath: Path) -> str:
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
    print(res.json())

if __name__ == '__main__':
    result = transcriber(Path("./audio/ums_and_uhs_2.flac"))
    print(result)

