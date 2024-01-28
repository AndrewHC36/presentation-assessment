import os
import subprocess
from pathlib import Path
import time
from dataclasses import dataclass
from typing import Optional

from flask import Flask, request, flash, redirect, url_for
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename


import transcriber_deepgram


@dataclass
class AssessmentResult:
    transcript: str
    general_score: int  # 5 to 99
    error_locations: list[(int, int)]  # start pos, end pos
    warning_locations: list[(int, int)]  # start pos, end pos


def process_data(fpath: str) -> Optional[AssessmentResult]:
    transcription = transcriber_deepgram.transcriber(Path(fpath))
    print("TRANSCRIPTION:")
    print(transcription)
    # analysis = analyzer_prowritingaid.analyze(transcription)

    if len(transcription.alternatives) > 0:
        return AssessmentResult(
            transcript = transcription.alternatives[0].transcript,
            general_score = 50,
            error_locations = [

            ],
            warning_locations = [

            ],
        )
    else:
        return None



UPLOAD_FOLDER = './audio'
ALLOWED_EXTENSIONS = {"mp3", "wav", "flac"}

app = Flask(__name__)
cors = CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = "SECRET_KEY"


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.post("/upload_audio")
@cross_origin()
def upload_audio():
    if request.method == 'POST':
        # print(f"REQ FILES: {request.files}")

        # check if the post request has the file part
        if 'audio_file' not in request.files:
            flash('No file part')
            return {
                "valid": False,
                "message": "No file part"
            }
        file = request.files['audio_file']
        # print(f"FILE: {file.filename}")

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return {
                "valid": False,
                "message": "No selected file"
            }

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            flac_fname = f"{time.time_ns()}.flac"
            subprocess.run([
                "ffmpeg", "-i",
                os.path.join(app.config['UPLOAD_FOLDER'], filename),
                os.path.join(app.config['UPLOAD_FOLDER'], flac_fname),
            ])
            assessment_result = process_data(os.path.join(app.config['UPLOAD_FOLDER'], flac_fname))
            if assessment_result is not None:
                return {
                    "valid": True,
                    "general_score": assessment_result.general_score,
                    "transcript": assessment_result.transcript,
                    "errors": [  # red underline
                        [s, e]
                        for (s, e) in assessment_result.error_locations
                    ],
                    "warnings": [  # yellow underline
                        [s, e]
                        for (s, e) in assessment_result.warning_locations
                    ],
                }
            else:
                return {
                    "valid": False,
                    "message": "No transcription available due to unintelligible audio"
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
