
import { Link } from "react-router";

function WeatherML() {
  return (
    <main className="project-detail">
      <Link to="/" className="back-link">
        ← Back to Home
      </Link>

      <h1>Online Weather-Based Decision Making</h1>

      <p>
        Umbrella and Clothing Layer Prediction under Concept Drift
      </p>

      <h2>Project Overview</h2>
      <p>
        This project applies online machine learning to historical
        weather data to predict whether an umbrella is needed and
        which clothing layer is appropriate.
      </p>

      <h2>Technologies</h2>
      <p>Python, Scikit-learn, Pandas, NumPy</p>

      <h2>Methods</h2>
      <p>
        Online SGD, Exponential Forgetting, Sliding Window,
        and Hedge Expert Ensemble.
      </p>

      <h2>Results</h2>
      <p>
        The Hedge Expert Ensemble achieved an umbrella prediction
        accuracy of 93.2% and an F1-score of 0.745.
      </p>

      <Link to="/" className="back-link">
        ← Return to Projects
      </Link>
    </main>
  );
}

export default WeatherML;
