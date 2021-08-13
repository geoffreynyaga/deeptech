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

import { EditControl } from "react-leaflet-draw";

function App() {
  const [center, setCenter] = useState<number[]>([
    -0.9594915139600687, 37.05146055565118,
  ]);
  return (
    <div style={{ borderColor: "red", borderWidth: 5 }}>
      {/* <MapContainer center={[-0.9594915139600687, 37.05146055565118]} zoom={13} scrollWheelZoom={false}>
  <TileLayer
    attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    url="C:/Users/geoff/Desktop/Tiles/{z}/{x}/{y}.png"
  />
  <Marker position={[-0.9594915139600687, 37.05146055565118]}>
    <Popup>
      A pretty CSS3 popup. <br /> Easily customizable.
    </Popup>
  </Marker>
</MapContainer> */}
      <h3>Hi there</h3>
      <MapContainer
        center={[-0.9594915139600687, 37.05146055565118]}
        zoom={13}
        scrollWheelZoom={false}
        style={{ height: "70vh", width: "80%" }}
      >
        <LayersControl position="topright">
          <LayersControl.BaseLayer checked name="Basemap">
            <TileLayer
              attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
              url="https://tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png"
            />
          </LayersControl.BaseLayer>
          <LayersControl.BaseLayer checked name="NDVI">
            <TileLayer
              attribution='&copy; <a href="http://osm.org/copyright">Deeptech</a> contributors'
              url="/Tiles/{z}/{x}/{y}.png"
            />
          </LayersControl.BaseLayer>
          <LayersControl.Overlay name="Marker with popup">
            <Marker position={[-0.9594915139600687, 37.05146055565118]}>
              <Popup>
                A pretty CSS3 popup. <br /> Easily customizable.
              </Popup>
            </Marker>
          </LayersControl.Overlay>
          <LayersControl.Overlay checked name="Layer group with circles">
            <LayerGroup>
              <Circle
                center={[-0.9594915139600687, 37.05146055565118]}
                pathOptions={{ fillColor: "blue" }}
                radius={200}
              />
              <Marker position={[-0.9594915139600687, 37.05146055565118]}>
                <Popup>
                  A pretty CSS3 popup. <br /> Easily customizable.
                </Popup>
              </Marker>
              <LayerGroup>
                {/* <Circle
                  center={[51.51, -0.08]}
                  pathOptions={{ color: "green", fillColor: "green" }}
                  radius={100}
                /> */}
              </LayerGroup>
            </LayerGroup>
          </LayersControl.Overlay>
          <LayersControl.Overlay name="Feature group">
            <FeatureGroup pathOptions={{ color: "purple" }}>
              <Popup>Popup in FeatureGroup</Popup>
              {/* <Circle center={[51.51, -0.06]} radius={200} /> */}
              {/* <Rectangle bounds={rectangle} /> */}
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
      ,
    </div>
  );
}

export default App;
