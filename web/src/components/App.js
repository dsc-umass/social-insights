import React, {Component} from 'react';
import '../App.css';
import Search from './Search'
import Results from './Results'
import {
  BrowserRouter,
  Route,
  Link,
} from 'react-router-dom'

class App extends Component {
  render() {
    return (
      <div>
        <h1 align='center'>Health-Insights</h1>
      </div>
    )
  }
}

export default App;
