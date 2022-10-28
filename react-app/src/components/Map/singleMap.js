import React, { useState, useEffect } from 'react'
import {useDispatch, useSelector} from 'react-redux'
import { getKey } from '../../store/businesses';

import {
    StaticGoogleMap,
    Marker,
} from 'react-static-google-map';


const SingleMap = ({ location }) => {
    const dispatch = useDispatch()
    
    const keyObj = useSelector(state => state.businesses.key)

    useEffect(() => {
        dispatch(getKey())
    }, [dispatch])

    let key
    if (keyObj && keyObj.googleMapsApiKey) {
        key = keyObj.googleMapsApiKey
    }


    let locationStr = `${location.lat}, ${location.lng}`

    return (
        <div>
            <StaticGoogleMap size="350x215" className="img-fluid" apiKey={key}>
                <Marker location={locationStr} color="red" />
            </StaticGoogleMap>
        </div>

    )
}

export default SingleMap
