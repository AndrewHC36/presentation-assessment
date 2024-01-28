import React, { useState, useEffect } from 'react';
import { ReactMic } from 'react-mic';
import { saveAs } from 'file-saver';
import MicRecorder from 'mic-recorder-to-mp3';

const Record = () => {
  const [isRecording, setIsRecording] = useState(false);
  const [timer, setTimer] = useState(0);
  const [audioChunks, setAudioChunks] = useState([]);
  const [audioBlob, setAudioBlob] = useState(null);
  const [audioURL, setAudioURL] = useState(null);
  const [recorder, setRecorder] = useState(new MicRecorder({ bitRate: 128, prefix: "data:audio/mp3;base64,", }));

  useEffect(() => {
    let interval;

    if (isRecording) {
      interval = setInterval(() => {
        setTimer((prevTimer) => prevTimer + 1);
      }, 1000);
    } else {
      clearInterval(interval);
    }

    return () => {
      clearInterval(interval);
    };
  }, [isRecording]);

  const onData = (recordedBlob) => {
    setAudioChunks((prevChunks) => [...prevChunks, recordedBlob.blob]);
  };

  const onStop = () => {
    if (audioChunks.length > 0) {
      const blob = new Blob(audioChunks, { type: 'audio/mp3' });
      setAudioBlob(blob);

      // Save the audio blob as a download
      saveAs(blob, `recorded_audio_${new Date().toISOString()}.mp3`);

      // Create a URL for the audio blob and set it to the state
      // const audioUrl = URL.createObjectURL(blob);
      // console.log(audioURL)
      // setAudioURL(audioUrl);

      // Clear the audio chunks
      setAudioChunks([]);
    }
  };

  const startRecording = () => {
    setIsRecording(true);
    setTimer(0);

    navigator.getUserMedia({ audio: true },
      () => {
        console.log('Permission Granted');
        // this.setState({ isBlocked: false });
      },
      () => {
        console.log('Permission Denied');
        // this.setState({ isBlocked: true })
      },
    );

    console.log("START RECORDING");
    setAudioURL(null);

    recorder
      .start()
      .then(() => {
        this.setState({ isRecording: true });
      }).catch((e) => console.error(e));
  };

  const stopRecording = () => {
    setIsRecording(false);
    
    recorder
      .stop()
      .getMp3()
      .then(([buffer, blob]) => {
        const blobURL = URL.createObjectURL(blob);
        console.log("=====");
        console.log(blob);
        console.log(buffer);
        console.log(blobURL);
        const binaryString = btoa(blobURL)
        console.log(binaryString);

        // var blob = new Blob(buffer, { type: "audio/mp3" } );
        var bUrl = window.URL.createObjectURL(blob);

        setAudioURL(bUrl);

        // send the download link to the console
        console.log('mp3 download:', bUrl);
        // this.setState({ blobURL, isRecording: false });
      }).catch((e) => console.log(e));
  };

  const formatTime = (seconds) => {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;
    console.log(remainingSeconds)
    return `${String(minutes).padStart(2, '0')}:${String(remainingSeconds).padStart(2, '0')}`;
  };

  return (
    <div className="app">
      <button onClick={isRecording ? stopRecording : startRecording}>
        {isRecording ? 'Stop Recording' : 'Start Recording'}
      </button>
      <div className="timer">Timer: {formatTime(timer)}</div>
      <ReactMic record={isRecording} onStop={onStop} onData={onData} strokeColor="#0099ff" />
      {audioURL && (
        <div>
          <audio controls>
            <source src={audioURL} type="audio/mp3" />
            Your browser does not support the audio tag.
          </audio>
        </div>
      )}
    </div>
  );
};

export default Record;