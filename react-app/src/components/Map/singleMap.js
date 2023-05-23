import React from 'react'

import {
    StaticGoogleMap,
    Marker,
} from 'react-static-google-map';


const SingleMap = ({ location }) => {

    let locationStr = `${location.lat}, ${location.lng}`

    return (
        <div>
            <StaticGoogleMap size="350x215" className="img-fluid" apiKey="AIzaSyBDVrc6BbFgeEx6oqsBGrHWOnZszK2uQPI">
                <Marker location={locationStr} color="red" />
            </StaticGoogleMap>
        </div>

    )
}

export default SingleMap
