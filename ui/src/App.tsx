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
import FarmersList from "./farmers/FarmersList";

function App() {
  const [center, setCenter] = useState<number[]>([
    -0.9594915139600687, 37.05146055565118,
  ]);
  return (
    <Container
      style={{
        height: "100vh",
        width: "100%",
        borderWidth: 3,
        borderColor: "red",
        marginTop: 20,
      }}
    >
      <Row
        style={{
          height: "100vh",
          width: "100%",
          borderWidth: 3,
          borderColor: "blue",
          marginTop: 20,
        }}
      >
        <Col xs={12} sm={12} md={4} lg={4}>
          <FarmersList />
        </Col>
        <Col
          xs={12}
          sm={12}
          md={8}
          lg={8}
          style={{ borderWidth: 3, borderColor: "red" }}
        >
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
        </Col>
      </Row>
    </Container>
  );
}

export default App;
