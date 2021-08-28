// react component for displaying a list of farmer

import React, { useState, useEffect } from "react";
// import { Link } from 'react-router-dom';
import { Container, Row, Col } from "shards-react";

import FarmerListItem from "./FarmerListItem";

function FarmersList(props) {
  const [farmers, setFarmers] = useState(null);

  // fetch farmers
  useEffect(() => {
    fetchFarmers();
  }, []);

  const fetchFarmers = () => {
    fetch("http://localhost:8000/api/farmers/list/", {
      method: "GET",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        Authorization: "Token f2b50e3f2ea08d5cc26a299e8e27d7b2f395dc6f",
      },
    })
      .then((res) => res.json())
      .then((data) => {
        setFarmers(data);
      });
  };

  return (
    <Container className="dr-example-container">
      <Row>
        <div className="row">
          <h4>Farmers List</h4>
          {/* <pre>
              {farmers !== null ? JSON.stringify(farmers) : "no farmers"}
            </pre> */}
          <div>
            {farmers !== null ? (
              <ul className="collection">
                {farmers !== null &&
                  farmers.map((farmer) => (
                    <FarmerListItem key={farmer.id} farmer={farmer} />
                  ))}
              </ul>
            ) : (
              <p>No farmerss</p>
            )}
          </div>
        </div>
      </Row>
    </Container>
  );
}

export default FarmersList;
