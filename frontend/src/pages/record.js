import React, { useState, useEffect } from 'react';
import { ReactMic } from 'react-mic';
import { saveAs } from 'file-saver';

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

  const onData = (recordedBlob) => {
    setAudioChunks((prevChunks) => [...prevChunks, recordedBlob.blob]);
  };

  const onStop = () => {
    if (audioChunks.length > 0) {
      const audioBlob = new Blob(audioChunks, { type: 'audio/mp3' });
      saveAs(audioBlob, `recorded_audio_${new Date().toISOString()}.mp3`);
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
    return `${String(minutes).padStart(2, '0')}:${String(remainingSeconds).padStart(2, '0')}`;
  };

  const visualSettings = {
    showFrequency: true,  // Set to false to hide frequency bar
    showWaveform: true,   // Set to false to hide waveform
    visualizerWidth: 400, // Adjust the width of the visualizer
    visualizerHeight: 100, // Adjust the height of the visualizer
    backgroundColor: '#ffffff', // Change the background color
    strokeColor: '#000000',    // Change the stroke color
    strokeWidth: 2,            // Adjust the stroke width
    fill: true,                // Set to false to disable fill
    fillParent: true,          // Set to false to disable fill parent
    magnitudeMode: 'sensitive', // Change the magnitude mode ('sensitive' or 'rigid')
  };

  return (
    <div className="app">
      <button onClick={isRecording ? stopRecording : startRecording}>
        {isRecording ? 'Stop Recording' : 'Start Recording'}
      </button>
      <div className="timer">Timer: {formatTime(timer)}</div>
      <ReactMic
        record={isRecording}
        onStop={onStop}
        onData={onData}
        strokeColor="#000000"
        backgroundColor="#ffffff"
        visualSetting={visualSettings}
      />
    </div>
  );
};

export default Record;
