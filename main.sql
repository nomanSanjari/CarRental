USE CarRentalDB;

SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS Employee;
DROP TABLE IF EXISTS Vehicle;

CREATE TABLE Customer (
    id INT PRIMARY KEY AUTO_INCREMENT,  -- Auto-generated ID
    first_name VARCHAR(50) NOT NULL, 
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20),          -- Consider appropriate length for phone numbers
    email VARCHAR(100) NOT NULL UNIQUE, -- Enforce unique emails
    password VARCHAR(255) NOT NULL      -- Store hashed password (important for security)
);

CREATE TABLE Employee (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20)
); 

CREATE TABLE Vehicle (
    id INT PRIMARY KEY AUTO_INCREMENT,
    vin VARCHAR(17) NOT NULL UNIQUE,  -- VINs are usually 17 characters
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    vehicle_class VARCHAR(50),        -- Consider using an 'ENUM' type for controlled values
    weekly_rate DECIMAL(10,2) NOT NULL,  -- Stores prices with 2 decimal places
    daily_rate DECIMAL(10,2) NOT NULL,
    odometer_reading INT,                -- Adapt the datatype if needed 
    is_available BOOLEAN DEFAULT TRUE    -- Add a status field for tracking availability
); 

SET FOREIGN_KEY_CHECKS = 1;