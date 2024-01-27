
import React from 'react';
import './App.css';

const App = () => {
  return (
    <div>
      <header>
        <div className="nav-bar">
          <a href="#" className="app-name">Presentation Analyzer</a>
          <ul className="nav-links">
          <a href="#" className="nav-link">Home</a>
            <a href="#" className="nav-link">About</a>
            <a href="#" className="nav-link">Developers</a>
          </ul>
        </div>
      </header>

      <div id="app-container">
        <h1>Presentation Analyzer</h1>

        <div id="upload-section">
          <button id="upload-btn">Upload Presentation</button>
        </div>

        <div id="score-section">
          <h2>Presentation Scores</h2>
          {/* Display scores here */}
        </div>

        <div id="feedback-section">
          <h2>Feedback Examples</h2>
          <ul id="feedback-list">
            {/* Display feedback items here */}
            <li className="feedback-item">Clear and concise speech.</li>
            <li className="feedback-item">Engaging delivery style.</li>
            {/* Add more feedback items as needed */}
          </ul>
        </div>
      </div>
    </div>
  );
};

export default App;
