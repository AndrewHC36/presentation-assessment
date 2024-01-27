import requests

def analyze(transcription: str):
    resp = requests.get(
        "https://api.languagetoolplus.com/v2/check",
        params = {
            "text": transcription,
            "language": "en-US"
        },
    )

    data = resp.json()

    print("LANG:", data["language"])
    for m in data["matches"]:
        print("ERROR MATCHED")
        print("Message:", m["message"])
        print("Short Message:", m["shortMessage"])
        print("Replacements:", m["replacements"])
        print("Error Offset:", m["offset"])
        print("Error Length:", m["length"])
        print("Context:", m["context"])
        print("ISSUE TYPE:", m["rule"]["issueType"])
        print("CATEGORY:", m["rule"]["category"])

    return data


if __name__ == '__main__':
    # testing

    result = analyze("I love IrvineHacks!")
    print("RESULT:")
    print(result)

