import os

from flask import Flask, request, flash, redirect, url_for
from werkzeug.utils import secure_filename

from analyzer import analyze
from score_generator import score_generator


UPLOAD_FOLDER = '/audio'
ALLOWED_EXTENSIONS = {"mp3", "wav", "flac"}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.post("/upload_audio")
def upload_audio():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name = filename))


#if __name__ == '__main__':
    # testing

    # the free api only checks for spelling
    #result = analyze("I love IrvineHacks! And I've yes to eat my breakfast. I forgot, becuase I dont know.")
    #print("RESULT:")
    #print(result)
    #score = score_generator(result)
    #print("SCORE:")
    #print(score)
