import './App.css';
import {useState, useEffect} from 'react';
import {Deploy} from './components/Deploy'

function App() {
  const [state, setState] = useState({})

  useEffect(() => {
    fetch('/api', {
      'method':'GET',
      headers: {
        'Content-Type':'applications/json'
      }
    })
    .then(resp => resp.json())
    .then(resp => setState(resp))
    .catch(error => console.log(error))

  },[])

  return (
    <div className="App">
      <Deploy prop={state}/>
    </div>
  );
}

export default App;