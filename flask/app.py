# import os
# from flask import Flask, render_template, url_for, request, session, flash, redirect
# from werkzeug.utils import secure_filename
# import base64
# from google.cloud import speech_v1

# UPLOAD_FOLDER = '/path/to/the/uploads'
# ALLOWED_EXTENSIONS = {'mp3'}

# app = Flask(__name__)
# app.config['ALLOWED_EXTENSIONS'] = UPLOAD_FOLDER

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.')[1].lower() in ALLOWED_EXTENSIONS


# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']

#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('download_file', name=filename))


# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request
from google.cloud import speech_v1 as speech
import base64


app = Flask(__name__)

def audio_file_to_base64(file_path):
    with open(file_path, 'rb') as audio_file:
        # reads the binary content of the audio file 
        audio_content = audio_file.read()

        encode_base64 = base64.b64encode(audio_content).decode('utf-8')

    return encode_base64

def transcribe_audio(base64_file):
    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(content=base64_file)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US',
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return 'No file part in the request'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    # Save the file locally
    file_path = 'audio_upload.mp3'
    file.save(file_path)

    # Transcribe the audio
    transcribe_audio(file_path)

    return 'Transcription request submitted successfully'

if __name__ == '__main__':
    app.run(debug=True)


