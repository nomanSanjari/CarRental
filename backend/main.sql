USE CarRentalDB;

SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS Employee;
DROP TABLE IF EXISTS Vehicle;
DROP TABLE IF EXISTS Rental;
DROP TABLE IF EXISTS Discount;

CREATE TABLE Customer (
    id INT PRIMARY KEY AUTO_INCREMENT,  
    first_name VARCHAR(50) NOT NULL, 
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20),          
    email VARCHAR(100) NOT NULL UNIQUE, 
    password VARCHAR(255) NOT NULL      
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
    vin VARCHAR(17) NOT NULL UNIQUE,  
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    vehicle_class ENUM ('LUXURY', 'ECONOMY'),
    vehicle_type ENUM ('SUV', 'COUPE', 'SEDAN', 'TRUCK'),
    weekly_rate DECIMAL(10,2) NOT NULL,  
    daily_rate DECIMAL(10,2) NOT NULL,
    odometer_reading INT,                 
    drive_train ENUM ('FWD', 'RWD', 'AWD'), 		
    is_available BOOLEAN DEFAULT TRUE    
); 

CREATE TABLE Rental (
    id INT PRIMARY KEY AUTO_INCREMENT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    vehicle_id INT NOT NULL,  
    employee_id INT NOT NULL, 
    customer_id INT NOT NULL,
    discount_id INT NOT NULL,
    
    total_price INT NOT NULL,
    verified BOOLEAN DEFAULT FALSE,
    
    FOREIGN KEY (vehicle_id) REFERENCES Vehicle (id),
    FOREIGN KEY (employee_id) REFERENCES Employee (id),
    FOREIGN KEY (customer_id) REFERENCES Customer (id),
    FOREIGN KEY (discount_id) REFERENCES Discount (id)
);

CREATE TABLE Discount (
	id INT PRIMARY KEY AUTO_INCREMENT,
    discount_type ENUM ('Corporate', 'Employee', 'Customer'),
    discount_percentage int
);

SET FOREIGN_KEY_CHECKS = 1;