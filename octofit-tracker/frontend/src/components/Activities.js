import React, { useState, useEffect } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;
    console.log('Fetching activities from API endpoint:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Fetched activities data:', data);
        // Handle both paginated (.results) and plain array responses
        const activitiesData = data.results || data;
        console.log('Processed activities array:', activitiesData);
        setActivities(activitiesData);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching activities:', error);
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
        <p className="mt-3">Loading activities...</p>
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

  const getActivityIcon = (type) => {
    const icons = {
      'running': '🏃',
      'cycling': '🚴',
      'swimming': '🏊',
      'walking': '🚶',
      'yoga': '🧘',
      'gym': '🏋️'
    };
    return icons[type?.toLowerCase()] || '💪';
  };

  return (
    <div className="container mt-4">
      <div className="page-header">
        <h1>🏃 Activities</h1>
        <p className="lead">Track your fitness journey and stay motivated</p>
      </div>

      <div className="d-flex justify-content-between align-items-center mb-3">
        <h5>Total Activities: <span className="badge bg-primary">{activities.length}</span></h5>
        <button className="btn btn-success">+ Log Activity</button>
      </div>

      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th>#</th>
              <th>User</th>
              <th>Activity Type</th>
              <th>Duration</th>
              <th>Distance</th>
              <th>Calories</th>
              <th>Date</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {activities.map((activity, index) => (
              <tr key={activity.id}>
                <td><strong>{index + 1}</strong></td>
                <td><span className="badge bg-secondary">{activity.user}</span></td>
                <td>
                  {getActivityIcon(activity.activity_type)} {activity.activity_type}
                </td>
                <td><span className="badge badge-duration">{activity.duration} min</span></td>
                <td>{activity.distance} km</td>
                <td><span className="badge badge-calories">{activity.calories_burned} kcal</span></td>
                <td>{new Date(activity.date).toLocaleDateString()}</td>
                <td>
                  <button className="btn btn-sm btn-outline-primary me-1">View</button>
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

export default Activities;
