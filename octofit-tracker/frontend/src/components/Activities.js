import React, { useEffect, useState } from 'react';

function Activities() {
    const [activities, setActivities] = useState([]);

    useEffect(() => {
        fetch('https://shiny-space-happiness-6wjqvpgw4gqc4xrj-8000.app.github.dev/api/activity')
            .then(response => response.json())
            .then(data => setActivities(data));
    }, []);

    return (
        <div>
            <h1 className="text-center">Activities</h1>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th>Activity Type</th>
                        <th>Duration</th>
                    </tr>
                </thead>
                <tbody>
                    {activities.map(activity => (
                        <tr key={activity._id}>
                            <td>{activity.activity_type}</td>
                            <td>{activity.duration}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default Activities;