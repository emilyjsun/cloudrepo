import logo from './logo.svg';
import './App.css';
import Fruit from './fruit';
import FruitClass from './FruitClass.js';
import React, { useState } from 'react';
import { BrowserRouter, Routes, Route } from "react-router-dom";




function App() {
  const [fruit, setFruit] = useState('apple');
  return (
    <BrowserRouter>
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="blogs" element={<Blogs />} />
        <Route path="contact" element={<Contact />} />
        <Route path="*" element={<NoPage />} />
      </Route>
    </Routes>
  </BrowserRouter>


    // <div className="App">
    //   <Fruit fruit={fruit} changeFruit={setFruit}/>
    //   {/* <FruitClass fruit={fruit}/> */}
    // </div>
  );
}

export default App;
