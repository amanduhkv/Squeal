import React from 'react'
import GoogleMapReact from 'google-map-react'
import LocationPin from './locationPin'

const Map = ({ location, zoomLevel }) => {
    return (

            <div className="google-map" style={{ height: '200px', width: '350px' }}>
                <GoogleMapReact
                    bootstrapURLKeys={{ key: 'AIzaSyDlKXZDRxr61aYIh4DphKb3a6m9Si4ryt4' }}
                    center={location}
                    defaultZoom={zoomLevel}
                    >
                    <LocationPin
                        lat={location.lat}
                        lng={location.lng}
                    />
                        </GoogleMapReact>
                    </div>
    )
}

export default Map