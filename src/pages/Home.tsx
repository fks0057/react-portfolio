
import { Link } from "react-router";
import HeadImg from "../assets/capybara.JPG";

function Home() {
  return (
    <main className="home">
      <h1>Yu-Yu Chiang</h1>
      <p>Computer Science Student @ OSU</p>

      <img
        src={HeadImg}
        alt="Capybara chilling"
        width={300}
      />

      <section className="projects">
        <h2>My Projects</h2>

        <div className="project-grid">
          <Link to="/projects/weather-ml" className="project-card">
            <h3>Online Weather Prediction</h3>
            <p>
              Online machine learning for umbrella and
              clothing layer prediction under concept drift.
            </p>
            <span>View Project →</span>
          </Link>
        </div>
      </section>
    </main>
  );
}

export default Home;
