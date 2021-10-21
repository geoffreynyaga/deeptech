

import { LatLngExpression } from "leaflet";

export interface ISafaricomFarmerData {
  farmer_name: string;
  is_mapped:boolean;
  id_number: null | number;
  phone_number: string;
  address: null;
  location_pin: {
    type: "Point";
    coordinates: LatLngExpression;
  };
  boundary: {
    type: "MultiPolygon";
    coordinates: number[][];
  };
  has_errors: boolean;
  error_comments: string;
  acreage: number ;
  county: string;
  location: string;
  total_acreage_sprayed: number;
  total_acreage_mapped: number;
  date_created: string;
  date_modified: string;
}
