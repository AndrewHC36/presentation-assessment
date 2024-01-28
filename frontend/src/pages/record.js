import React, { useState, useEffect } from 'react';
import { ReactMic } from 'react-mic';
import { saveAs } from 'file-saver';

const Record = () => {
  const [isRecording, setIsRecording] = useState(false);
  const [timer, setTimer] = useState(0);
  const [audioChunks, setAudioChunks] = useState([]);
  const [audioBlob, setAudioBlob] = useState(null);
  const [audioURL, setAudioURL] = useState(null);

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
      const audioUrl = URL.createObjectURL(blob);
      console.log(audioURL)
      setAudioURL(audioUrl);

      // Clear the audio chunks
      setAudioChunks([]);
    }
  };

  const startRecording = () => {
    setIsRecording(true);
    setTimer(0);
  };

  const stopRecording = () => {
    setIsRecording(false);
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
