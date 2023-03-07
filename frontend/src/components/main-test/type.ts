
export interface CountryData {
    country: string,
    capital: string
}

export interface Metrics {
    time: number,
    score: number,
    error: number,
    length: number,
    accuracy: number,
    speed: number
}

export interface TestData {
    time: number | null,
    score: number | null,
    speed: number | null,
    length: number | null,
    region: string | null
}