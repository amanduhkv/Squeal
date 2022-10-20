import React from 'react'

import {
    StaticGoogleMap,
    Marker,
    Path,
} from 'react-static-google-map';

// let locations = []
// biz.map(biz => {
//     let locationObj = {}
//     locationObj['lat'] = biz.lat
//     locationObj['lng'] = biz.lng
//     locations.push(locationObj)
// })

const env = require('dotenv')

const MultipleMap = ({ locations }) => {

    let markers
    if (locations) {
        markers = locations.map(location => {
            let locationStr = `${location.lat}, ${location.lng}`
            return (
            <Marker location={locationStr} color="red" />
            )
        })
    }

    return (
        <div>
            <StaticGoogleMap size="350x715" className="img-fluid" apiKey={process.env.REACT_APP_API_KEY}>
                {markers}
            </StaticGoogleMap>
        </div>

    )
}
// change to push
export default MultipleMap