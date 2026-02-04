import React, { useState, useEffect } from 'react';

function Users() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;
    console.log('Fetching users from API endpoint:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Fetched users data:', data);
        // Handle both paginated (.results) and plain array responses
        const usersData = data.results || data;
        console.log('Processed users array:', usersData);
        setUsers(usersData);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching users:', error);
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
        <p className="mt-3">Loading users...</p>
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
        <h1>👥 Users</h1>
        <p className="lead">Manage and view all OctoFit community members</p>
      </div>

      <div className="d-flex justify-content-between align-items-center mb-3">
        <h5>Total Users: <span className="badge bg-primary">{users.length}</span></h5>
        <button className="btn btn-success">+ Add User</button>
      </div>

      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th>#</th>
              <th>Username</th>
              <th>Full Name</th>
              <th>Email</th>
              <th>Team</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {users.map((user, index) => (
              <tr key={user.id}>
                <td><strong>{index + 1}</strong></td>
                <td><span className="badge bg-secondary">{user.username}</span></td>
                <td>{user.first_name} {user.last_name}</td>
                <td>{user.email}</td>
                <td>{user.team ? <span className="badge bg-info">{user.team}</span> : <span className="text-muted">No Team</span>}</td>
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

export default Users;
