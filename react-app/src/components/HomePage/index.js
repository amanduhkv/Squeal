import React from 'react';
import './HomePage.css';

const HomePage = () => {
  return (
    <div className='homepage-container'>
        <div className='recent-activity-container'>
            <h2 className='recent-activity-title'>
                Recent Activity
            </h2>
        </div>
        <div className='category-type-container'>
            <h2 className='category-type-title'>
                Categories
            </h2>
        </div>
    </div>
  )
}

export default HomePage
