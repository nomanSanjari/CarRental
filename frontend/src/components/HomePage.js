// React import statement, necessary for using React features
import React from 'react';
import { useNavigate } from 'react-router-dom';
// Importing the Slider component and required styles from react-slick
import Slider from 'react-slick';
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

// Importing the main CSS for the homepage
import '../HomePage.css';

// Importing image assets used in the homepage
import carImage from '../carPNG2.png';
import ReservationForm from './ReservationForm';
import locationIcon from '../pin.png';
import calendarIcon from '../calendar.png';
import starIcon from '../star.png';
import specialRatesIcon from '../discount.png';
import mobilePhoneIcon from '../phoneReserve.png';
import unlimitedMileageIcon from '../mileage.png';
import damageWaiverIcon from '../damage.png';
import aboutImage from '../aboutUS.jpg';

// Settings for the react-slick Slider component
const settings = {
  dots: true,
  infinite: true,
  speed: 500,
  slidesToShow: 1,
  slidesToScroll: 1,
  autoplay: true,
  autoplaySpeed: 3000,
  pauseOnDotsHover: true,
  cssEase: "linear"
};

// Sample testimonials
const testimonials = [
    {
        quote: "It is always a positive experience when renting from your 5th street location. The staff is very professional and efficient and always smiling. And I always feel welcome and appreciated. The management is always prompt to solve any issue at any moment. Their efficiency and professionalism makes it my number one choice.",
        author: "Micheal Neel",
        location: "Yellowknife NWT"
      },
      {
        quote: "The customer service at this location is outstanding! Every time I rent a car, the process is smooth and straightforward. Highly recommended for anyone needing a reliable rental.",
        author: "Jane Smith",
        location: "Edmonton AB"
      },
      {
        quote: "It is always a positive experience when renting from your 5th street location. The staff is very professional and efficient and always smiling. And I always feel welcome and appreciated. The management is always prompt to solve any issue at any moment. Their efficiency and professionalism makes it my number one choice.",
        author: "Jon Doe",
        location: "Winnipeg MB"
      },
      {
        quote: "The customer service at this location is outstanding! Every time I rent a car, the process is smooth and straightforward. Highly recommended for anyone needing a reliable rental.",
        author: "Jennifer Wood",
        location: "Kelowna BC"
      },
];

// Functional component for the Homepage
function HomePage() {

    // Get the current year for the copyright in the footer
    const currentYear = new Date().getFullYear(); 

    const navigate = useNavigate();  // Hook to access navigate function

    const handleLoginClick = () => {
      navigate('/login');  // Navigate to the login page
    };
  

  return (
    <div className="home">
        {/* Navigation bar with links and a login button */}
      <nav className="navbar"> 
        {/* Logo for the car rental company*/}
        <span className="logo">CAR RENTAL</span> 

        {/*Navigation links to sections of the homepage */}
        <div className="nav-links">
          <a href="#home">Home</a>
          <a href="#about">About</a>
          <a href="#testimonials">Testimonials</a>
          <a href="#contact">Contact</a>
        </div>
        {/*Login button for user authentication */}
        <button className="login-button" onClick={handleLoginClick}>Login</button>
      </nav>

      {/* Promotional section displaying the reservation form and car image */}
      <div className="promo-section">
        <div className="reservation-and-car">

            {/*Import of the ReservationForm component */}
          <ReservationForm />
          <img src={carImage} alt="Car" className="car-image" />
        </div>
      </div>
      
      {/*  Section highlighting customer services provided by the company*/}
      <section className="customer-services">
        <h2>Customer Service</h2>
        <p className="subheading">Best customer service in the world</p>
        {/*Decorative underline for the section title */}
        <div className="highlight-line"></div> 
        <div className="service-boxes">

            {/*Individual service boxes with icon and description */}
        <div className="service-box">
                <img src={mobilePhoneIcon} alt="Mobile reservation" />
                <h3>Mobile Phone Reservation</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit...</p>
        </div>
        <div className="service-box">
                <img src={unlimitedMileageIcon} alt="Unlimited mileage" />
                <h3>Unlimited Mileage</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit...</p>
        </div>
        <div className="service-box">
                <img src={specialRatesIcon} alt="Special rates" />
                <h3>Special rates on car booking</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit...</p>
        </div>
        <div className="service-box">
                <img src={damageWaiverIcon} alt="Damage waiver" />
                <h3>Damage Waiver</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit...</p>
        </div>
        </div>
        </section>

        {/*About section providing details about the company */}
        <section id="about" className="about-section">
        <img src={aboutImage} alt="About Company" className="about-image" />
        <div className="about-details">
            {/* Title for the about section with a highlight underneath*/}
          <div className="about-title-container">
            <h2 className="about-title">About Company</h2>
            <div className="about-highlight"></div> 
          </div>
          {/*Main heading for the about section */}
          <h1 className="about-heading">You start the engine and your adventure begins</h1>
          <p className="about-text">
            {/* Detailed company description and philosophy*/}
          Welcome to Car Rental, the place where every mile is filled with moments, every turn brings excitement, 
          and every journey begins with reliability. Nestled in the heart of the community for over a decade, we pride ourselves on fueling adventures with a diverse fleet of vehicles to suit any traveler's needs.
          From the bustling city streets to serene country roads, our cars have traversed every path you can imagine, powered by a commitment to impeccable service and unbeatable value. We believe that the best stories are found between the pages of a passport and the journey on the road. Whether you're a frequent traveler or setting out for the occasional getaway, our dedicated team is here to ensure that your rental experience is seamless, comfortable, and tailored to the adventure that awaits.
          </p>
          
        </div>
      </section>

        {/*Testimonials section for customer reviews */}
      <section id="testimonials" className="testimonial-section">
        <h2 className="testimonials-title">Testimonials</h2>
        <div className="testimonials-rectangle"></div> {/*  rectangle */}
        {/*Slider component to display testimonials in a carousel */}
        <Slider {...settings}>
          {testimonials.map((testimonial, index) => (
            <div key={index} className="testimonial-container">
              <div className="testimonial-stars">
                {/* Mapping through the testimonials array to display each testimonial*/}
                {[...Array(5)].map((_, i) => (
                  <img key={i} src={starIcon} alt="Star" className="star" />
                ))}
              </div>
              <blockquote>{testimonial.quote}</blockquote>
              {/*Author and location of the testimonial, styled with the company color */}
              <p className="testimonial-author" style={{ color: "#ffcc00" }}>
                — {testimonial.author}, {testimonial.location}
              </p>
            </div>
          ))}
        </Slider>
      </section>


      {/* Contact section with a form for inquiries*/}
      <section id="contact" className="contact-section">
        {/*Title for the contact section with an underline */}
        <div className="contact-header">
        <h2 className="contact-title">Contact Us</h2>
        <div className="contact-title-underline"></div>
        </div>
        <p>You have any questions or need additional information?</p>
        <p><strong>Address:</strong> Car Rental / 1234 5th Avenue / Calgary, AB T3H 9B3</p>
        
        {/*The form for users to submit their contact information and message */}
        <form className="contact-form">
          <div className="input-row">
            {/* Inputs for name, telephone, and email, arranged in rows*/}
            <input type="text" placeholder="First Name" />
            <input type="text" placeholder="Last Name" />
          </div>
          <div className="input-row">
            <input type="tel" placeholder="Telephone" />
            <input type="email" placeholder="Email" />
          </div>
          <textarea placeholder="Message"></textarea>
          {/* Button to submit the contact form*/}
          <button type="submit" className="submit-button">SUBMIT MESSAGE</button>
        </form>
      </section>
        
        {/* Button to submit the contact form*/}
      <footer className="site-footer">
        <p>Car Rental © {currentYear} All Rights Reserved</p>
      </footer>


    </div>
  );
}



// Exporting HomePage component for use in other parts of the app
export default HomePage;

