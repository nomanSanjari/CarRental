import React from 'react';

import locationIcon from '../pin.png'; // Update with the correct path
import calendarIcon from '../calendar.png'; // Update with the correct path

import { useNavigate } from 'react-router-dom';


import './ReservationForm.css'; // Make sure to create this CSS file in the same folder

function ReservationForm() {

  const navigate = useNavigate();  // Hook to access navigate function

  function handleSubmit(event) {
      event.preventDefault();  // Prevent the default form submission behavior
      navigate('/reserve');  // Navigate to the reservation page
  }

  return (
    <form onSubmit={handleSubmit} className="reservation-form">
      <div className="form-group">
        <select id="carType" name="carType" className="select-car-type">
          <option value="" disabled selected>Select Your Car Type</option>
          <option value="vw-passat">Volkswagen Golf GTI</option>
          <option value="mercedes-glk">Mercedes-Benz GLK</option>
          <option value="bmw-320">BMW 3-series</option>
          <option value="toyota-camry">Toyota Camry</option>
          <option value="audi-a1">Audi A4 S-LINE</option>
          <option value="vw-golf">Toyota Supra</option>
        </select>
      </div>
      
      <div className="form-group location-group">
        <img src={locationIcon} alt="Location" />
        <input type="text" placeholder="Pick-up location" />
      </div>
      
      <div className="form-group location-group">
        <img src={locationIcon} alt="Location" />
        <input type="text" placeholder="Drop-off location" />
      </div>
      
      <div className="form-group datetime-group">
        <img src={calendarIcon} alt="Calendar" />
        <input type="date" />
        <input type="time" />
      </div>
      
      <div className="form-group datetime-group">
        <img src={calendarIcon} alt="Calendar" />
        <input type="date" />
        <input type="time" />
      </div>
      
      <button type="submit" className="reservation-button">CONTINUE CAR RESERVATION</button>
      </form>
  );
}

export default ReservationForm;
