
export interface CountryData {
    country: string,
    capital: string,
    region: string
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
    time: number,
    score: number,
    speed: number,
    length: number,
    region: string
}

export interface InputData {
    answer: string,
    valid: boolean,
    timeReaction: number,
    timeTotal: number
}