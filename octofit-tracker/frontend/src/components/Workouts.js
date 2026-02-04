import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
    console.log('Fetching workouts from API endpoint:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Fetched workouts data:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        console.log('Processed workouts array:', workoutsData);
        setWorkouts(workoutsData);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching workouts:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return (
    <div className="container mt-4">
      <div className="loading-container">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
        <p className="mt-3">Loading workouts...</p>
      </div>
    </div>
  );
  
  if (error) return (
    <div className="container mt-4">
      <div className="error-container">
        <h3>⚠️ Error</h3>
        <p>{error}</p>
      </div>
    </div>
  );

  const getDifficultyBadge = (difficulty) => {
    const badges = {
      'beginner': <span className="badge bg-success">🟢 Beginner</span>,
      'intermediate': <span className="badge bg-warning">🟡 Intermediate</span>,
      'advanced': <span className="badge bg-danger">🔴 Advanced</span>
    };
    return badges[difficulty?.toLowerCase()] || <span className="badge bg-secondary">{difficulty}</span>;
  };

  return (
    <div className="container mt-4">
      <div className="page-header">
        <h1>💪 Workouts</h1>
        <p className="lead">Personalized workout plans to help you reach your goals</p>
      </div>

      <div className="d-flex justify-content-between align-items-center mb-3">
        <h5>Total Workouts: <span className="badge bg-primary">{workouts.length}</span></h5>
        <button className="btn btn-success">+ Create Workout</button>
      </div>

      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th>#</th>
              <th>User</th>
              <th>Workout Name</th>
              <th>Description</th>
              <th>Difficulty</th>
              <th>Duration</th>
              <th>Date Created</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {workouts.map((workout, index) => (
              <tr key={workout.id}>
                <td><strong>{index + 1}</strong></td>
                <td><span className="badge bg-secondary">{workout.user}</span></td>
                <td><strong>{workout.name}</strong></td>
                <td>{workout.description}</td>
                <td>{getDifficultyBadge(workout.difficulty_level)}</td>
                <td><span className="badge badge-duration">{workout.duration} min</span></td>
                <td>{new Date(workout.created_at).toLocaleDateString()}</td>
                <td>
                  <button className="btn btn-sm btn-outline-primary me-1">Start</button>
                  <button className="btn btn-sm btn-outline-success me-1">View</button>
                  <button className="btn btn-sm btn-outline-secondary">Edit</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Workouts;
