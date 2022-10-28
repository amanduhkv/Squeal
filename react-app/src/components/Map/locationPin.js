import React from 'react'
import location from '../../icons/location.svg'

const LocationPin = ({ text }) => {
    return (
        <div className="pin">
            <img src={location} height='24px' width='24px' className="pin-icon" onError={e => e.target.src=brokenImgPig} />
        </div>
    )
}

export default LocationPin
