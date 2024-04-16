
import React, { useState } from 'react';
import { useEffect } from 'react';

import './ReservationPage.css'

const carsData = [
    { id: 1, type: 'Sedan', drivetrain: 'AWD', available: true, class: 'Economy', name: 'Toyota Camry' },
    { id: 2, type: 'SUV', drivetrain: '4WD', available: false, class: 'Premium', name: 'BMW X5' },
    { id: 3, type: 'Sedan', drivetrain: 'FWD', available: true, class: 'Compact', name: 'Honda Civic' },
    // Add more as needed
  ];

  

  function ReservationPage() {
    const [cars, setCars] = useState(carsData);
    const [type, setType] = useState('');
    const [drivetrain, setDrivetrain] = useState('');
    const [availability, setAvailability] = useState('');
    const [vehicleClass, setVehicleClass] = useState('');
    const handleTypeChange = (event) => {
        setType(event.target.value);
      };
    
      const handleDrivetrainChange = (event) => {
        setDrivetrain(event.target.value);
      };
    
      const handleAvailabilityChange = (event) => {
        setAvailability(event.target.checked);
      };
    
      const handleClassChange = (event) => {
        setVehicleClass(event.target.value);
      };
        
      const handleSubmit = (event) => {
        event.preventDefault();  // Prevent the default form submission
        // You might want to fetch or filter cars here based on selected values
        console.log({ type, drivetrain, available: availability, class: vehicleClass });
      };
    
  
    useEffect(() => {
      const filteredCars = carsData.filter(car => (
        (type ? car.type === type : true) &&
        (drivetrain ? car.drivetrain === drivetrain : true) &&
        (vehicleClass ? car.class === vehicleClass : true) &&
        (availability ? car.available === availability : true)
      ));
      setCars(filteredCars);
    }, [type, drivetrain, vehicleClass, availability]);

    return (
        <div className="reservation-container">
        <h1>Reserve Your Car</h1>
        <form onSubmit={handleSubmit}>
          <select value={type} onChange={handleTypeChange} className="select-input">
            <option value="">Select Type</option>
            <option value="Sedan">Sedan</option>
            <option value="SUV">SUV</option>
          </select>
  
          <select value={drivetrain} onChange={handleDrivetrainChange}>
            <option value="">Select Drivetrain</option>
            <option value="AWD">AWD</option>
            <option value="4WD">4WD</option>
            <option value="FWD">FWD</option>
          </select>
  
          <label>
            <input type="checkbox" checked={availability} onChange={handleAvailabilityChange} /> Available
          </label>
  
          <select value={vehicleClass} onChange={handleClassChange}>
            <option value="">Select Class</option>
            <option value="Economy">Economy</option>
            <option value="Premium">Premium</option>
          </select>
  
          <button type="submit">Filter</button>
        </form>
        <ul>
          {cars.map(car => <li key={car.id}>{car.name}</li>)}
        </ul>
      </div>
      );
    }
    

    
export default ReservationPage;
