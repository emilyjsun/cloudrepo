import logo from './logo.svg';
import './App.css';
// import Navigationbar from "./Components/Navigationbar.js";
// import "bootstrap/dist/css/bootstrap.min.css";


function App() {
  return (
    <div className="App">
      {/* <Navigationbar></Navigationbar> */}
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          HELLO WORLD
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn
        </a>
      </header>
    </div>
  );
}

export default App;
