import HeadImg from "./assets/capybara.JPG"
import './App.css'

function App() {
  return (
    <main>
      <h1>Yu-Yu Chiang</h1>
      <p>Computer Science Student @ OSU</p>
    
      <img
        src={HeadImg}
        alt="Capybara chilling"
        width={300}
      />
    </main>
  )
}
export default App