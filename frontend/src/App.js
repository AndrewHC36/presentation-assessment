
import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';
import Record from "./pages/record";

const App = () => {
  return (
    <Router>
      <div>
        <header>
          <div className="nav-bar">
            <a href="#" className="app-name">Presentation Analyzer</a>
            <ul className="nav-links">
              <a href="#" className="nav-link">Home</a>
              <a href="#" className="nav-link">About</a>
              <a href="#" className="nav-link">Contact</a>
            </ul>
          </div>
        </header>

        <Routes>
          <Route path="/record" element={<Record />} />
          <Route path="/" element={<div id="app-container">
            <h1>Presentation Analyzer</h1>
            <div id="upload-section">
              {/* Use Link to navigate to the /record page */}
              <Link to="/record" className="upload-btn-link">
                <button id="upload-btn">Start Recording</button>
              </Link>
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
          </div>} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;