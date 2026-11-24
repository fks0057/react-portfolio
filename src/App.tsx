
import { HashRouter, Routes, Route } from "react-router";
import Home from "./pages/Home";
import WeatherML from "./pages/WeatherML";
import "./App.css";

function App() {
  return (
    <HashRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route
          path="/projects/weather-ml"
          element={<WeatherML />}
        />
      </Routes>
    </HashRouter>
  );
}

export default App;
