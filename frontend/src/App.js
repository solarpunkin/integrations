import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import ManageRoute from './components/ManageRoute';
import BusDashboard from './components/BusDashboard';
import Chat from './components/Chat';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <div className="main-content">
          <nav>
            <ul>
              <li>
                <Link to="/manage-route">Manage Route</Link>
              </li>
              <li>
                <Link to="/bus-dashboard">Bus Dashboard</Link>
              </li>
            </ul>
          </nav>
          <Routes>
            <Route path="/manage-route" element={<ManageRoute />} />
            <Route path="/bus-dashboard" element={<BusDashboard />} />
          </Routes>
        </div>
        <div className="chat-widget">
          <Chat />
        </div>
      </div>
    </Router>
  );
}

export default App;
