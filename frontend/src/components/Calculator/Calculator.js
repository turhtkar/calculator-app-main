import React, { useState } from 'react';
import axios from 'axios';
import { useAuth } from '../../contexts/AuthContext';
import { useNavigate } from 'react-router-dom';

function Calculator() {
  const [num1, setNum1] = useState('');
  const [num2, setNum2] = useState('');
  const [operation, setOperation] = useState('add');
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');
  const { token, logout } = useAuth();
  const navigate = useNavigate();

  const handleCalculate = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/calculate', 
        { num1: parseFloat(num1), num2: parseFloat(num2), operation },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      setResult(response.data.result);
      setError('');
    } catch (err) {
      setError('Calculation failed. Please try again.');
    }
  };

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <div>
      <h2>Calculator</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <form onSubmit={handleCalculate}>
        <input type="number" value={num1} onChange={(e) => setNum1(e.target.value)} placeholder="Number 1" required />
        <input type="number" value={num2} onChange={(e) => setNum2(e.target.value)} placeholder="Number 2" required />
        <select value={operation} onChange={(e) => setOperation(e.target.value)}>
          <option value="add">Add</option>
          <option value="subtract">Subtract</option>
          <option value="multiply">Multiply</option>
          <option value="divide">Divide</option>
        </select>
        <button type="submit">Calculate</button>
      </form>
      {result !== null && <p>Result: {result}</p>}
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
}

export default Calculator;