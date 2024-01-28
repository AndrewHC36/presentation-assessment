import os
import subprocess
from pathlib import Path
import time

from flask import Flask, request, flash, redirect, url_for
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename

import analyzer_prowritingaid
import transcriber_deepgram
from analyzer import analyze
from score_generator import score_generator


UPLOAD_FOLDER = './audio'
ALLOWED_EXTENSIONS = {"mp3", "wav", "flac"}

app = Flask(__name__)
cors = CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = "SECRET_KEY"


def process_data(fpath: str) -> "Data":
    transcription = transcriber_deepgram.transcriber(Path(fpath))
    print("TRANSCRIPTION:")
    print(transcription)
    # analysis = analyzer_prowritingaid.analyze(transcription)

    return 45


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.post("/upload_audio")
@cross_origin()
def upload_audio():
    if request.method == 'POST':
        print(f"REQ FILES: {request.files}")

        # check if the post request has the file part
        if 'audio_file' not in request.files:
            flash('No file part')
            return {
                "valid": False,
                "message": "No file part"
            }
        file = request.files['audio_file']
        print(f"FILE: {file.filename}")

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return {
                "valid": False,
                "message": "No selected file"
            }

        if file and allowed_file(file.filename):
            print("FILE EXISTS AND ALLOWED")
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            flac_fname = f"{time.time_ns()}.flac"
            subprocess.run([
                "ffmpeg", "-i",
                os.path.join(app.config['UPLOAD_FOLDER'], filename),
                os.path.join(app.config['UPLOAD_FOLDER'], flac_fname),
            ])
            return f"{process_data(os.path.join(app.config['UPLOAD_FOLDER'], flac_fname))}"
            return {
                "valid": True,
                "general_score": 45,  # out of a 100
                
            }


#if __name__ == '__main__':
    # testing

    # the free api only checks for spelling
    #result = analyze("I love IrvineHacks! And I've yes to eat my breakfast. I forgot, becuase I dont know.")
    #print("RESULT:")
    #print(result)
    #score = score_generator(result)
    #print("SCORE:")
    #print(score)
