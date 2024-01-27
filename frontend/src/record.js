import React, { useState, useRef } from 'react';
import { ReactMic } from 'react-mic';
import CanvasDraw from 'react-canvas-draw';

import './record.css';

const App = () => {
  const [isRecording, setIsRecording] = useState(false);
  const [timer, setTimer] = useState(0);
  const canvasRef = useRef();

  const startRecording = () => {
    setIsRecording(true);
    setTimer(0);
    canvasRef.current.clear();
  };

  const stopRecording = () => {
    setIsRecording(false);
  };

  const onData = (recordedBlob) => {
    // You can handle the audio data here
  };

  const onStop = () => {
    // Recording has stopped
  };

  const updateTimer = () => {
    setTimer((prevTimer) => prevTimer + 1);
  };

  return (
    <div className="app">
      <button onClick={isRecording ? stopRecording : startRecording}>
        {isRecording ? 'Stop Recording' : 'Start Recording'}
      </button>
      <div className="timer">Timer: {formatTime(timer)}</div>
      {isRecording && <ReactMic record={isRecording} onStop={onStop} onData={onData} strokeColor="#000000" />}
      <CanvasDraw
        ref={canvasRef}
        canvasWidth={300}
        canvasHeight={100}
        brushColor="#000000"
        style={{ marginTop: '20px' }}
      />
    </div>
  );
};

const formatTime = (seconds) => {
  const minutes = Math.floor(seconds / 60);
  const remainingSeconds = seconds % 60;
  return `${minutes.toString().padStart(2, '0')}:${remainingSeconds.toString().padStart(2, '0')}`;
};

export default App;
