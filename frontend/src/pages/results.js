import React, { useState, useEffect } from 'react';
import './results.css';

const Results = () => {
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState(null);

  useEffect(() => {
    // Simulate an asynchronous data fetching process
    const fetchData = async () => {
      try {
        // Replace this with your actual API endpoint
        const response = await fetch('/result');
        const resultData = await response.json();
        
        // Simulate a delay for loading purposes
        await new Promise(resolve => setTimeout(resolve, 1000));

        setData(resultData);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching data:', error);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="results-container">
      {loading ? (
        <div className="loading">Loading...</div>
      ) : (
        <div className="result-content">
          <h2>Results</h2>
          <div className="percentage">{data.percentage}% Complete</div>
          <ul>
            {data.results.map((result, index) => (
              <li key={index}>{result}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default Results;