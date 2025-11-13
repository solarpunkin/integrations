import React, { useState, useEffect } from 'react';
import './ManageRoute.css';

const ManageRoute = () => {
    const [routes, setRoutes] = useState([]);

    useEffect(() => {
        fetch('/api/routes')
            .then(response => response.json())
            .then(data => setRoutes(data.routes));
    }, []);

    return (
        <div className="manage-route-container">
            <h1>Manage Routes</h1>
            <table className="manage-route-table">
                <thead>
                    <tr>
                        <th>Route ID</th>
                        <th>Route Name</th>
                        <th>Direction</th>
                        <th>Shift Time</th>
                        <th>Start Point</th>
                        <th>End Point</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {routes.map(route => (
                        <tr key={route.route_id}>
                            <td>{route.route_id}</td>
                            <td>{route.route_display_name}</td>
                            <td>{route.direction}</td>
                            <td>{route.shift_time}</td>
                            <td>{route.start_point}</td>
                            <td>{route.end_point}</td>
                            <td>{route.status}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default ManageRoute;
