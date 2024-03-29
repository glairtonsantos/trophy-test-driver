import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Row, Col, Button } from 'react-bootstrap';

import './App.css';
import useToken from './useToken';

import Panel from '../Panel/Panel';
import Login from '../Login/Login';
import MonsterList from '../Monster/MonsterList';
import CollectCoin from '../Coin/CollectCoin';
import Death from '../Death/Death';
import TrophyList from '../Trophy/TrophyList';


function App() {

  const { token, setToken } = useToken();

  function logout() {
    localStorage.removeItem('token');
    window.location.reload();
  }

  if(!token) {
    return <Login setToken={setToken} />
  }

  return(
    <Container>
      <Row>
        <Col>
          <h1>Trophy - Ribon</h1>
        </Col>
        <Col className="btn-right">
          <Button variant="outline-info" size="sm" onClick={logout}>Exit</Button>
        </Col>
        
      </Row>
      
      <hr></hr>
      <h3>User - Panel</h3>
      <Panel></Panel>

      <hr></hr>
      <h3>User - Actions</h3>
      <div className="row">
        <CollectCoin></CollectCoin>
        
        <MonsterList></MonsterList>
        
        <Death></Death>
      </div>

      <hr></hr>
      <h3>User - Trophies</h3>
      <TrophyList></TrophyList>

    </Container>
  );
}

export default App;