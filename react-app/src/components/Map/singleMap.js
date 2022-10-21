import React from 'react'

import {
    StaticGoogleMap,
    Marker,
    Path,
} from 'react-static-google-map';

const env = require('dotenv')

const SingleMap = ({ location }) => {
    
    let locationStr = `${location.lat}, ${location.lng}`
    
    return (
        <div>
            <StaticGoogleMap size="350x215" className="img-fluid" apiKey="AIzaSyCLdszu6GiovZNBOUIM4WxYqcVB9EP9Zxo">
                <Marker location={locationStr} color="red"/>
            </StaticGoogleMap>
        </div>

    )
}

export default SingleMap
