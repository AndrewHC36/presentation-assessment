import React, { useState, useEffect } from 'react';
import { useSpring, animated } from 'react-spring';
// import data from './record.js';
import './results.css';

// Simulated data (replace with your actual data)
const resultsData = {
  overallScore: 45,
  categories: [
    { name: "Content", score: 80 },
    { name: "Delivery", score: 70 },
    { name: "Engagement", score: 85 },
  ],
  feedback: [
    "Clear and concise speech.",
    "Engaging delivery style.",
    "Room for improvement in slide transitions.",
  ],
};

const cleanPercentage = (percentage) => {
  const isNegativeOrNaN = !Number.isFinite(+percentage) || percentage < 0; // we can set non-numbers to 0 here
  const isTooHigh = percentage > 100;
  return isNegativeOrNaN ? 0 : isTooHigh ? 100 : +percentage;
};

const Circle = ({ colour, percentage }) => {
  const r = 70;
  const circ = 2 * Math.PI * r;
  const strokePct = ((100 - percentage) * circ) / 100; // where stroke will start, e.g. from 15% to 100%.
  return (
    <circle
      r={r}
      cx={100}
      cy={100}
      fill="transparent"
      stroke={strokePct !== circ ? colour : ""} // remove colour as 0% sets full circumference
      strokeWidth={"2rem"}
      strokeDasharray={circ}
      strokeDashoffset={percentage ? strokePct : 0}
    ></circle>
  );
};

const Pie = ({ percentage, colour, scoreAnimation }) => {
  const pct = cleanPercentage(percentage);
  return (
    <div className="pie-container">
      <svg width={310} height={200}>
        <g transform={`rotate(-90 ${"100 100"})`}>
          <Circle colour="lightgrey" />
          <Circle colour={colour} percentage={pct} />
        </g>
      </svg>
      <div className="overall-score">
        <animated.p>{scoreAnimation.score.interpolate(score => `${Math.round(score)}%`)}</animated.p>
      </div>
    </div>
  );
};


class Results extends React.Component {
  constructor(props) {
    super(props);

    const [loading, setLoading] = useState(true);
    const [scoreAnimation, setScoreAnimation] = useSpring(() => ({
      score: 0,
      from: { score: 0 },
    }));

    useEffect(() => {
      // Simulate asynchronous data loading
      const loadData = async () => {
        // Simulate loading time
        await new Promise(resolve => setTimeout(resolve, 6000));
  
        // Data loaded, update loading state
        setLoading(false);
  
        // Animate the overall score
        setScoreAnimation({ score: this.props.data["general_score"] });
      };
  
      loadData();
    }, [setScoreAnimation]);
  }

  colorPicker (overallScore) {
    if (overallScore < 60) {
      return '#D81D13'
    }
    else if (overallScore < 80) {
      return '#EFC700'
    }
    else {
      return '#009950'
    }
  }

  render() {
    return (
      <div className="results-container">
        {loading ? (
          <div className="loading-ui">Loading...</div>
        ) : (
          <>
            <div className="App">
              <h2>Overall Presentation Score</h2>
              <div className='overall-score' width={310} height={200}>
                <Pie percentage={this.props.data["general_score"]} colour={colorPicker(this.props.data["general_score"])} scoreAnimation={scoreAnimation} />
                <div className="overall-score-container">
                  <animated.p className="overall-score-text">
                    {scoreAnimation.score.interpolate(score => `${Math.round(score)}%`)}
                  </animated.p>
                </div>
              </div>
            </div>
  
  
            <div className="category-scores">
              <h2>Category Scores</h2>
              <ul>
                {resultsData.categories.map((category, index) => (
                  <li key={index}>
                    <span>{category.name}</span>
                    <span>{category.score}%</span>
                  </li>
                ))}
              </ul>
            </div>
  
            <div className="feedback-section">
              <h2>Feedback</h2>
              <ul>
                {resultsData.feedback.map((item, index) => (
                  <li key={index}>{item}</li>
                ))}
              </ul>
            </div>
          </>
        )}
      </div>
    );
  }
}



// const Results = () => {
  // const [loading, setLoading] = useState(true);
  // const [scoreAnimation, setScoreAnimation] = useSpring(() => ({
  //   score: 0,
  //   from: { score: 0 },
  // }));

 


// };

export default Results;