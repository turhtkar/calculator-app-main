import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './contexts/AuthContext';
import Login from './components/Login/Login';
import Register from './components/Register/Register';
import Calculator from './components/Calculator/Calculator';

const PrivateRoute = ({ children }) => {
  const { token } = useAuth();
  return token ? children : <Navigate to="/login" replace />;
};

function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route 
            path="/calculator" 
            element={
              <PrivateRoute>
                <Calculator />
              </PrivateRoute>
            } 
          />
          <Route path="/" element={<Navigate to="/calculator" replace />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;