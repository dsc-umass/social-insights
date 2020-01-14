import React, {Component} from 'react';
import '../App.css';
import Results from './Results'
import Search from './Search'

import {
  BrowserRouter,
  Route,
  Link,
} from 'react-router-dom'

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <div align='center'>
            <h1>Health Insights</h1>
        </div>
        <div>
          <Route exact path='/' component={Search} />
        </div>
      </BrowserRouter>
    )
  }
}

export default App;
