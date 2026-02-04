import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
    console.log('Fetching leaderboard from API endpoint:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Fetched leaderboard data:', data);
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        console.log('Processed leaderboard array:', leaderboardData);
        setLeaderboard(leaderboardData);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching leaderboard:', error);
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
        <p className="mt-3">Loading leaderboard...</p>
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

  const getRankBadge = (rank) => {
    if (rank === 1) return <span className="badge badge-rank-1">🥇 1st</span>;
    if (rank === 2) return <span className="badge badge-rank-2">🥈 2nd</span>;
    if (rank === 3) return <span className="badge badge-rank-3">🥉 3rd</span>;
    return <span className="badge bg-secondary">{rank}th</span>;
  };

  return (
    <div className="container mt-4">
      <div className="page-header">
        <h1>🏆 Leaderboard</h1>
        <p className="lead">See who's dominating the fitness game!</p>
      </div>

      <div className="row mb-4">
        <div className="col-md-4">
          <div className="stats-card" style={{background: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)'}}>
            <h3>{leaderboard.length}</h3>
            <p>Total Competitors</p>
          </div>
        </div>
        <div className="col-md-4">
          <div className="stats-card" style={{background: 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)'}}>
            <h3>{leaderboard[0]?.total_points || 0}</h3>
            <p>Top Score</p>
          </div>
        </div>
        <div className="col-md-4">
          <div className="stats-card" style={{background: 'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)'}}>
            <h3>{leaderboard[0]?.user || 'N/A'}</h3>
            <p>Current Leader</p>
          </div>
        </div>
      </div>

      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th>Rank</th>
              <th>User</th>
              <th>Team</th>
              <th>Total Points</th>
              <th>Last Updated</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.map((entry, index) => (
              <tr key={entry.id} className={index < 3 ? 'table-warning' : ''}>
                <td>{getRankBadge(index + 1)}</td>
                <td>
                  <strong>{entry.user}</strong>
                  {index === 0 && <span className="ms-2">👑</span>}
                </td>
                <td>
                  {entry.team ? <span className="badge bg-info">{entry.team}</span> : <span className="text-muted">No Team</span>}
                </td>
                <td>
                  <span className="badge badge-points" style={{fontSize: '1rem'}}>
                    {entry.total_points} pts
                  </span>
                </td>
                <td>{new Date(entry.last_updated).toLocaleDateString()}</td>
                <td>
                  <button className="btn btn-sm btn-outline-primary">View Profile</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Leaderboard;
