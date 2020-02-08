import React, {Component} from 'react';
import '../App.css';
import AutoComplete from './AutoComplete';

import {
  BrowserRouter,
  Route,
  Link,
} from 'react-router-dom'

class App extends Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <AutoComplete />
      </div>
    )
  }
}

export default App;
