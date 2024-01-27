// App.js

import React from 'react';
import { BrowserRouter as Router, Route, Link, Switch } from 'react-router-dom';
import './App.css';
import Record from './pages/record.js';

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

        <Switch>
          <Route path="/record" component={Record} />
          <Route path="/" exact>
            <div id="app-container">
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
            </div>
          </Route>
        </Switch>
      </div>
    </Router>
  );
};

export default App;
