import React, {Component} from 'react';
import '../App.css';
import Results from './Results'
import Home from './Home'

import {
  BrowserRouter,
  Route,
  Link,
} from 'react-router-dom'

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <div>
          <Route exact path='/' component={Home} />
          <Route exact path='/results' component={Results} />
        </div>
      </BrowserRouter>
    )
  }
}

export default App;
