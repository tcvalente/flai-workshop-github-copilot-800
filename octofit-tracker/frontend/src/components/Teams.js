import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;
    console.log('Fetching teams from API endpoint:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Fetched teams data:', data);
        // Handle both paginated (.results) and plain array responses
        const teamsData = data.results || data;
        console.log('Processed teams array:', teamsData);
        setTeams(teamsData);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching teams:', error);
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
        <p className="mt-3">Loading teams...</p>
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

  return (
    <div className="container mt-4">
      <div className="page-header">
        <h1>👫 Teams</h1>
        <p className="lead">Join forces and achieve fitness goals together</p>
      </div>

      <div className="d-flex justify-content-between align-items-center mb-3">
        <h5>Total Teams: <span className="badge bg-primary">{teams.length}</span></h5>
        <button className="btn btn-success">+ Create Team</button>
      </div>

      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th>#</th>
              <th>Team Name</th>
              <th>Description</th>
              <th>Created Date</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {teams.map((team, index) => (
              <tr key={team.id}>
                <td><strong>{index + 1}</strong></td>
                <td>
                  <h6 className="mb-0">
                    <span className="badge bg-info">{team.name}</span>
                  </h6>
                </td>
                <td>{team.description}</td>
                <td>{new Date(team.created_at).toLocaleDateString()}</td>
                <td>
                  <button className="btn btn-sm btn-outline-primary me-1">View</button>
                  <button className="btn btn-sm btn-outline-success me-1">Join</button>
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

export default Teams;
