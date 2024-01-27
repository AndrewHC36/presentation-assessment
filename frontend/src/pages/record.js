import React, { useState, useEffect } from 'react';
import { ReactMic } from 'react-mic';

import './record.css';

const Record = () => {
  const [isRecording, setIsRecording] = useState(false);
  const [timer, setTimer] = useState(0);
  const [audioChunks, setAudioChunks] = useState([]);

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

  const startRecording = () => {
    setIsRecording(true);
    setTimer(0);
    setAudioChunks([]); // Clear previous audio chunks
  };

  const stopRecording = () => {
    setIsRecording(false);
    // You can now use the audioChunks to generate a download link or send it to a server for further processing.
    downloadAudio();
  };

  const onData = (recordedBlob) => {
    // Handle the audio data, e.g., store it in state
    setAudioChunks((prevChunks) => [...prevChunks, recordedBlob.blob]);
  };

  const downloadAudio = () => {
    const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
    const audioUrl = URL.createObjectURL(audioBlob);

    const link = document.createElement('a');
    link.href = audioUrl;
    link.download = `recorded_audio_${new Date().toISOString()}.wav`;
    document.body.appendChild(link);
    link.click();

    // Clean up
    document.body.removeChild(link);
    URL.revokeObjectURL(audioUrl);
  };

  const formatTime = (seconds) => {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;
    return `${String(minutes).padStart(2, '0')}:${String(remainingSeconds).padStart(2, '0')}`;
  };

  return (
    <div className="app">
      <button onClick={isRecording ? stopRecording : startRecording}>
        {isRecording ? 'Stop Recording' : 'Start Recording'}
      </button>
      <div className="timer">Timer: {formatTime(timer)}</div>
      {isRecording && <ReactMic record={isRecording} onStop={() => {}} onData={onData} strokeColor="#000000" className="react-mic" />}
    </div>
  );
};

export default Record;
