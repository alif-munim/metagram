import logo from './logo.svg';
import './App.css';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom'
import { Fragment } from 'react';
import Test from "./page/test";
import Alerts from './components/layout/alert';
//Redux
import {Provider} from 'react-redux'
import store from './store'

const App = () =>{
  return (
    <Provider store={store}>
      <Alerts/>
    <Router>
      <Fragment>
        <Route exact path="/" component={Test}/>
      </Fragment>
    </Router>
    </Provider>
  );
}

export default App;
