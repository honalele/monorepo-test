import logo from './logo.svg';
import './App.css';
import { add } from '@monorepo-test/utils';
function App() {
  const result = add(3, 5);
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Addition result of 3 and 5 is: <h1>{result}</h1>
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
