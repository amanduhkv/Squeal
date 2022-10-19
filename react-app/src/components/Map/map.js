
import React from 'react'

import {
    StaticGoogleMap,
    Marker,
    Path,
} from 'react-static-google-map';

const env = require('dotenv')

const Map = ({ location }) => {
    
    let locationStr = `${location.lat}, ${location.lng}`

    return (
        <div>
{/* process.env.API_KEY  */}
            {/* <StaticGoogleMap size="315x250" apiKey={process.env.API_KEY} > */}
            <StaticGoogleMap size="350x215" className="img-fluid" apiKey={process.env.REACT_APP_API_KEY}>
                <Marker location="6.4488387,3.5496361" color="red"/>
            </StaticGoogleMap>
        </div>

    )
}

export default Map
// <div className="google-map" style={{ height: '200px', width: '350px' }}>
//      <StaticGoogleMap
//         bootstrapURLKeys={{ key: 'AIzaSyDlKXZDRxr61aYIh4DphKb3a6m9Si4ryt4' }}
//         center={location}
//         defaultZoom={zoomLevel}
//         >
//         <LocationPin
//             lat={location.lat}
//             lng={location.lng}
//         />
//             </StaticGoogleMap> 
//         </div>