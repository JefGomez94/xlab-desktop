import React, { useEffect } from 'react';
import { Navigate, useNavigate } from 'react-router-dom';
import { checkTokenValidity } from '../service/AuthService';

export function PrivateRoute({ children }) {
  const navigate = useNavigate();
  const token = localStorage.getItem('token');
  
  useEffect(() => {
    const validateToken = async () => {
      const isValid = await checkTokenValidity();
      if (!isValid) {
        navigate('/', { replace: true });
      }
    };
    
    if (token) {
      validateToken();
    }
  }, [navigate]);

  return token ? children : <Navigate to="/" replace />;
}