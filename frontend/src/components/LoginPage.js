import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
import './LoginPage.css'; // Assuming this file is named LoginPage.css


function LoginPage() {
  const navigate = useNavigate();

  const [formMode, setFormMode] = useState('login');

  const handleLogin = (event) => {
    event.preventDefault();
    navigate('/'); // Navigate to the homepage or dashboard after login
  };

  const toggleFormMode = () => {
    setFormMode(formMode === 'login' ? 'signup' : 'login');
  };

  return (
    <div className="login-page-container">
      <div className="login-container">
        <h2 className="login-title">{formMode === 'login' ? 'LOGIN' : 'SIGN UP'}</h2>
        <form className="login-form" onSubmit={handleLogin}>
          {formMode === 'signup' && (
            <>
              <div className="input-container">
                <input type="text" placeholder="First Name" required />
              </div>
              <div className="input-container">
                <input type="text" placeholder="Last Name" required />
              </div>
              <div className="input-container">
                <input type="tel" placeholder="Phone" required />
              </div>
            </>
          )}
          <div className="input-container">
            <input type="email" placeholder="Email" required />
          </div>
          {formMode === 'login' ? (
            <>
              <div className="input-container">
                <input type="password" placeholder="Password" required />
              </div>
              <div className="remember-me-container">
                <label>
                  <input type="checkbox" id="rememberMe" />
                  Remember me
                </label>
              </div>
            </>
          ) : (
            <div className="input-container">
              <input type="password" placeholder="Create Password" required />
            </div>
          )}
          <button type="submit" className="login-button">
            {formMode === 'login' ? 'LOGIN' : 'SIGN UP'}
          </button>
          {formMode === 'login' ? (
            <p className="signup-link">
              Not a member? <span onClick={toggleFormMode} style={{ color: '#ffcc00', cursor: 'pointer' }}>Sign up now</span>
            </p>
          ) : (
            <p className="signup-link">
              Already a member? <span onClick={toggleFormMode} style={{ color: '#ffcc00', cursor: 'pointer' }}>Login</span>
            </p>
          )}
        </form>
      </div>
    </div>
  );
}

export default LoginPage;
