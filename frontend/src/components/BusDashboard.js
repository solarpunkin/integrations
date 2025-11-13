import React, { useState, useEffect } from 'react';
import './BusDashboard.css';

const BusDashboard = () => {
    const [trips, setTrips] = useState([]);

    useEffect(() => {
        fetch('/api/daily-trips')
            .then(response => response.json())
            .then(data => setTrips(data.trips));
    }, []);

    return (
        <div className="bus-dashboard-container">
            <h1>Bus Dashboard</h1>
            <table className="bus-dashboard-table">
                <thead>
                    <tr>
                        <th>Trip ID</th>
                        <th>Display Name</th>
                        <th>Booking Status</th>
                        <th>Live Status</th>
                    </tr>
                </thead>
                <tbody>
                    {trips.map(trip => (
                        <tr key={trip.trip_id}>
                            <td>{trip.trip_id}</td>
                            <td>{trip.display_name}</td>
                            <td>{trip.booking_status_percentage * 100}%</td>
                            <td>{trip.live_status}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default BusDashboard;
