import React, { useState, useEffect } from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';
import Record from "./pages/record";
import Results from './pages/results'
import { useCallback } from "react";
// import Particles from "react-tsparticles";
import { loadFull } from "tsparticles";

const App = () => {
  const [data, setData] = useState({"general_score": 99});

  const particlesInit = useCallback(async engine => {      
    await loadFull(engine);
  }, []);

  const particlesLoaded = useCallback(async container => {
    await console.log(container);
  }, []);

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

        {/* <Particles
          id="tsparticles"
          init={particlesInit}
          loaded={particlesLoaded}
          options={{ "fullScreen": true, "background":{ "image":" linear-gradient(19deg, #21D4FD 0%, #B721FF 100%)" }, "particles":{ "number":{ "value":10, "density":{ "enable":true, "value_area":600 } }, "color":{ "value":"#ffffff" }, "shape": { "type": "square", "stroke":{ "width":0, "color":"#000000" }, "polygon":{ "nb_sides":5 } }, "opacity":{ "value":0.25, "random":true, "anim":{ "enable":false, "speed":1, "opacity_min":0.1, "sync":false } }, "size":{ "value":29, "random":true, "anim":{ "enable":false, "speed":2, "size_min":0.1, "sync":false } }, "line_linked":{ "enable":false, "distance":300, "color":"#ffffff", "opacity":0, "width":0 }, "move":{ "enable":true, "speed":0.5, "direction":"top", "straight":true, "out_mode":"out", "bounce":false, "attract":{ "enable":false, "rotateX":600, "rotateY":1200 } } }, "interactivity":{ "detect_on":"canvas", "events":{ "onhover":{ "enable":false, "mode":"repulse" }, "onclick":{ "enable":false, "mode":"push" }, "resize":true }, "modes":{ "grab":{ "distance":800, "line_linked":{ "opacity":1 } }, "bubble":{ "distance":790, "size":79, "duration":2, "opacity":0.8, "speed":3 }, "repulse":{ "distance":400, "duration":0.4 }, "push":{ "particles_nb":4 }, "remove":{ "particles_nb":2 } } }, "retina_detect":true}}
        /> */}

        <Routes>
          <Route path="/record" element={<Record data={data} setData={setData} />} />
          <Route path="/results" element={<Results data={data} setData={setData} />} />
          <Route path="/" element={<div id="app-container">

            <div id="upload-section">
              <Link to="/record" className="upload-btn-link">
                <button id="upload-btn">Start Recording</button>
              </Link>
            </div>

            <div>
              <h2 id="blurb-center">What we do. 🗣️</h2>
              <p>
                Presentation Analyzer is the service to improve your presentation and speaking skills.
                With AI models at the tip of your microphone, we <b>strive</b> excellency and quality to make sure
                you get the highest quality of analysis at <i>no delay!</i>
              </p>
              <h2 id="blurb-center">Why? </h2>
              <p>

              </p>
              <h2 id="blurb-center">How we accomplish. </h2>
              <p>

              </p>
              <h2 id="blurb-center">How we can help you. 🫵</h2>
            </div>

          </div>} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
