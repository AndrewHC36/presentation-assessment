import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';
import Record from "./pages/record";
import Results from './pages/results'

const App = () => {
  return (
    <Router>
      <div>
        <header>
          <div className="nav-bar">
            <Link to="/" className="app-name">Presentation Analyzer</Link>
            <ul className="nav-links">
              <Link to="/" className="nav-link">Home</Link>
              <Link to="/about" className="nav-link">About</Link>
              <Link to="/contact" className="nav-link">Contact</Link>
            </ul>
          </div>
        </header>

        <Routes>
          <Route path="/record" element={<Record />} />
          <Route path="/results" element={<Results />} />
          <Route path="/" element={<div id="app-container">
            <h1>Presentation Analyzer</h1>
            <div id="upload-section">
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
                <li className="feedback-item">Clear and concise speech.</li>
                <li className="feedback-item">Engaging delivery style.</li>
              </ul>
            </div>
          </div>} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
