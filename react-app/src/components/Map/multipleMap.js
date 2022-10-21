import React from 'react'

import {
    StaticGoogleMap,
    Marker,
    Path,
} from 'react-static-google-map';

// let locations = []
// if (biz) {
//     let bizArr
//     if (pageNum === 0) bizArr = Object.values(biz).slice(0, 10)
//     bizArr.map(b => {
//         let locationObj = {}
//         locationObj['lat'] = b.lat
//         locationObj['lng'] = b.lng
//         locations.push(locationObj)
//     })
// }

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
export default MultipleMap
