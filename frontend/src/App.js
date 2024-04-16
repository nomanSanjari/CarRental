// App.js
import React from 'react';
import HomePage from './components/HomePage';
import ReservationPage from './components/ReservationPage'; // Assume this component is created under the components directory

import LoginPage from './components/LoginPage';

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';



function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/reserve" element={<ReservationPage />} />
        <Route path="/login" element={<LoginPage />} /> {/* New route for LoginPage */}
      </Routes>
    </Router>
  );
}


export default App;

