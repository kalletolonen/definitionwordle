import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from 'react';

function App() {

const list = []

function alphabet() {
	var abc = "abccdefghijklmnopqrstuxyz"
	for (var i=0;i < abc.length; i++) {
		list.push(abc[i])
	}
}

alphabet()
//console.log(list)
const jsonData= require('./data/a.json'); 

console.log(jsonData)


  return (
    <div className="App">
    Howdy
    </div>
  );
}

export default App;
