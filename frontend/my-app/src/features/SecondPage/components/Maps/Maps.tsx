import React from 'react'
import { compose, withProps } from 'recompose'
import { withScriptjs, withGoogleMap, GoogleMap, Marker } from 'react-google-maps'

const Maps = compose(
  withProps({
    /**
     * Note: create and replace your own key in the Google console.
     * https://console.developers.google.com/apis/dashboard
     * The key "AIzaSyBkNaAGLEVq0YLQMi-PYEMabFeREadYe1Q" can be ONLY used in this sandbox (no forked).
     */
    googleMapURL:
      'https://maps.googleapis.com/maps/api/js?key=AIzaSyC8NvTbFTV8gttDptmlSFDYe87xgxlG6bw&v=3.exp&libraries=geometry,drawing,places',
    loadingElement: <div style={{ height: '100%' }} />,
    containerElement: <div style={{ height: '770px' }} />,
    mapElement: <div style={{ height: '100%' }} />
  }),
  withScriptjs,
  withGoogleMap
)(() => (
  <GoogleMap defaultZoom={16} defaultCenter={{ lat: 45.035667, lng: 38.976389 }}>
    <Marker position={{ lat: 45.035667, lng: 38.976389 }} />
  </GoogleMap>
))

export default Maps
