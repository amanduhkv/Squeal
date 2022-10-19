import React from 'react'

const Map = ({ location, zoomLevel }) => {
    return (

            <div className="google-map" style={{ height: '200px', width: '350px' }}>
                {/* <StaticGoogleMap
                    bootstrapURLKeys={{ key: 'AIzaSyDlKXZDRxr61aYIh4DphKb3a6m9Si4ryt4' }}
                    center={location}
                    defaultZoom={zoomLevel}
                    >
                    <LocationPin
                        lat={location.lat}
                        lng={location.lng}
                    />
                        </StaticGoogleMap> */}
                    </div>
    )
}

export default Map