import React, { useState } from "react";
import logo from "./logo.svg";
import "./App.css";
import {
  MapContainer,
  TileLayer,
  Marker,
  Popup,
  LayersControl,
  LayerGroup,
  Circle,
  FeatureGroup,
} from "react-leaflet";
import { Container, Row, Col } from "shards-react";

import { EditControl } from "react-leaflet-draw";
import SafaricomFarmersList from "./safcomfarmers/SafaricomFarmersList";

function App() {
  const [center, setCenter] = useState<number[]>([
    -0.9594915139600687, 37.05146055565118,
  ]);
  return (
    <div
      className="row"
      col-xs-12
      style={{
        height: "100vh",
        width: "100%",
        borderWidth: 3,
        borderColor: "red",
        marginTop: 20,
      }}
    >
      <div className="col col-6" style={{ borderWidth: 3, borderColor: "red" }}>
        <SafaricomFarmersList />
      </div>
      <div className="col col-6">
        <MapContainer
          center={[-1.1860016820338626, 34.449603073128934]}
          zoom={13}
          scrollWheelZoom={false}
          style={{ height: "100vh", width: "100%" }}
        >
          <LayersControl position="topright">
            <LayersControl.BaseLayer checked name="Basemap">
              <TileLayer
                attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                url="https://tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png"
              />
            </LayersControl.BaseLayer>
            <LayersControl.BaseLayer checked name="RGB">
              <TileLayer
                attribution='&copy; <a href="http://osm.org/copyright">Deeptech</a> contributors'
                url="http://localhost:8000/raster/algebra/{z}/{x}/{y}.png?layers=r:0=1,g:1=1,b:1=1&alpha=0"
              />
            </LayersControl.BaseLayer>
            <LayersControl.Overlay name="Marker with popup">
              <Marker position={[-1.1860016820338626, 34.449603073128934]}>
                <Popup>
                  A pretty CSS3 popup. <br /> Easily customizable.
                </Popup>
              </Marker>
            </LayersControl.Overlay>
            <LayersControl.Overlay checked name="Layer group with circles">
              <LayerGroup>
                <Circle
                  center={[-1.1860016820338626, 34.449603073128934]}
                  pathOptions={{ fillColor: "blue" }}
                  radius={200}
                />
                <Marker position={[-1.1860016820338626, 34.449603073128934]}>
                  <Popup>
                    A pretty CSS3 popup. <br /> Easily customizable.
                  </Popup>
                </Marker>
              </LayerGroup>
            </LayersControl.Overlay>
            <LayersControl.Overlay name="Feature group">
              <FeatureGroup pathOptions={{ color: "purple" }}>
                <Popup>Popup in FeatureGroup</Popup>
              </FeatureGroup>
              <FeatureGroup>
                <EditControl
                  position="topleft"
                  // onEdited={this._onEditPath}
                  // onCreated={this._onCreate}
                  // onDeleted={this._onDeleted}
                  draw={{
                    rectangle: false,
                  }}
                />
                {/* <Circle center={[51.51, -0.06]} radius={200} /> */}
              </FeatureGroup>
            </LayersControl.Overlay>
          </LayersControl>
        </MapContainer>
      </div>
    </div>
  );
}

export default App;
