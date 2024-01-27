from flask import Flask

from analyzer import analyze
from score_generator import score_generator


app = Flask(__name__)

@app.post("/upload_audio")
def upload_audio():
    return f"{45}"


if __name__ == '__main__':
    # testing

    # the free api only checks for spelling
    result = analyze("I love IrvineHacks! And I've yes to eat my breakfast. I forgot, becuase I dont know.")
    print("RESULT:")
    print(result)
    score = score_generator(result)
    print("SCORE:")
    print(score)
