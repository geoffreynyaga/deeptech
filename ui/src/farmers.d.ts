
import { GeoJsonObject } from "geojson";
import { LatLngExpression } from "leaflet";

export interface IFarmerData {
  id: number;
  type: "Feature";
  geometry: {
    type: "Point";
    coordinates: LatLngExpression;
  };
  properties: {
    farm_name: string;
    id_number: number | null;
    phone_number: string | null;
    address: string | null;
    acreage: number | null;
    pin_number: string | null;
    county: string;
    sub_county: string;
    ward: string | null;
    boundary: {
      type: "MultiPolygon";
      coordinates: number[][];
    };
    plots: GeoJsonObject;
  };
}
