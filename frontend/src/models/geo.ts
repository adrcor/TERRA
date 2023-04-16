export interface Geo {
    country: string,
    capital: string
}

export interface GeoRegion extends Geo {
    region: string
}