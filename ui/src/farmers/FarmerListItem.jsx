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

function FarmerListItem(props) {
  return (
    <Card style={{ maxWidth: "300px", margin: 30 }}>
      <CardHeader>{props.farmer.farm_name}</CardHeader>
      {/* <CardImg src="https://place-hold.it/300x200" /> */}
      <CardBody>
        {/* <CardTitle>{props.farmer.farm_name}</CardTitle> */}
        <p>Phone number: {props.farmer.phone_number}</p>
      </CardBody>

      <CardFooter>
        <Button>See more &rarr;</Button>
      </CardFooter>
    </Card>
  );
}

export default FarmerListItem;
