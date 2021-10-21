// FarmersListItem component

import React from "react";
import {
  Card,
  CardHeader,
  CardTitle,
  CardImg,
  CardBody,
  CardFooter,
  Button,
} from "shards-react";
import { ISafaricomFarmerData } from "../safarcomfarmers";

interface ChildComponentProps {
  farmer: ISafaricomFarmerData;
}

function SafaricomFarmerListItem(props: ChildComponentProps) {
  return (
    <Card style={{ maxWidth: "300px", margin: 30 }}>
      <CardHeader>Farmer Name: {props.farmer.farmer_name}</CardHeader>
      {/* <CardImg src="https://place-hold.it/300x200" /> */}
      <CardBody>
        {/* <CardTitle>{props.farmer.farm_name}</CardTitle> */}
        <p>County: {props.farmer.county}</p>
        <p>Location: {props.farmer.location}</p>

        {props.farmer.is_mapped ? (
          <div>
            <p>Farmer Mapped</p>
          </div>
        ) : (
          <div>
            <p>Farmer Not Mapped</p>
          </div>
        )}

        <p>Acreage: {props.farmer.acreage}</p>
        <hr />
        {props.farmer.has_errors ? (
          <div>
            <p>{props.farmer.error_comments}</p>
          </div>
        ) : null}
      </CardBody>

      <CardFooter>
        <Button>See more &rarr;</Button>
      </CardFooter>
    </Card>
  );
}

export default SafaricomFarmerListItem;
