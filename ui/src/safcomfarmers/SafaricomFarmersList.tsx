// react component for displaying a list of farmer

import React, { useState, useEffect } from "react";
// import { Link } from 'react-router-dom';
import { Container, Row } from "shards-react";

import SafaricomFarmerListItem from "./SafaricomFarmerListItem";
import { ISafaricomFarmerData } from "../safarcomfarmers";

function SafaricomFarmersList(props: any) {
  const [farmers, setFarmers] = useState<ISafaricomFarmerData[] | null>(null);

  // fetch farmers
  useEffect(() => {
    fetchFarmers();
  }, []);

  const fetchFarmers = () => {
    fetch("http://localhost:8000/api/farmers/safaricom/list/", {
      method: "GET",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        Authorization: "Token 437e40ad5b38ebb77ef53458cf764b3db33b8b67",
      },
    })
      .then((res) => res.json())
      .then((data) => {
        setFarmers(data.results);
      });
  };

  return (
    <div className="col-xs-12" style={{ borderWidth: 3, borderColor: "red" }}>
      <table className="meta-table">
        <thead>
          <tr>
            <th>Prop</th>
            <th>Description</th>
            <th>Type</th>
            <th>Default</th>
            <th>Required</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td data-label="Prop">
              <strong>className</strong>
            </td>
            <td data-label="Description">The className name.</td>
            <td data-label="Type">
              <code className="mr-1">String</code>
            </td>
            <td data-label="Default">-</td>
            <td data-label="Required">No</td>
          </tr>
          <tr>
            <td data-label="Prop">
              <strong>flush</strong>
            </td>
            <td data-label="Description">
              Whether the list group should be flushed, or not.
            </td>
            <td data-label="Type">
              <code className="mr-1">Bool</code>
            </td>
            <td data-label="Default">-</td>
            <td data-label="Required">No</td>
          </tr>
          <tr>
            <td data-label="Prop">
              <strong>small</strong>
            </td>
            <td data-label="Description">
              Whether the list group is small, or not.
            </td>
            <td data-label="Type">
              <code className="mr-1">Bool</code>
            </td>
            <td data-label="Default">-</td>
            <td data-label="Required">No</td>
          </tr>
          <tr>
            <td data-label="Prop">
              <strong>tag</strong>
            </td>
            <td data-label="Description">The component's tag type.</td>
            <td data-label="Type">
              <code className="mr-1">Func</code>
              <code className="mr-1">String</code>
            </td>
            <td data-label="Default">
              <code>"ul"</code>
            </td>
            <td data-label="Required">No</td>
          </tr>
        </tbody>
      </table>

      <div className="col-xs-12">
        <h4>Farmers List</h4>
        {/* <pre>{farmers !== null ? JSON.stringify(farmers) : "no farmers"}</pre> */}
        <div>
          {farmers !== null && farmers !== undefined ? (
            <ul className="collection">
              {farmers !== null &&
                farmers.map((farmer) => (
                  <SafaricomFarmerListItem
                    key={farmer.farmer_name}
                    farmer={farmer}
                  />
                ))}
            </ul>
          ) : (
            <p>No farmers</p>
          )}
        </div>
      </div>
    </div>
  );
}

export default SafaricomFarmersList;
