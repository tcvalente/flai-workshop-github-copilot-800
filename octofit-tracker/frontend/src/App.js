import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Users from './components/Users';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Workouts from './components/Workouts';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
          <div className="container-fluid">
            <Link className="navbar-brand" to="/">
              <img src="/octofit-logo.svg" alt="OctoFit Tracker" className="navbar-logo" />
            </Link>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav ms-auto">
                <li className="nav-item">
                  <Link className="nav-link" to="/">🏠 Home</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/users">👥 Users</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">🏃 Activities</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">🏆 Leaderboard</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">👫 Teams</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">💪 Workouts</Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <div className="container-fluid py-4">
          <Routes>
            <Route path="/" element={
              <div className="container">
                <div className="hero-section">
                  <h1>🏋️ Welcome to OctoFit Tracker</h1>
                  <p className="lead">Track your fitness activities, compete with your team, and achieve your goals!</p>
                  <div>
                    <Link to="/activities" className="btn btn-light btn-lg mx-2">Start Tracking</Link>
                    <Link to="/leaderboard" className="btn btn-outline-light btn-lg mx-2">View Leaderboard</Link>
                  </div>
                </div>
                
                <div className="row mt-4">
                  <div className="col-md-4">
                    <div className="fitness-card text-center">
                      <h3>🏃 Track Activities</h3>
                      <p>Log your runs, workouts, and fitness activities to monitor your progress</p>
                      <Link to="/activities" className="btn btn-primary mt-2">View Activities</Link>
                    </div>
                  </div>
                  <div className="col-md-4">
                    <div className="fitness-card text-center">
                      <h3>👫 Join Teams</h3>
                      <p>Connect with friends and colleagues to stay motivated together</p>
                      <Link to="/teams" className="btn btn-primary mt-2">Browse Teams</Link>
                    </div>
                  </div>
                  <div className="col-md-4">
                    <div className="fitness-card text-center">
                      <h3>🏆 Compete</h3>
                      <p>Climb the leaderboard and prove you're the ultimate fitness champion</p>
                      <Link to="/leaderboard" className="btn btn-primary mt-2">See Rankings</Link>
                    </div>
                  </div>
                </div>
              </div>
            } />
            <Route path="/users" element={<Users />} />
            <Route path="/activities" element={<Activities />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
            <Route path="/teams" element={<Teams />} />
            <Route path="/workouts" element={<Workouts />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
